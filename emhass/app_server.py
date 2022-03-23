#!/usr/bin/python

from flask import Flask, make_response, render_template
from pathlib import Path
import os, json

app = Flask(__name__)

OPTIONS_PATH = "/data/options.json"
options_json = Path(OPTIONS_PATH)
CONFIG_PATH = "/app/config_emhass.json"
config_json = Path(CONFIG_PATH)
# Read options info
if options_json.exists():
    with options_json.open('r') as data:
        options = json.load(data)
    seconds_to_publish_data = options['seconds_to_publish_data']
else:
    app.logger.error("ERROR: options.json does not exists")
# Read example config file
if config_json.exists():
    with config_json.open('r') as data:
        config = json.load(data)
    retrieve_hass_conf = config['retrieve_hass_conf']
    optim_conf = config['optim_conf']
    plant_conf = config['plant_conf']
else:
    app.logger.error("ERROR: config_emhass.json does not exists")
# Build params and params_secrets
# ...

@app.route('/')
def hello():
    app.logger.info("EMHASS server online...")
    app.logger.info("Passed seconds: "+str(seconds_to_publish_data))
    return render_template('index.html')

@app.route('/action/<name>', methods=['POST'])
def action_call(name):
    if name == 'publish-data':
        app.logger.info("Publishing data...")
    elif name == 'dayahead-optim':
        app.logger.info("Performing optimization...")
    else:
        app.logger.error("ERROR: passed action is not valid")

    msg = f'EMHASS >> Action {name} received\n'
    return make_response(msg, 201)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)