# EMHASS Add-on Documentation

This is the documentation for the Add-on of EMHASS: Energy Management for Home Assistant.

This add-on repository: https://github.com/davidusb-geek/emhass-add-on
The EMHASS module github repository: https://github.com/davidusb-geek/emhass
The complete documentation for this module can be found here: https://emhass.readthedocs.io/en/latest/

## Configuration

These are the configuration parameters needed to correctly use this module.

- home_assistant_url: Enter the URL to your Home Assistant instance. For example: https://myhass.duckdns.org/ or http://localhost:8123/
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

This add-on exposes a simple webserver on port 5000. You can access it hiting on the `OPEN WEB UI` button or directly using your brower, ex: http://localhost:5000. The webserver can be used to manually launch an optimization task or to publish the optimization data to some Home Assistant variables. For this use the manual buttons in the webserver. It can also be used to visualize optimization results with a graphic and table overview.

Using this web server you can perform RESTful POST commands on one ENDPOINT called `action` with two main options:

- A POST call to `action/dayahead-optim` to perform a day-ahead optimization task of your home energy
- A POST call to `action/publish-data ` to publish the optimization results data

To integrate with home assistant we will need to define some shell commands in the `configuration.yaml` file and some basic automations in the `automations.yaml` file.

In `configuration.yaml`:

```
shell_command:
  dayahead_optim: curl -X POST http://localhost:5000/action/dayahead-optim
  publish_data: curl -X POST http://localhost:5000/action/publish-data 
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

## Disclaimer

The quality of the optimization results is bound to the quality of forecasts. To improve the forecast you can provide your own forecast results as CSV files input. This is fully implemented in the EMHASS module but not yet in this add-on. It is a work in progress and this will be added in the future.

It is up to the user to test and validate the optimization results. Before control any deferrable load on your home, you should check that the results are coherent with your expectations. The webapp allows this with a visual inspection and an overview table of the optimization results, including the expected cost of the objective function choosed by the user.

## TODOs

- [ ] Implement the different methods for weather, load power, production and load costs forecasting.
- [ ] Currently this add-on is built locally on the user machine. It is expected to migrate to pre-built containers in the future.
