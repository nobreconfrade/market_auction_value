import json
import logging

from flask import Flask, render_template

from model import EquipmentSet

app = Flask(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] %(levelname).1s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

# with open('dist/api-response.json') as f:
with open('/home/willpereira/projects/market_auction_value/dist/api-response.json') as f:
    json_data = json.load(f)
    # Since there is no database, I'll duplicate de ID for indexing purposes
    equipment_sets: dict[str, EquipmentSet] = {}
    for id, value in json_data.items():
        equipment_sets[id] = EquipmentSet.json_load(id, value)


@app.route('/')
def index():
    return render_template('index.html')
