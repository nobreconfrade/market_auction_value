from flask import render_template, Blueprint, request

from database import database
from model import CalculatedRatios

views = Blueprint('views', __name__, template_folder='templates')


@views.route('/')
def index() -> any:
    return render_template('index.html')


@views.route('/search', methods=['POST'])
def search() -> any:
    if request.form['id'] == '' or request.form['year'] == '':
        return render_template('index.html', msg='incomplete')
    id = request.form['id']
    year = request.form['year']
    if id not in database.keys():
        return render_template('index.html', msg='id_404')
    schedule = database[id].schedule
    cost = database[id].sale_details.cost
    if year not in schedule.years.keys():
        return render_template('index.html', msg='year_404')
    ratios = schedule.years[year]
    c_market = cost * ratios.market_ration
    c_auction = cost * ratios.auction_ration
    results = CalculatedRatios(c_market, c_auction)
    return render_template('index.html', results=results)
