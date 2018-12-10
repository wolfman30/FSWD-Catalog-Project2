from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark, HallmarkDetails

app =  Flask(__name__)

engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
@app.route('/aging_hallmarks')
def agingHallmarks():
    aging_hallmarks = session.query(AgingHallmark).all()

    return render_template('agingHallmarks.html', 
                                aging_hallmarks = aging_hallmarks)

@app.route('/aging_hallmarks/new', methods = ['GET', 'POST'])
def newHallmark():
    if request.method == 'POST':
        marker = AgingHallmark(name=request.form['name'], 
                               summary=request.form['summary'])
        session.add(marker)
        session.commit()
        return redirect(url_for('agingHallmarks'))
    else:
        return render_template('newHallmark.html')

@app.route('/aging_hallmarks/<int:hallmark_id>/edit', methods = ['GET', 'POST'])
def editHallmark(hallmark_id):
    editedHallmark = session.query(
            AgingHallmark).filter_by(id=hallmark_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedHallmark.name = request.form['name']
        elif request.form['summary']:
            editedHallmark.summary = request.form['summary']
        session.add(editedHallmark)
        session.commit()
        return redirect(url_for('agingHallmarks'))
    else:
        return render_template('editHallmark.html', hallmark=editedHallmark)

@app.route('/aging_hallmarks/<int:hallmark_id>/delete', methods = ['GET', 'POST'])
def deleteHallmark(hallmark_id):
    markerToDelete = session.query(
                AgingHallmark).filter_by(id=hallmark_id).one()
    if request.method == 'POST':
        session.delete(markerToDelete)
        session.commit()
        return redirect(url_for('agingHallmarks'))
    else:
        return render_template('deleteHallmark.html', hallmark = markerToDelete)

@app.route('/aging_hallmarks/<int:hallmark_id>/')
@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details')
def hallmarkDetails(hallmark_id):
    hallmark = session.query(AgingHallmark).filter_by(id=hallmark_id).one()
    details = session.query(HallmarkDetails).filter_by(
                    hallmark_id = hallmark_id).all()
    return render_template('details.html', details=details, hallmark=hallmark)

@app.route('/aging_hallmarks/<int:hallmark_id>/detail/<int:detail_id>/edit',
            methods = ['GET', 'POST'])
def editDetail(hallmark_id, detail_id):
    editedDetail = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if request.method == 'POST':
        if request.form['name']: 
            editedDetail = request.form['name']
        if request.form['description']:
            editedDetail.description = request.form['description']
        if request.form['treatment']:
            editedDetail.treatment = request.form['treatment']
        if request.form['references']: 
            editedDetail.references = request.form['references']
        session.add(editedDetail)
        session.commit()
        return redirect(url_for('hallmarkDetails', hallmark_id=hallmark_id))
    else:
        return render_template('editDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, detail=editedDetail)

@app.route('/aging_hallmarks/<int:hallmark_id>/detail/<int:detail_id>/delete', 
            methods = ['GET', 'POST'])
def deleteDetail(hallmark_id, detail_id):
    detailToDetail = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if request.method == 'POST':
        session.delete(detailToDetail)
        session.commit()
        return redirect(url_for('hallmarkDetails', hallmark_id=hallmark_id))
    else:
        return render_template('deleteDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, detail=detailToDetail)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)