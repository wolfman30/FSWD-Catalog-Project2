from flask import Flask, render_template, redirect, request 
from flask import url_for, flash, jsonify, session as login_session
import random, string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, AgingHallmark, HallmarkDetails, GlossaryofTerms, References

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json 
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"

app =  Flask(__name__)

#Connects to aginghallmarks.db database and creates session
engine = create_engine('sqlite:///aginghallmarks.db', 
            connect_args = {'check_same_thread': False})
            #connect_args: courtesy of John S from:
            # https://knowledge.udacity.com/questions/7834

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/aging_hallmarks/JSON')
def aging_hallmarksJSON():
    aging_hallmarks = session.query(AgingHallmark).all()
    return jsonify(aging_hallmarks = [a.serialize for a in aging_hallmarks])

@app.route('/')
@app.route('/aging_hallmarks')
def agingHallmarks():
    aging_hallmarks = session.query(AgingHallmark).all()

    return render_template('agingHallmarks.html', 
                                aging_hallmarks = aging_hallmarks)


@app.route('/aging_hallmarks/new', methods = ['GET', 'POST'])
def newHallmark():
    if 'username' not in login_session:
        return redirect('/login')
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
    if 'username' not in login_session:
        return redirect('/login')
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
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        session.delete(markerToDelete)
        session.commit()
        flash("Aging hallmark deleted!")
        return redirect(url_for('agingHallmarks'))
    else:
        return render_template('deleteHallmark.html', hallmark = markerToDelete)

@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details/JSON')
def detailsJSON(hallmark_id):
    hallmark = session.query(AgingHallmark).filter_by(id=hallmark_id).one()
    details = session.query(HallmarkDetails).filter_by(
                    hallmark_id = hallmark_id).all()
    return jsonify(Details = [d.serialize for d in details])

@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details')
def details(hallmark_id):
    hallmark = session.query(AgingHallmark).filter_by(id=hallmark_id).one()
    details = session.query(HallmarkDetails).filter_by(
                    hallmark_id = hallmark_id).all()
    return render_template('details.html', details=details, 
                    hallmark=hallmark, 
                    hallmark_id = hallmark_id)

@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details/new', methods = ['GET', 'POST'])
def newDetail(hallmark_id):
    if 'username' not in login_session:
        return redirect('/login')
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

    return render_template('newDetail.html', aging_hallmarks = aging_hallmark)


@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details/<int:detail_id>/edit',
            methods = ['GET', 'POST'])
def editDetail(hallmark_id, detail_id):
    editedDetail = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        if request.form['name']: 
            editedDetail.name = request.form['name']
        if request.form['description']:
            editedDetail.description = request.form['description']
        session.add(editedDetail)
        session.commit()
        flash("Edited detail!")
        return redirect(url_for('details', hallmark_id=hallmark_id))
    else:
        return render_template('editDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, hallmark_details=editedDetail)

@app.route('/aging_hallmarks/<int:hallmark_id>/hallmark_details/<int:detail_id>/delete', 
            methods = ['GET', 'POST'])
def deleteDetail(hallmark_id, detail_id):
    detail_to_del = session.query(HallmarkDetails).filter_by(id=detail_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        session.delete(detail_to_del)
        session.commit()
        flash("Deleted detail!")
        return redirect(url_for('details', hallmark_id=hallmark_id))
    else:
        return render_template('deleteDetail.html', hallmark_id=hallmark_id, 
                                detail_id=detail_id, hallmark_details=detail_to_del)

@app.route('/aging_hallmarks/glossary/JSON')
def glossaryJSON():
    glossary = session.query(GlossaryofTerms).all()
    return jsonify(Glossary = [g.serialize for g in glossary])
    
@app.route('/aging_hallmarks/glossary')
def glossary():
    glossary = session.query(GlossaryofTerms).all()

    return render_template('glossary.html', glossary = glossary)

@app.route('/aging_hallmarks/glossary/newTerm', methods = ['GET', 'POST'])
def newTerm():
    if 'username' not in login_session:
        return redirect('/login')
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
    if 'username' not in login_session:
        return redirect('/login')
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
    if 'username' not in login_session:
        return redirect('/login')
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


@app.route('/aging_hallmarks/references/JSON')
def referencesJSON():
    references = session.query(References).all()
    return jsonify(References = [r.serialize for r in references])

@app.route('/aging_hallmarks/references')
def references():
    references = session.query(References).all()
    return render_template('references.html', references = references)

@app.route('/aging_hallmarks/references/<int:reference_id>/delete', methods = ['GET', 'POST'])
def deleteReference(reference_id):
    ref_to_del = session.query(
            References).filter_by(id=reference_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        session.delete(ref_to_del)
        session.commit()
        flash("Deleted reference!")
        return redirect(url_for('references'))
    else:
        return render_template('deleteReference.html', reference = ref_to_del, 
                                                  references = references, 
                                                  reference_id = reference_id)

@app.route('/aging_hallmarks/references/<int:reference_id>/edit', methods = ['GET', 'POST'])
def editReference(reference_id):
    ref_to_edit = session.query(
        References).filter_by(id=reference_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        if request.form['name']:
            ref_to_edit.name = request.form['name']
        session.add(ref_to_edit)
        session.commit()
        flash("Edited references!")
        return redirect(url_for('references', reference_id = reference_id))
    else:
        return render_template('editReference.html', reference = ref_to_edit, 
                                references = references, reference_id = reference_id)

@app.route('/aging_hallmarks/references/newReference', methods = ['GET', 'POST'])
def newReference():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newReference = References(name=request.form['name'])
        session.add(newReference)
        session.commit()
        return redirect(url_for('references'))
        flash("Created new reference!")
    else:
        return render_template('newReference.html')

@app.route('/login')
def ShowLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) 
                                        for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods = ['POST'])
def gconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.header['Content-type'] = 'application/json'
        return response
    #Obtains aurhorization code 
    code = request.database

    try:
        #Upgraded the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-type'] = 'application/json'
        return response

    #Check that the access token is valid
    access_token = credential.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
            % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    
    # Aborts if there was an error in the access token.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verifies that the access token is used for the intended user. 
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verifies that the access token is valid for this app 
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Tokens client ID does not match app's."), 401)
        print "Token's client ID does not match app's"
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'), 
                                        200)
        response.headers['Content-Type'] = 'application/json'
        return response

    #Stores the access token in the session for later 
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width:300px; height: 300px; border-radius: 150px; -webkit-border-radius: 150px; -moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output 
#DISCONNECT - Revoke a current user's doken and reset their login_session
@app.route("/gdisconnect")
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(json.dumps('''Current user not 
                            connected.'''), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Execute HTTP GET request to revoke current token. 
    access_token = credentials.access_token 
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token

    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    
    if result['status'] == '200':
        # Reset the user's session.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.header['Content-Type'] = 'application/json'
        return response

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)