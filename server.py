from flask import Flask,render_template,request,redirect,flash,url_for

from utils import load_competitions, load_clubs, update_competition_points, has_event_passed

app = Flask(__name__)
app.secret_key = 'something_special'
app.jinja_env.filters['has_event_passed'] = has_event_passed

competitions = load_competitions()
clubs = load_clubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary',methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        if request.form['email'] == '':
            flash('The email address cannot be empty', 'error')
        else:
            flash('Invalid email address', 'error')

        return render_template('index.html'), 400
    
    return render_template('welcome.html',club=club,competitions=competitions)

@app.route('/book/<competition>/<club>')
def book(competition,club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html',club=foundClub,competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces',methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])

    if placesRequired > int(club['points']):
        flash('You do not have enough points to book that many places.')
        return render_template('booking.html', club=club, competition=competition), 400

    elif placesRequired > 12:
        flash('You cannot book more than 12 places per competition.')
        return render_template('booking.html', club=club, competition=competition), 400

    elif has_event_passed(competition['date']):
        flash('You cannot book places for an event that has already passed.')
        return render_template('booking.html', club=club, competition=competition), 400

    competition['numberOfPlaces'] = str(int(competition['numberOfPlaces'])-placesRequired)
    update_competition_points(competition)
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
