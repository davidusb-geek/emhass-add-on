<!-- markdown file presented on the documentation tab -->

# EMHASS Add-on Documentation

<div>
 <a style="text-decoration:none" href="https://emhass.readthedocs.io/en/latest/">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Documentation_button.svg" alt="EMHASS Documentation">
  </a>
   <a style="text-decoration:none" href="https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant/338126">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Community_button.svg" alt="Community">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass/issues">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Issues_button.svg" alt="Issues">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass-add-on">
     <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_Add_on_button.svg" alt="EMHASS Add-on">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass">
     <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_button.svg" alt="EMHASS">
  </a>
</div>

## This is the documentation for the Add-on of **EMHASS: Energy Management for Home Assistant**

EMHASS is a Python module proposing an **optimized energy management** approach using the Linear Programming (LP) optimization technique.

## What is this?

The goal here is to optimize the energy use of your home in order to maximize a pre-defined cost function, for example: autoconsumption.

The main study case is a household where we have solar panels, a grid connection, one or more controllable (deferrable) electrical loads and an energy storage system with batteries. Of course, it is not necessary to have all these equipements to use EMHASS (PV panels, batteries, etc), in the minimal use case you have a controllable/deferrable load and you just want to obtain the optimized daily schedule for your load.

The package flow can be graphically represented as follows:

![](https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/ems_schema.png)

So we have some data entering EMHASS (PV power, load, cost and selling prices forecasts), we have defined an objective function and some contraints (this is simply defined in a configuration file) and we have some controllable/deferrable loads. A call to an EMHASS optimization will yield the deferrable load schedule for future timestamps, the battery optimal power/SOC and the obtained value of the cost function. This information can published as sensors with attributes to Home Assistant and then we use the HA magic to automate our home energy consumption based on the optimization results.

The package is meant to be highly configurable with an object oriented modular approach and a main configuration file defined by the user.
EMHASS was designed to be integrated with Home Assistant, hence it's name.
Installation instructions and example Home Assistant automation configurations are given below.

You must follow these steps to make EMHASS work properly:

1. Define all the parameters in the configuration pane according to your installation. See the description for each parameter in the **configuration** section below.

2. You most notably will need to define the main data entering EMHASS. This will be the `sensor_power_photovoltaics` for the name of the your hass variable containing the PV produced power and the variable `sensor_power_load_no_var_loads` for the load power of your household excluding the power of the deferrable loads that you want to optimize.

3. Launch the actual optimization and check the results. This can be done manually using the buttons in the web ui or with a `curl` command like this: `curl -i -H 'Content-Type:application/json' -X POST -d '{}' http://localhost:5000/action/dayahead-optim`.

4. If you’re satisfied with the optimization results then you can set the optimization and data publish task commands in an automation. You can read more about this on the **usage** section below.

5. The final step is to link the deferrable loads variables to real switchs on your installation. An example code for this using automations and the shell command integration is presentedd below in the **usage** section.

## Configuration

These are the configuration parameters needed to correctly use this module.

- hass_url: Enter the URL of your Home Assistant instance. This defaults to empty. If using the supervisor you can leave this to the default empty value.
- long_lived_token: A Long-Lived Access Token that can be created from the Lovelace profile page. This defaults to empty. If using the supervisor you can leave this to the default empty value.
- costfun: Define the type of cost function, this is optional and the options are: `profit` (default), `cost`, `self-consumption`
- optimization_time_step: The time step to resample retrieved data from hass. This parameter is given in minutes. It should not be defined too low or you will run into memory problems when defining the Linear Programming optimization. Defaults to 30.
- historic_days_to_retrieve: We will retrieve data from now and up to historic_days_to_retrieve days. Defaults to 2. This will be used for the `perfect-optim` task.
- method_ts_round: Set the method for timestamp rounding, options are: first, last and nearest.
- set_total_pv_sell: Set this parameter to true to consider that all the PV power produced is injected to the grid. No direct self-consumption. The default is false, for as system with direct self-consumption.
- lp_solver: Set the name of the linear programming solver that will be used. Defaults to 'COIN_CMD'. The options are 'PULP_CBC_CMD', 'GLPK_CMD' and 'COIN_CMD'.
- lp_solver_path: Set the path to the LP solver. Defaults to '/usr/bin/cbc'.
- set_nocharge_from_grid: Set this to true if you want to forbidden to charge the battery from the grid. The battery will only be charged from excess PV.
- set_nodischarge_to_grid: Set this to true if you want to forbidden to discharge the battery power to the grid.
- set_battery_dynamic: Set a power dynamic limiting condition to the battery power. This is an additional constraint on the battery dynamic in power per unit of time.
- battery_dynamic_max: The maximum positive battery power dynamic. This is the power variation in percentage of battery maximum power.
- battery_dynamic_min: The minimum negative battery power dynamic. This is the power variation in percentage of battery maximum power.
- weight_battery_discharge: An additional weight applied in cost function to battery usage for discharge.
- weight_battery_charge: An additional weight applied in cost function to battery usage for charge.
- load_forecast_method: The load forecast method. This defaults to 'naive'. The available options are 'csv', 'list' or 'mlforecaster' to use the machine learning forecaster.
- sensor_power_photovoltaics: This is the name of the photovoltaic produced power sensor in Watts from Home Assistant. For example: 'sensor.power_photovoltaics'.
- sensor_power_load_no_var_loads: The name of the household power consumption sensor in Watts from Home Assistant. The deferrable loads that we will want to include in the optimization problem should be substracted from this sensor in HASS. For example: 'sensor.power_load_no_var_loads'
- number_of_deferrable_loads: Define the number of deferrable loads to consider. Defaults to 2.
- nominal_power_of_deferrable_loads: The nominal power for each deferrable load in Watts. This is a list of comma separated values with a number of elements consistent with the number of deferrable loads defined before. For example: 3000, 750
- operating_hours_of_each_deferrable_load: The total number of hours that each deferrable load should operate. A list of comma separated values. For example: 5, 8

We will define now the paramters associated with the energy cost.

- peak_hours_periods_start_hours: This is a list of start hours of peak hours periods. A list of hours in 24h HH:MM format.
- peak_hours_periods_end_hours: This is a list of end hours of peak hours periods. A list of hours in 24h HH:MM format.

In the default configuration example the first peak hour will start at 02:54 and end at 15:24, and so on. If you don't have a peak/off-peak hours contract, then just leave these defaults period values and set the following peak/off-peak hours cost at the same value.

- treat_deferrable_load_as_semi_cont: Define if we should treat each deferrable load as a semi-continuous variable. Semi-continuous variables are variables that can take either their nominal value or zero.
- load_peak_hours_cost: The cost of the electrical energy from the grid during peak hours in €/kWh. Defaults to 0.1907.
- load_offpeak_hours_cost: The cost of the electrical energy from the grid during non-peak hours in €/kWh. Defaults to 0.1419.
- photovoltaic_production_sell_price: The paid price for energy injected to the grid from excedent PV production in €/kWh. Defaults to 0.065.

The following parameters are associated with the technical specifications of the PV power plant and the batteries.

- maximum_power_from_grid: The maximum power that can be supplied by the utility grid in Watts (consumption). Defaults to 9000.
- maximum_power_to_grid: The maximum power that can be supplied to the utility grid in Watts (injection). Defaults to 9000.

We will define the technical parameters of the PV installation. For the modeling task we rely on the PVLib Python package. For more information see: [https://pvlib-python.readthedocs.io/en/stable/](https://pvlib-python.readthedocs.io/en/stable/)

This webapp can help you find your correct module/inverter key: [https://emhass-pvlib-database.streamlit.app/](https://emhass-pvlib-database.streamlit.app/)

If your specific model is not found in these lists then solution (1) is to pick another model as close as possible as yours in terms of the nominal power.

Solution (2) would be to use SolCast and pass that data directly to emhass as a list of values from a template. Take a look at this example here: [https://emhass.readthedocs.io/en/latest/forecasts.html#example-using-solcast-forecast-amber-prices](https://emhass.readthedocs.io/en/latest/forecasts.html#example-using-solcast-forecast-amber-prices)

- pv*module_model: The PV module model. For example: 'CSUN_Eurasia_Energy_Systems_Industry_and_Trade_CSUN295_60M'. This parameter can be a list of strings to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270). When finding the correct model for your installation remember to replace all the special characters in the model name by '*'.
- pv*inverter_model: The PV inverter model. For example: 'Fronius_International_GmbH**Fronius_Primo_5_0_1_208_240**240V*'. This parameter can be a list of strings to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270). When finding the correct model for your installation remember to replace all the special characters in the model name by '\_'.
- surface_tilt: The tilt angle of your solar panels. This is a value between 0 and 90. Defaults to 30. This parameter can be a list of integers to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
- surface_azimuth: The azimuth of your PV installation. This is a value between 0 and 360. Defaults to 205. This parameter can be a list of integers to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
- modules_per_string: The number of modules per string. Defaults to 16. This parameter can be a list of integers to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
- strings_per_inverter: The number of used strings per inverter. Defaults to 1. This parameter can be a list of integers to enable the simulation of mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
- inverter_is_hybrid: Set to True to consider that the installation inverter is hybrid for PV and batteries. (Default False).
- compute_curtailment: Set to True to compute a PV curtailment variable. (Default False).
- set_use_battery: Set to True if we should consider an energy storage device such as a Li-Ion battery. Defaults to False.

If the `set_use_battery` is set to `true`, then the following parameters need to be defined properly. If you don't have a battery then just leave the default values, they will not be used.

- battery_discharge_power_max: The maximum discharge power in Watts. Defaults to 1000.
- battery_charge_power_max: The maximum charge power in Watts. Defaults to 1000.
- battery_discharge_efficiency: The discharge efficiency. Defaults to 0.95.
- battery_charge_efficiency: The charge efficiency. Defaults to 0.95.
- battery_nominal_energy_capacity: The total capacity of the battery stack in Wh. Defaults to 5000.
- battery_minimum_state_of_charge: The minimun allowable battery state of charge. Defaults to 0.3.
- battery_maximum_state_of_charge: The maximum allowable battery state of charge. Defaults to 0.9.
- battery_target_state_of_charge: The desired battery state of charge at the end of each optimization cycle. Defaults to 0.6.

Don't forget to hit the `SAVE` button at the end of the page.

You are now ready to lauch the add-on using the `START` button.

## Usage

This add-on exposes a simple webserver on port 5000. You can access it by clicking on the `OPEN WEB UI` button or directly using your brower, ex: http://localhost:5000.

When you access the webserver you will be looking at the latests results stored in a csv file on the data folder inside the add-on. This will look something like this:

![](https://raw.githubusercontent.com/davidusb-geek/emhass-add-on/master/emhass/images/screenshot_emhass_webui.png)

Each time that you launch the optimization task this csv file is rewritten and the graph and table in the UI can be refreshed. I left an initial csv file in the data folder so that the first time an user access the webserver it can check what type of results EMHASS will obtain when launching the optimization task. This initial csv was obtained with the default configuration presented in the configuration pane. The graph is interactive, so what you can do is use the legend to turn off the visualization of all variables except the deferrable load powers. In that example we have two deferrable loads and what you’re seeing is the result of the optimization. This is giving you the optimal evolution and turn on/off times of those deferrable loads in order to maximize profit for example, depending on what objective function you choose and all the forecast data that have been entered to EMHASS.

The webserver can be used to manually launch an optimization task or to publish the optimization data to some Home Assistant variables. For this use the manual buttons in the webserver. It can also be used to visualize optimization results with a graphic and table overview.

With this web server you can perform RESTful POST commands on one ENDPOINT called `action` with four options:

- A POST call to `action/perfect-optim` to perform a perfect optimization task on the historical data.
- A POST call to `action/dayahead-optim` to perform a day-ahead optimization task of your home energy.
- A POST call to `action/naive-mpc-optim` to perform a naive Model Predictive Controller optimization task. If using this option you will need to define the correct `runtimeparams` (see further below).
- A POST call to `action/publish-data` to publish the optimization results data for the current timestamp.

A `curl` command can then be used to launch an optimization task like this: `curl -i -H 'Content-Type:application/json' -X POST -d '{}' http://localhost:5000/action/dayahead-optim`.

To integrate with home assistant we will need to define some shell commands in the `configuration.yaml` file and some basic automations in the `automations.yaml` file.

In `configuration.yaml`:

```yaml
shell_command:
  dayahead_optim: 'curl -i -H "Content-Type:application/json" -X POST -d ''{}'' http://localhost:5000/action/dayahead-optim'
  publish_data: 'curl -i -H "Content-Type:application/json" -X POST -d ''{}'' http://localhost:5000/action/publish-data'
```

In `automations.yaml`:

```yaml
- alias: EMHASS day-ahead optimization
  trigger:
    platform: time
    at: "05:30:00"
  action:
    - service: shell_command.dayahead_optim
- alias: EMHASS publish data
  trigger:
    - minutes: /5
      platform: time_pattern
  action:
    - service: shell_command.publish_data
```

The final action will be to link a sensor value in Home Assistant to control the switch of a desired controllable load. For example imagine that I want to control my water heater and that the `publish-data` action is publishing the optimized value of a deferrable load that I want to be linked to my water heater desired behavior. In this case we could use an automation like this one below to control the desired real switch:

```yaml
automation:
  - alias: Water Heater Optimized ON
    trigger:
      - minutes: /5
        platform: time_pattern
    condition:
      - condition: numeric_state
        entity_id: sensor.p_deferrable0
        above: 0.1
    action:
      - service: homeassistant.turn_on
        entity_id: switch.water_heater_switch
```

A second automation should be used to turn off the switch:

```yaml
automation:
  - alias: Water Heater Optimized OFF
    trigger:
      - minutes: /5
        platform: time_pattern
    condition:
      - condition: numeric_state
        entity_id: sensor.p_deferrable0
        below: 0.1
    action:
      - service: homeassistant.turn_off
        entity_id: switch.water_heater_switch
```

The `publish-data` command will push to Home Assistant the optimization results for each deferrable load defined in the configuration. For example if you have defined two deferrable loads, then the command will publish `sensor.p_deferrable0` and `sensor.p_deferrable1` to Home Assistant. When the `dayahead-optim` is launched, after the optimization, a csv file will be saved on disk. The `publish-data` command will load the latest csv file and look for the closest timestamp that match the current time using the `datetime.now()` method in Python. This means that if EMHASS is configured for 30min time step optimizations, the csv will be saved with timestamps 00:00, 00:30, 01:00, 01:30, ... and so on. If the current time is 00:05, then the closest timestamp of the optimization results that will be published is 00:00. If the current time is 00:25, then the closest timestamp of the optimization results that will be published is 00:30.
The `publish-data` command will also publish PV and load forecast data on sensors `p_pv_forecast` and `p_load_forecast`. If using a battery, then the battery optimized power and the SOC will be published on sensors `p_batt_forecast` and `soc_batt_forecast`. On these sensors the future values are passed as nested attributes.

## Passing your own data

In EMHASS we have basically 4 forecasts to deal with:

- PV power production forecast (internally based on the weather forecast and the characteristics of your PV plant). This is given in Watts.

- Load power forecast: how much power your house will demand on the next 24h. This is given in Watts.

- Load cost forecast: the price of the energy from the grid on the next 24h. This is given in EUR/kWh.

- PV production selling price forecast: at what price are you selling your excess PV production on the next 24h. This is given in EUR/kWh.

The sensor containing the load data should be specified in parameter `var_load` in the configuration file. As we want to optimize the household energies, when need to forecast the load power conumption. The default method for this is a naive approach using 1-day persistence. The load data variable should not contain the data from the deferrable loads themselves. For example, lets say that you set your deferrable load to be the washing machine. The variable that you should enter in EMHASS will be: `var_load: 'sensor.power_load_no_var_loads'` and `sensor_power_load_no_var_loads = sensor_power_load - sensor_power_washing_machine`. This is supposing that the overall load of your house is contained in variable: `sensor_power_load`. The sensor `sensor_power_load_no_var_loads` can be easily created with a new template sensor in Home Assistant.

If you are implementing a MPC controller, then you should also need to provide some data at the optimization runtime using the key `runtimeparams`.

The valid values to pass for both forecast data and MPC related data are explained below.

### Forecast data

It is possible to provide EMHASS with your own forecast data. For this just add the data as list of values to a data dictionnary during the call to `emhass` using the `runtimeparams` option.

For example if using the add-on or the standalone docker installation you can pass this data as list of values to the data dictionnary during the `curl` POST:

```bash
curl -i -H 'Content-Type:application/json' -X POST -d '{"pv_power_forecast":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 141.22, 246.18, 513.5, 753.27, 1049.89, 1797.93, 1697.3, 3078.93, 1164.33, 1046.68, 1559.1, 2091.26, 1556.76, 1166.73, 1516.63, 1391.13, 1720.13, 820.75, 804.41, 251.63, 79.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}' http://localhost:5000/action/dayahead-optim
```

The possible dictionnary keys to pass data are:

- `pv_power_forecast` for the PV power production forecast.

- `load_power_forecast` for the Load power forecast.

- `load_cost_forecast` for the Load cost forecast.

- `prod_price_forecast` for the PV production selling price forecast.

### Passing other data

It is possible to also pass other data during runtime in order to automate the energy management. For example, it could be useful to dynamically update the total number of hours for each deferrable load (`def_total_hours`) using for instance a correlation with the outdoor temperature (useful for water heater for example).

Here is the list of the other additional dictionnary keys that can be passed at runtime:

- `num_def_loads` for the number of deferrable loads to consider.

- `P_deferrable_nom` for the nominal power for each deferrable load in Watts.

- `def_total_hours` for the total number of hours that each deferrable load should operate.

- `treat_def_as_semi_cont` to define if we should treat each deferrable load as a semi-continuous variable.

- `set_def_constant` to define if we should set each deferrable load as a constant fixed value variable with just one startup for each optimization task.

- `solcast_api_key` for the SolCast API key if you want to use this service for PV power production forecast.

- `solcast_rooftop_id` for the ID of your rooftop for the SolCast service implementation.

- `solar_forecast_kwp` for the PV peak installed power in kW used for the solar.forecast API call.

## A naive Model Predictive Controller

A MPC controller was introduced in v0.3.0. This is an informal/naive representation of a MPC controller.

A MPC controller performs the following actions:

- Set the prediction horizon and receding horizon parameters.
- Perform an optimization on the prediction horizon.
- Apply the first element of the obtained optimized control variables.
- Repeat at a relatively high frequency, ex: 5 min.

This is the receding horizon principle.

When applying this controller, the following `runtimeparams` should be defined:

- `prediction_horizon` for the MPC prediction horizon. Fix this at at least 5 times the optimization time step.

- `soc_init` for the initial value of the battery SOC for the current iteration of the MPC.

- `soc_final` for the final value of the battery SOC for the current iteration of the MPC.

- `def_total_hours` for the list of deferrable loads functioning hours. These values can decrease as the day advances to take into account receding horizon daily energy objectives for each deferrable load.

A correct call for a MPC optimization should look like:

```bash
curl -i -H 'Content-Type:application/json' -X POST -d '{"pv_power_forecast":[0, 70, 141.22, 246.18, 513.5, 753.27, 1049.89, 1797.93, 1697.3, 3078.93], "prediction_horizon":10, "soc_init":0.5,"soc_final":0.6,"def_total_hours":[1,3]}' http://localhost:5000/action/naive-mpc-optim
```

## A machine learning forecaster

Starting in v0.4.0 a new machine learning forecaster class was introduced. Check the dedicated section in the documentation here: [https://emhass.readthedocs.io/en/latest/mlforecaster.html](https://emhass.readthedocs.io/en/latest/mlforecaster.html)

## Disclaimer

The quality of the optimization results is bound to the quality of forecasts.

It is up to the user to test and validate the optimization results. Before control any deferrable load on your home, you should check that the results are coherent with your expectations. The webapp allows this with a visual inspection and an overview table of the optimization results, including the expected cost of the objective function choosed by the user.

## Contact

If you have a request, or if you need any help using this add-on or EMHASS in general, you can leave a message in this HA community thread:
</br></br><a style="text-decoration:none" href="https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant/338126">
<img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Community_button.svg" alt="Community">
</a>
</br></br>
If you find any problems with the code, you can open new issues in the EMHASS or EMHASS-Add-on Github repositories:
</br></br>
<a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass-add-on/issues">
<img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_Add_on_button.svg" alt="EMHASS-Add-on Issues">
</a>
</br>
_For any add-on specific issues. E.g. configuration page, add-on installation or add-on updating._
</br></br>
<a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass/issues">
<img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_button.svg" alt="EMHASS Issues">
</a>
</br>
_For for any other EMHASS issues issues._
