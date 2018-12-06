from flask import Flask, render_template, url_for
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
@app.route('/aging_hallmarks/')
def agingHallmarks():
    aging_hallmarks = session.query(AgingHallmark).all()

    return render_template('agingHallmarks.html', 
                                aging_hallmarks = aging_hallmarks)

@app.route('/restaurant/<int:hallmark_id>/edit')
def editHallmark(hallmark_id):
    editedHallmark = session.query(
            AgingHallmark).filter_by(id=hallmark_id).one()
    return render_template('editHallmark.html', hallmark=editedHallmark)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)