from flask import Flask,render_template,request,redirect,flash,url_for

from utils import load_competitions, load_clubs, update_points_and_places, has_event_passed, get_usable_points

app = Flask(__name__)
app.secret_key = 'something_special'
app.jinja_env.filters['has_event_passed'] = has_event_passed

competitions = load_competitions()
clubs = load_clubs()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSummary', methods=['POST'])
def show_summary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        if request.form['email'] == '':
            flash('The email address cannot be empty', 'error')
        else:
            flash('Invalid email address', 'error')

        return render_template('index.html'), 400

    return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/book/<competition>/<club>')
def book(competition,club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        usable_points = get_usable_points(found_competition, found_club)
        return render_template('booking.html', club=found_club, competition=found_competition, usable_points=usable_points)
    else:
        flash('Something went wrong-please try again', 'error')
        return render_template('welcome.html', club=club, competitions=competitions)

@app.route('/purchasePlaces',methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    usable_points = get_usable_points(competition, club)

    try:
        places_required = int(request.form['places'])

    except ValueError:
        flash('You can only book between 1 and 12 places.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400

    if has_event_passed(competition['date']):
        flash('You cannot book places for an event that has already passed.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400
    
    elif places_required > competition['numberOfPlaces']:
        flash('The number of reservations requested exceeds the number of available places.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400

    elif places_required < 1:
        flash('You can only book between 1 and 12 places.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400

    elif places_required > club['points']:
        flash('You do not have enough points to book that many places.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400

    elif places_required > 12:
        flash('You cannot book more than 12 places per competition.', 'error')
        return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400
    
    elif club['name'] in competition['clubs']:
        total_place_booked = competition['clubs'][club['name']] + places_required
        if total_place_booked > 12:
            flash('You cannot book more than 12 places per competition.', 'error')
            return render_template('booking.html', club=club, competition=competition, usable_points=usable_points), 400

    competition['numberOfPlaces'] = competition['numberOfPlaces'] - places_required
    club['points'] = club['points'] - places_required
    try:
        competition['clubs'][club['name']] += places_required
    except KeyError:
        competition['clubs'][club['name']] = places_required

    update_points_and_places(competitions, clubs)
    flash('Great-booking complete!', 'success')
    return redirect(url_for('success_purchase', club_email=club['email']))


@app.route('/successPurchase/<club_email>/', methods=['GET'])
def success_purchase(club_email):
    club = [club for club in clubs if club['email'] == club_email][0]
    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/clubPointsBoard', methods=['GET'])
def club_points_board():
    return render_template('club_points_board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)