#!/usr/bin/python

from flask import Flask, make_response, render_template, request
from flask_caching import Cache
from jinja2 import Environment, FileSystemLoader
from requests import get
from pathlib import Path
import os, json, argparse
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px
from emhass.command_line import setUp
from emhass.command_line import dayahead_forecast_optim
from emhass.command_line import publish_data
from emhass.utils import get_root

def get_injection_dict(df, plot_size = 1366):
    # Create plots
    fig = px.line(df, title='Systems powers and optimization cost results', 
                  template='seaborn', width=plot_size, height=0.75*plot_size)   
    # Load HTML template
    app.logger.info("Look for this path: "+base_path)
    file_loader = FileSystemLoader(base_path+'/templates')
    env = Environment(loader=file_loader)
    template = env.get_template('index.html')
    # Get full path to image
    image_path_0 = fig.to_html(full_html=False, default_width='75%')
    # The tables
    table1 = df.reset_index().to_html(classes='mystyle', index=False)
    # The dict of plots
    injection_dict = {}
    injection_dict['title'] = '<h2>EMHASS optimization results</h2>'
    injection_dict['subsubtitle2'] = '<h4>Plotting latest optimization results</h4>'
    injection_dict['figure_0'] = image_path_0
    injection_dict['subsubtitle1'] = '<h4>Last run optimization results table</h4>'
    injection_dict['table1'] = table1
    # Render HTML template with elements from report
    source_html = template.render(injection_dict=injection_dict)
    return source_html

def get_forecast_dates(freq, delta_forecast, timedelta_days = 0):
    freq = pd.to_timedelta(freq, "minutes")
    start_forecast = pd.Timestamp(datetime.now()).replace(hour=0, minute=0, second=0, microsecond=0)
    end_forecast = (start_forecast + pd.Timedelta(days=delta_forecast)).replace(microsecond=0)
    forecast_dates = pd.date_range(start=start_forecast, 
        end=end_forecast+timedelta(days=timedelta_days)-freq, 
        freq=freq).round(freq)
    return forecast_dates

# Define the Flask instance
app = Flask(__name__, static_url_path='/static')
app.env = "development"

# Define cache instance
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

# Define the paths
OPTIONS_PATH = "/data/options.json"
options_json = Path(OPTIONS_PATH)
CONFIG_PATH = "/usr/src/config_emhass.json"
config_path = Path(CONFIG_PATH)
base_path = str(config_path.parent)
is_prod = True

# Read options info
if options_json.exists():
    with options_json.open('r') as data:
        options = json.load(data)
else:
    app.logger.error("ERROR: options.json does not exists")

# Read example config file
if config_path.exists():
    with config_path.open('r') as data:
        config = json.load(data)
    retrieve_hass_conf = config['retrieve_hass_conf']
    optim_conf = config['optim_conf']
    plant_conf = config['plant_conf']
else:
    app.logger.error("ERROR: config_emhass.json does not exists")

params = {}
params['retrieve_hass_conf'] = retrieve_hass_conf
params['optim_conf'] = optim_conf
params['plant_conf'] = plant_conf
cache.set("params", params)

# The cost function
costfun = options['costfun']

# Initialize this global dict
if is_prod:
    opt_res = pd.read_csv(base_path+'/data/opt_res_dayahead_latest.csv', index_col='timestamp')
else:
    root = get_root(__name__)
    opt_res = pd.read_csv(root / 'data' / 'opt_res_dayahead_latest.csv', index_col='timestamp')
source_html = get_injection_dict(opt_res)
cache.set("source_html", source_html)

@app.route('/')
def index():
    app.logger.info("EMHASS server online, serving index.html...")
    source_html = cache.get("source_html")
    return source_html

@app.route('/action/<name>', methods=['POST'])
def action_call(name):
    params = cache.get("params")
    data = request.get_json(force=True)
    if data is not None:
        forecast_dates = get_forecast_dates(params['retrieve_hass_conf'][0]['freq'], params['optim_conf'][1]['delta_forecast'])
        if 'pv_power_forecast' in data.keys():
            if type(data['pv_power_forecast']) == list and len(data['pv_power_forecast']) < len(forecast_dates):
                params['passed_data']['pv_power_forecast'] = data['pv_power_forecast']
                params['optim_conf'][7]['weather_forecast_method'] = 'list'
            else:
                app.logger.error("ERROR: The passed data is either not a list or the length is not correct, length should be "+str(len(forecast_dates)))
                app.logger.error("Passed type is "+str(type(data['pv_power_forecast']))+" and length is "+str(len(data['pv_power_forecast'])))
        if 'load_power_forecast' in data.keys():
            if type(data['load_power_forecast']) == list and len(data['load_power_forecast']) < len(forecast_dates):
                params['passed_data']['load_power_forecast'] = data['load_power_forecast']
                params['optim_conf'][8]['load_forecast_method'] = 'list'
            else:
                app.logger.error("ERROR: The passed data is either not a list or the length is not correct, length should be "+str(len(forecast_dates)))
                app.logger.error("Passed type is "+str(type(data['load_power_forecast']))+" and length is "+str(len(data['load_power_forecast'])))
        if 'load_cost_forecast' in data.keys():
            if type(data['load_cost_forecast']) == list and len(data['load_cost_forecast']) < len(forecast_dates):
                params['passed_data']['load_cost_forecast'] = data['load_cost_forecast']
                params['optim_conf'][9]['load_cost_forecast_method'] = 'list'
            else:
                app.logger.error("ERROR: The passed data is either not a list or the length is not correct, length should be "+str(len(forecast_dates)))
                app.logger.error("Passed type is "+str(type(data['load_cost_forecast']))+" and length is "+str(len(data['load_cost_forecast'])))
        if 'prod_price_forecast' in data.keys():
            if type(data['prod_price_forecast']) == list and len(data['prod_price_forecast']) < len(forecast_dates):
                params['passed_data']['prod_price_forecast'] = data['prod_price_forecast']
                params['optim_conf'][13]['prod_price_forecast_method'] = 'list'
            else:
                app.logger.error("ERROR: The passed data is either not a list or the length is not correct, length should be "+str(len(forecast_dates)))
                app.logger.error("Passed type is "+str(type(data['prod_price_forecast']))+" and length is "+str(len(data['prod_price_forecast'])))
        cache.set("params", params)
    params = json.dumps(params)
    input_data_dict = setUp(config_path, base_path, costfun, params, app.logger)
    if name == 'publish-data':
        app.logger.info("Publishing data...")
        _ = publish_data(input_data_dict, app.logger)
        return index()
    elif name == 'dayahead-optim':
        app.logger.info("Performing optimization...")
        global source_html
        opt_res = dayahead_forecast_optim(input_data_dict, app.logger)
        source_html = get_injection_dict(opt_res)
        cache.set("source_html", source_html)
        return index()
    else:
        app.logger.error("ERROR: passed action is not valid")
        return index()
    msg = f'EMHASS >> Action {name} received... \n'
    return make_response(msg, 201)

def main():
    # Parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, help='The hass instance url')
    parser.add_argument('--key', type=str, help='Your access key')
    args = parser.parse_args()
    web_ui_url = options['web_ui_url']
    url_from_options = options['hass_url']
    if url_from_options == 'empty':
        hass_url = args.url
        url = hass_url+"/config"
    else:
        hass_url = url_from_options
        url = hass_url+"/api/config"
    token_from_options = options['long_lived_token']
    if token_from_options == 'empty':
        long_lived_token = args.key
    else:
        long_lived_token = token_from_options
    headers = {
        "Authorization": "Bearer " + long_lived_token,
        "content-type": "application/json"
    }
    response = get(url, headers=headers)
    config_hass = response.json()
    params_secrets = {
        'hass_url': hass_url,
        'long_lived_token': long_lived_token,
        'time_zone': config_hass['time_zone'],
        'lat': config_hass['latitude'],
        'lon': config_hass['longitude'],
        'alt': config_hass['elevation']
    }
    # Build params
    params = cache.get("params")
    # Updating variables in retrieve_hass_conf
    params['retrieve_hass_conf'][0]['freq'] = options['optimization_time_step']
    params['retrieve_hass_conf'][1]['days_to_retrieve'] = options['historic_days_to_retrieve']
    params['retrieve_hass_conf'][2]['var_PV'] = options['sensor_power_photovoltaics']
    params['retrieve_hass_conf'][3]['var_load'] = options['sensor_power_load_no_var_loads']
    params['retrieve_hass_conf'][6]['var_replace_zero'] = [options['sensor_power_photovoltaics']]
    params['retrieve_hass_conf'][7]['var_interp'] = [options['sensor_power_photovoltaics'], options['sensor_power_load_no_var_loads']]
    # Updating variables in optim_conf
    params['optim_conf'][0]['set_use_battery'] = options['set_use_battery']
    params['optim_conf'][2]['num_def_loads'] = options['number_of_deferrable_loads']
    params['optim_conf'][3]['P_deferrable_nom'] = [int(i) for i in options['nominal_power_of_deferrable_loads'].split(',')]
    params['optim_conf'][4]['def_total_hours'] = [int(i) for i in options['operating_hours_of_each_deferrable_load'].split(',')]
    params['optim_conf'][5]['treat_def_as_semi_cont'] = [True for i in range(len(params['optim_conf'][3]['P_deferrable_nom']))]
    params['optim_conf'][6]['set_def_constant'] = [False for i in range(len(params['optim_conf'][3]['P_deferrable_nom']))]
    start_hours_list = options['peak_hours_periods_start_hours'].split(',')
    end_hours_list = options['peak_hours_periods_end_hours'].split(',')
    num_peak_hours = len(start_hours_list)
    list_hp_periods_list = [{'period_hp_'+str(i+1):[{'start':start_hours_list[i]},{'end':end_hours_list[i]}]} for i in range(num_peak_hours)]
    params['optim_conf'][10]['list_hp_periods'] = list_hp_periods_list
    params['optim_conf'][11]['load_cost_hp'] = options['load_peak_hours_cost']
    params['optim_conf'][12]['load_cost_hc'] = options['load_offpeak_hours_cost']
    params['optim_conf'][14]['prod_sell_price'] = options['photovoltaic_production_sell_price']
    # Updating variables in plant_conf
    params['plant_conf'][0]['P_grid_max'] = options['maximum_power_from_grid']
    params['plant_conf'][1]['module_model'] = options['pv_module_model']
    params['plant_conf'][2]['inverter_model'] = options['pv_inverter_model']
    params['plant_conf'][3]['surface_tilt'] = options['surface_tilt']
    params['plant_conf'][4]['surface_azimuth'] = options['surface_azimuth']
    params['plant_conf'][5]['modules_per_string'] = options['modules_per_string']
    params['plant_conf'][6]['strings_per_inverter'] = options['strings_per_inverter']
    params['plant_conf'][7]['Pd_max'] = options['battery_discharge_power_max']
    params['plant_conf'][8]['Pc_max'] = options['battery_charge_power_max']
    params['plant_conf'][9]['eta_disch'] = options['battery_discharge_efficiency']
    params['plant_conf'][10]['eta_ch'] = options['battery_charge_efficiency']
    params['plant_conf'][11]['Enom'] = options['battery_nominal_energy_capacity']
    params['plant_conf'][12]['SOCmin'] = options['battery_minimum_state_of_charge']
    params['plant_conf'][13]['SOCmax'] = options['battery_maximum_state_of_charge']
    params['plant_conf'][14]['SOCtarget'] = options['battery_target_state_of_charge']
    # The params dict
    params['params_secrets'] = params_secrets
    params['passed_data'] = {'pv_power_forecast':None,'load_power_forecast':None,'load_cost_forecast':None,'prod_price_forecast':None}
    cache.set("params", params)

    # Launch server
    os.environ.setdefault('FLASK_ENV', 'development')
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host=web_ui_url, port=port)

if __name__ == "__main__":
    main()

