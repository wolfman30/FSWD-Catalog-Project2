from flask import Flask, render_template, redirect, request, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark

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

@app.route('/aging_hallmarks/<int:hallmark_id>/edit')
def editHallmark(hallmark_id):
    editedHallmark = session.query(
            AgingHallmark).filter_by(id=hallmark_id).one()
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

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)