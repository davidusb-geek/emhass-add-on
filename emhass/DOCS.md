# EMHASS Add-on Documentation

This is the documentation for the Add-on of EMHASS: Energy Management for Home Assistant.

This add-on repository: https://github.com/davidusb-geek/emhass-add-on
The EMHASS module github repository: https://github.com/davidusb-geek/emhass
The complete documentation for this module can be found here: https://emhass.readthedocs.io/en/latest/

## Installation

To install add the EMHASS Add-on repository in the Home Assistant stroe. Follow these steps: https://www.home-assistant.io/common-tasks/os/#installing-third-party-add-ons

This will be: Configuration > Add-ons & Backups open the add-on store > Add the URL of the repository and then press "Add".

Look for the EMHASS Add-on tab and when inside the Add-on click on `install`.

This add-on is based on the official python:3.8-slim-buster docker image from docker-hub. In the future I may migrate this to the official Home Assistant docker images, however the slim version offers a good trade-off between final image size and possibility to install complete PyPi Python packages. Despite the reduced size of the slim image be patient, the installation may take some time depending on your hardware.

When the installation has finished go to the `Configuration` tab to set the add-on parameters.


## Configuration

These are the configuration parameters needed to correctly use this module.

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

In this previous example the first peak hour will start at 02:54 and end at 15:24, and so on.

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


## Usage

Define automations...

## Disclaimer

Quality of the optimization results bound to the quality of forecasts...

## TODOs

Implement the different methods for weather, load power, production and load costs forecasting...