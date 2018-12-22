from flask import Flask, render_template, redirect, request 
from flask import url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark, HallmarkDetails, GlossaryofTerms

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
        flash("New aging hallmark created!")
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
        flash("Aging hallmark edited!")
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
        flash("Aging hallmark deleted!")
        return redirect(url_for('agingHallmarks'))
    else:
        return render_template('deleteHallmark.html', hallmark = markerToDelete)

@app.route('/aging_hallmarks/<int:hallmark_id>')
@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details')
def details(hallmark_id):
    hallmark = session.query(AgingHallmark).filter_by(id=hallmark_id).one()
    details = session.query(HallmarkDetails).filter_by(
                    hallmark_id = hallmark_id).all()
    return render_template('details.html', details=details, hallmark=hallmark)

@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_detail/new', methods = ['GET', 'POST'])
def newDetail(hallmark_id):
    if request.method == 'POST':
        newDetail = HallmarkDetails(name=request.form['name'],
                                  description = request.form['description'], 
                                  hallmark_id = hallmark_id)
        session.add(newDetail)
        session.commit()
        return redirect(url_for('details', hallmark_id = hallmark_id))
        flash("Created new detail!")
    else:
        return render_template('newDetail.html', hallmark_id = hallmark_id)

    return render_template('newDetail.html', aging_hallmarks=aging_hallmark)


@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_detail/<int:detail_id>/edit',
            methods = ['GET', 'POST'])
def editDetail(hallmark_id, detail_id):
    editedDetail = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if request.method == 'POST':
        if request.form['name']: 
            editedDetail = request.form['name']
        if request.form['description']:
            editedDetail.description = request.form['description']
        if request.form['references']: 
            editedDetail.references = request.form['references']
        session.add(editedDetail)
        session.commit()
        flash("Edited detail!")
        return redirect(url_for('details', hallmark_id=hallmark_id))
    else:
        return render_template('editDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, hallmark_detail=editedDetail)

@app.route('/aging_hallmarks/<int:hallmark_id>/detail/<int:detail_id>/delete', 
            methods = ['GET', 'POST'])
def deleteDetail(hallmark_id, detail_id):
    detail_to_del = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if request.method == 'POST':
        session.delete(detail_to_del)
        session.commit()
        flash("Deleted detail!")
        return redirect(url_for('hallmarkDetails', hallmark_id=hallmark_id))
    else:
        return render_template('deleteDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, detail=detail_to_del)

@app.route('/aging_hallmarks/glossary')
def glossary():
    glossary = session.query(GlossaryofTerms).all()

    return render_template('glossary.html', glossary = glossary)

@app.route('/aging_hallmarks/glossary/newTerm', methods = ['GET', 'POST'])
def newTerm():
    if request.method == 'POST':
        newTerm = GlossaryofTerms(name=request.form['name'],
                                  definition = request.form['definition'])
        session.add(newTerm)
        session.commit()
        return redirect(url_for('glossary'))
        flash("Created new term!")
    else:
        return render_template('newTerm.html')

@app.route('/aging_hallmarks/glossary/<int:term_id>/delete', methods = ['GET', 'POST'])
def deleteTerm(term_id):
    term_to_del = session.query(
            GlossaryofTerms).filter_by(id=term_id).one()
    if request.method == 'POST':
        session.delete(term_to_del)
        session.commit()
        flash("Deleted term!")
        return redirect(url_for('glossary'))
    else:
        return render_template('deleteTerm.html', term = term_to_del, glossary = glossary, term_id = term_id)


@app.route('/aging_hallmarks/glossary/<int:term_id>/edit', methods = ['GET', 'POST'])
def editTerm(term_id):
    term_to_edit = session.query(
        GlossaryofTerms).filter_by(id=term_id).one()
    if request.method == 'POST':
        if request.form['name']:
            term_to_edit.name = request.form['name']
        elif request.form['definition']:
            term_to_edit.definition = request.form['definition']
        session.add(term_to_edit)
        session.commit()
        flash("Edited term!")
        return redirect(url_for('glossary', term_id = term_id))
    else:
        return render_template('editTerm.html', term = term_to_edit, 
                                glossary = glossary, term_id = term_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)