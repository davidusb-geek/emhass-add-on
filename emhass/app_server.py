#!/usr/bin/python

from flask import Flask, make_response, render_template
from pathlib import Path
import os, json

OPTIONS = "/data/options.json"
options_json = Path(OPTIONS)
# Read options info
if options_json.exists():
    with options_json.open('r') as data:
        options = json.load(data)
    seconds_to_publish_data = options['seconds_to_publish_data']
    optimization_task_at = options['optimization_task_at']
    opt_task_at_hour = int(optimization_task_at.split(":")[0])
    opt_task_at_minute = int(optimization_task_at.split(":")[1])
else:
    seconds_to_publish_data = None

app = Flask(__name__)

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