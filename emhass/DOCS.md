# EMHASS Add-on Documentation

This is the documentation for the Add-on of **EMHASS: Energy Management for Home Assistant**

This add-on repository: [https://github.com/davidusb-geek/emhass-add-on](https://github.com/davidusb-geek/emhass-add-on)
The EMHASS module github repository: [https://github.com/davidusb-geek/emhass](https://github.com/davidusb-geek/emhass)
The complete documentation for this module can be found here: [https://emhass.readthedocs.io/en/latest/](https://emhass.readthedocs.io/en/latest/)

EMHASS is a Python module proposing an **optimized energy management** approach using the Linear Programming (LP) optimization technique.

Right out the box EMHASS can be used to optimize the use of loads that are deferrable. This means that these loads can be “moved” around the day with “ideally” no impact on our everyday life. Good examples of these are: dishwasher, washing machine, etc. At my place I also considered as deferrable the water heater and the pool pump.

You must follow these steps to make EMHASS work properly:

1) Define all the parameters in the configuration pane according to your installation. See the description for each parameter in the **configuration** section below.

2) You most notably will need to define the main data entering EMHASS. This will be the `sensor_power_photovoltaics` for the name of the your hass variable containing the PV produced power and the variable `sensor_power_load_no_var_loads` for the load power of your household excluding the power of the deferrable loads that you want to optimize.

3) Launch the actual optimization and check the results. This can be done manually using the buttons in the web ui or with a `curl` command like this: `curl -i -H "Content-Type: application/json" -X POST -d '{}' http://localhost:5000/action/dayahead-optim`.

4) If you’re satisfied with the optimization results then you can set the optimization and data publish task commands in an automation. You can read more about this on the **usage** section below.

5) The final step is to link the deferrable loads variables to real switchs on your installation. An example code for this using automations and the shell command integration is presentedd below in the **usage** section.

## Configuration

These are the configuration parameters needed to correctly use this module.

- web_ui_url: Provide the web ui url. Leave this at the default value to have the web ui at localhost. Otherwise provide your custom url.
- hass_url: Enter the URL of your Home Assistant instance. For example: https://myhass.duckdns.org/ or http://localhost/. This defaults to empty. If using the supervisor you can leave this to the default empty value.
- long_lived_token: A Long-Lived Access Token that can be created from the Lovelace profile page. This defaults to empty. If using the supervisor you can leave this to the default empty value.
- costfun: Define the type of cost function, this is optional and the options are: `profit` (default), `cost`, `self-consumption`
- optimization_time_step: The time step to resample retrieved data from hass. This parameter is given in minutes. It should not be defined too low or you will run into memory problems when defining the Linear Programming optimization. Defaults to 30. 
- historic_days_to_retrieve: We will retrieve data from now and up to days_to_retrieve days. Defaults to 2.
- sensor_power_photovoltaics: This is the name of the photovoltaic produced power sensor in Watts from Home Assistant. For example: 'sensor.power_photovoltaics'.
- sensor_power_load_no_var_loads: The name of the household power consumption sensor in Watts from Home Assistant. The deferrable loads that we will want to include in the optimization problem should be substracted from this sensor in HASS. For example: 'sensor.power_load_no_var_loads'
- number_of_deferrable_loads: Define the number of deferrable loads to consider. Defaults to 2.
- nominal_power_of_deferrable_loads: The nominal power for each deferrable load in Watts. This is a list of comma separated values with a number of elements consistent with the number of deferrable loads defined before. For example: 3000, 750
- operating_hours_of_each_deferrable_load: The total number of hours that each deferrable load should operate. A list of comma separated values. For example: 5, 8

We will define now the paramters associated with the energy cost.

- peak_hours_periods_start_hours: This is a list of start hours of peak hours periods. A list of comma separated hours in 24h HH:MM format. For example for two peak hour periods: 02:54, 17:24
- peak_hours_periods_end_hours: This is a list of end hours of peak hours periods. A list of comma separated hours in 24h HH:MM format. For example for two peak hour periods: 15:24, 20:24

In this previous example the first peak hour will start at 02:54 and end at 15:24, and so on. If you don't have a peak/off-peak hours contract, then just leave these defaults period values and set the following peak/off-peak hours cost at the same value.

- load_peak_hours_cost: The cost of the electrical energy from the grid during peak hours in €/kWh. Defaults to 0.1907.
- load_offpeak_hours_cost: The cost of the electrical energy from the grid during non-peak hours in €/kWh. Defaults to 0.1419.
- photovoltaic_production_sell_price: The paid price for energy injected to the grid from excedent PV production in €/kWh. Defaults to 0.065.

The following parameters are associated with the technical specifications of the PV power plant and the batteries.

- maximum_power_from_grid: The maximum power that can be supplied by the utility grid in Watts. Defaults to 9000.

We will define the technical parameters of the PV installation. For the modeling task we rely on the PVLib Python package. For more information see: [https://pvlib-python.readthedocs.io/en/stable/](https://pvlib-python.readthedocs.io/en/stable/)
The complete list of supported modules and inverter models can be found here: [https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.pvsystem.retrieve_sam.html](https://pvlib-python.readthedocs.io/en/stable/generated/pvlib.pvsystem.retrieve_sam.html)

- pv_module_model: The PV module model. For example: 'CSUN_Eurasia_Energy_Systems_Industry_and_Trade_CSUN295_60M'
- pv_inverter_model: The PV inverter model. For example: 'Fronius_International_GmbH__Fronius_Primo_5_0_1_208_240__240V_'
- surface_tilt: The tilt angle of your solar panels. Defaults to 30.
- surface_azimuth: The azimuth of your PV installation. Defaults to 205.
- modules_per_string: The number of modules per string. Defaults to 16.
- strings_per_inverter: The number of used strings per inverter. Defaults to 1.
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

![](./images/screenshot_emhass_webui.png)

Each time that you launch the optimization task this csv file is rewritten and the graph and table in the UI can be refreshed. I left an initial csv file in the data folder so that the first time an user access the webserver it can check what type of results EMHASS will obtain when launching the optimization task. This initial csv was obtained with the default configuration presented in the configuration pane. The graph is interactive, so what you can do is use the legend to turn off the visualization of all variables except the deferrable load powers. In that example we have two deferrable loads and what you’re seeing is the result of the optimization. This is giving you the optimal evolution and turn on/off times of those deferrable loads in order to maximize profit for example, depending on what objective function you choose and all the forecast data that have been entered to EMHASS.

The webserver can be used to manually launch an optimization task or to publish the optimization data to some Home Assistant variables. For this use the manual buttons in the webserver. It can also be used to visualize optimization results with a graphic and table overview.

Using this web server you can perform RESTful POST commands on one ENDPOINT called `action` with two main options:

- A POST call to `action/dayahead-optim` to perform a day-ahead optimization task of your home energy
- A POST call to `action/publish-data ` to publish the optimization results data

To integrate with home assistant we will need to define some shell commands in the `configuration.yaml` file and some basic automations in the `automations.yaml` file.

In `configuration.yaml`:

```
shell_command:
  dayahead_optim: curl -i -H "Content-Type: application/json" -X POST -d '{}' http://localhost:5000/action/dayahead-optim
  publish_data: curl -i -H "Content-Type: application/json" -X POST -d '{}' http://localhost:5000/action/publish-data 
```

In `automations.yaml`:

```
- alias: EMHASS day-ahead optimization
  trigger:
    platform: time
    at: '05:30:00'
  action:
  - service: shell_command.dayahead_optim
- alias: EMHASS publish data
  trigger:
  - minutes: /5
    platform: time_pattern
  action:
  - service: shell_command.publish_data
```

The final action will be to link a sensor value in Home Assistant to control the switch of a desired controllable load. For example imagine that I want to control my water heater and that the `publish-data` action is publishing the optimized value of a deferrable load that I have linked to my water heater desired behavior. In this case we could use an automation like this one below to control the desired real switch:

```
automation:
  trigger:
    - platform: numeric_state
      entity_id:
        - sensor.p_deferrable1
      above: 0.1
  action:
    - service: homeassistant.turn_on
      entity_id: switch.water_heater
```

A second automation should be used to turn off the switch:

```
automation:
  trigger:
    - platform: numeric_state
      entity_id:
        - sensor.p_deferrable1
      below: 0.1
  action:
    - service: homeassistant.turn_off
      entity_id: switch.water_heater
```
The `publish-data` command will push to Home Assistant the optimization results for each deferrable load defined in the configuration. For example if you have defined two deferrable loads, then the command will publish `sensor.p_deferrable1` and `sensor.p_deferrable2` to Home Assistant.

## Forecast data

In EMHASS we have basically 4 forecasts to deal with:

- PV power production forecast (internally based on the weather forecast and the characteristics of your PV plant). This is given in Watts.

- Load power forecast: how much power your house will demand on the next 24h. This is given in Watts.

- Load cost forecast: the price of the energy from the grid on the next 24h. This is given in EUR/kWh.

- PV production selling price forecast: at what price are you selling your excess PV production on the next 24h. This is given in EUR/kWh.

Maybe the hardest part is the load data: `sensor_power_load_no_var_loads`. As we want to optimize the energies, the load forecast default method is a naive approach using 1-day persistence, this mean that the load data variable should not contain the data from the deferrable loads themselves. For example, lets say that you set your deferrable load to be the washing machine. The variable that you should enter in EMHASS will be: `sensor_power_load_no_var_loads = sensor_power_load - sensor_power_washing_machine`. This is supposing that the overall load of your house is contained in variable: `sensor_power_load`. This can be easily done with a new template sensor in Home Assistant.

### Passing your own forecast data

It is possible to provide EMHASS with your own forecast data. For this just add the data as list of values to the data dictionnary during the `curl` POST. 

For example:
```
curl -i -H "Content-Type: application/json" -X POST -d '{"pv_power_forecast":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 141.22, 246.18, 513.5, 753.27, 1049.89, 1797.93, 1697.3, 3078.93, 1164.33, 1046.68, 1559.1, 2091.26, 1556.76, 1166.73, 1516.63, 1391.13, 1720.13, 820.75, 804.41, 251.63, 79.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]}' http://localhost:5000/action/dayahead-optim
```

The possible dictionnary keys to pass data are:

- `pv_power_forecast` for the PV power production forecast.

- `load_power_forecast` for the Load power forecast.

- `load_cost_forecast` for the Load cost forecast.

- `prod_price_forecast` for the PV production selling price forecast.


## Disclaimer

The quality of the optimization results is bound to the quality of forecasts. To improve the forecast you can provide your own forecast results as CSV files input. This is fully implemented in the EMHASS module but not yet in this add-on. It is a work in progress and this will be added in the future.

It is up to the user to test and validate the optimization results. Before control any deferrable load on your home, you should check that the results are coherent with your expectations. The webapp allows this with a visual inspection and an overview table of the optimization results, including the expected cost of the objective function choosed by the user.

## Contact

If you have any request or if you need any help using this add-on or EMHASS in general you can leave a message in this HA community thread: [https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant](https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant).

If you find any problems with the code you can of course open new issues on the Github repository of [this add-on](https://github.com/davidusb-geek/emhass-add-on) or on the repository of the [core EMHASS code](https://github.com/davidusb-geek/emhass).

## TODOs

- [ ] Implement the different methods for weather, load power, production and load costs forecasting.
- [ ] Currently this add-on is built locally on the user machine. It is expected to migrate to pre-built containers in the future.
