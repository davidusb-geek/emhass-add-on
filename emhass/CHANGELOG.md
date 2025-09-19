# Changelog

## 0.13.5 - 2025-09-19
### Improvement
- Use SVG render mode for Plotly figures (@Crosenhain)
- Constrain PV curtailment of hybrid inverter (@rmounce)
### Fix
- Fix operating_timesteps_of_each_deferrable_load validation formula (@scruysberghs)

## 0.13.4 - 2025-08-25
### Improvement
- Added support for minimum power value for each deferrable load
- Add configuration for hybrid inverter input power limit and efficiency (@rmounce)
- Add runtime parameter to prevent PV forecast feedback loop during curtailment (@scruysberghs)
- Update Docker documentation for volume mounting of config.json (@cabberley)
- Apply ruff formatting for improved code consistency (@polyfloyd)
- Set executable permissions for `__main__` entrypoints and remove unused shebangs (@polyfloyd)
- Correct minor typos in README documentation (@Ultimation)
### Fix
- Fixed naive load power forecast shifted timestamp issue #516
- Fix Docker build for aarch64 architecture (@polyfloyd)

## 0.13.3 - 2025-05-02
### Improvement
- Enhance optimization solver capabilities by adding HiGHS solver, improving thread configuration, and updating solver support across the project (@Crosenhain)
- Update spelling and extended some error messages to include more troubleshooting information (@kcoffau)
### Fix
- Fixed incorrect indentation in a for loop, leaving relevant constraints out of the optimisation (@purcell_lab)

## 0.13.2 - 2025-04-29
### Improvement
- Improved README and development documentation (@Crosenhain and @gieljnssns)
- Improved forecasting and optimization classes logging (@purcell_lab)
### Fix
- Fixed ML Regressor for correct time zone treatment (@gieljnssns)
- Fixed long standing problem to allow thermal and standard loads to be scheduled (@purcell_lab)
- Fixing Missing files in python package issue (@pail23)
- Fixed improper handling of home assistant API errors (@Gruek)
- Remove an extraneous comma in the pd.to_datetime() method call in retrieve_hass.py (@GeoDerp)
- Fixed the SettingWithCopyWarning Pandas problem and PV sensor handling when set_use_adjusted_pv is false (@paulhomes)

## 0.13.1 - 2025-04-21
### Improvement
- Add timeout and thread configuration for different LP solvers (CBC, GLPK, COIN). Thanks to @GeoDerp
- Clean up actions and add sourcery scan action. Thanks to @GeoDerp
- Cache Open-Meteo JSON reponse locally to reduce the number of API calls and add resilience. Thanks to @paulhomes
### Fix
- Update default weight battery value in config_defaults.json. Thanks to @purcell-lab
- Fix forecast output assignment and avoid SettingWithCopyWarning. Thanks to @radim2tej
- Fix for get_mix_forecast ValueError: cannot convert float NaN to integer. Thanks to @paulhomes
- Fix for hard-coded actual/forecast PV sensor names. Thanks to @paulhomes
- Update pyproject.toml to solve issue #495: Missing files in python package after 0.12.5. Thanks to @GeoDerp

## 0.13.0 - 2025-04-02
### Improvement
- Added a new feature to automatically adjust PV forecast using historical actual/forecast data
- Added Support for multiple days forecasting with CSV data. Thanks to @nielskool for this contribution!
- Refactored a new method `retrieve_home_assistant_data` in `command_line`
- Unified default training data for ML algorithms using `data/long_train_data.pkl`
- Added a presentation stack using `marp`
### Fix
- Fixed Value has dtype incompatible with int64 error, issue #465
- Fixed Runtime "delta_forecast_daily" not recognized, issue #479
- Attempt to fix Missing files in python package after 0.12.5, issue #495
- Fixed workflow for macos tests

## 0.12.8 - 2025-02-27
### Improvement
- Added a new method for weather forecast: open-meteo. This offers a very nice API to obtain weather forecasts. We are dropping the old scrapper method, if you were using the scapper method you just need to change the Weather forecast method to open-meteo
- Added support to `device_class` definition when posting sensors to HA. Thanks to @paulhomes for this contribution
- Improved github workflow Python testing
- Updated documentation
### Fix
- Fixed TZ shift issue when using the typical load power forecaster

## 0.12.7 - 2025-02-16
### Improvement
- A first batch of improvements (code reliability) proposed by SonarQube
### Fix
- Added missing files to Dockerfile
- Changes to the Dockerfile to make `/app/data` folder persistent. Thanks to @scruysberghs
- Fixing errors with missing sensor `power_load_no_var_loads`. Thanks to @scruysberghs
- Improved documentation and fixed automated testing for code quality. Thanks to @GeoDerp

## 0.12.6 - 2025-02-09
### Improvement
- Improved warning message in case of wrong URL setting
- Improved testing on typical load forecast method with different time steps
### Fix
- Solved missing file problem: data_load_cost_forecast.csv
- Fixed warning issue on `findall` method

## 0.12.5 - 2025-02-02
### Improvement
- Implemented new package manager uv resulting in faster builds. Thanks to @GeoDerp
- Implemented SonarQube automatic code review. Thanks to @GeoDerp
- Better management of SOC min/max to solve issue: MPC optim status infeasible when SOC lower than min SOC
### Fix
- Reverted back skforecast to latest version
- Fixed issue with list index out of range. Thanks to @meks007 for identifying and reporting this

## 0.12.4 - 2025-01-27
### Patch fix
- Fixed bugs on gunicorn logger and missing CBC modules

## 0.12.3 - 2025-01-26
### Improvement
- PVLib DBs append custom EMHASS modules and inverters. Thanks to @GeoDerp
- Added a `def_total_timestep` parameter (runtime only for now) that can be used instead of `def_total_hours` for passing timestep number instead of hour number. Thanks to @GeoDerp
- Updated list of currencies in utils.py. Thanks to @BDVGitHub
- Multiple roof_id support. Thanks to @radim2tej
### Fix
- Fix inconsistencies with Modules and Inverters from PVLib (thanks to help from @RafAustralia)
- Fix issue with NAN sensors causing crash errors if incorrect (error handling) @purcell-lab
- Fix Database path on optimization file (Thanks to @paulhomes for finding this issue)
- Fixed weight_battery_charge sign problem. Thanks to @radim2tej
- Fixed bug with out of index in list when retrieving config params from HA

## 0.12.2 - 2025-01-01
### Patch fix
- Fixed Problem with calling weather-forecast-cache
### Improvement
- Updated readthedocs.yml, got rid of duplicated requirements.txt

## 0.12.1 - 2024-12-30
### Patch fix
- Fixed error with retrieve config from HA

## 0.12.0 - 2024-12-29
### BREAKING CHANGE
- The solar PV system is now optional. If you have a PV system then use the switch on the webui or set the `set_use_pv` parameter to `True`.
### Improvement
- A new load power forecast method based on statistic and typical household load power consumption. This and the optional PV, will make it easier for new users to on-board EMHASS because this new default behavior does not require any data retrieval from Home Assistant or any other external source.
- Updated documentation.

## 0.11.4 - 2024-12-24
### Fix
- Fix bug when treating runtime params, fix optimization_time_step timedelta 

## 0.11.3 - 2024-12-23
### Improvement
- Runtime parameters now support all config parameters
- Adopted the Ruff code fomatting
- Added a Github Actions for Google OSV security code scan 
- Updated the param_definitions.json 
- Bump skforecast from 0.13.0 to 0.14.0. This needed upgrading a bunch of deprecated options. Notably skforcast now uses the time series cross-validation object (cv) from sklearn 
### Fix
- Updated the default battery optimization weights
- Fix publish_data defaulting to opt_res_latest, tweak warning logs
- Added MLForecaster options to load_forecast_method for param_definitions.json

## 0.11.2 - 2024-10-31
### Improvement
- Added support to retrieve HA configuration. This will be used in the future to automatically retrieve some parameters as the currency
### Fix
- utils fix runtime parameter merge bugs 
- configuration_script.js fix placeholder value bug 

## 0.11.1 - 2024-10-29
### Fix
- Fix parameter saving and duplicate battery bugs 
- utils.py add more specific logging information for config 
- Fix issue where thermal runtime parameters were not being propagated into optim_conf 

## 0.11.0 - 2024-10-25

This version marks huge improvement works by @GeoDerp aiming to simplfy the intial and normal setup of EMHASS. The workflow for setting the EMHASS configuration regardless of the installation method has now been centralized on the single `config.json` file. The webserver has now a configuration tab that can be used to to modify and save the `config.json` file.

The complete discussion of the changes on this thread:
[https://github.com/davidusb-geek/emhass/pull/334](https://github.com/davidusb-geek/emhass/pull/334)

### Automatic version bot improvements
- Bump h5py from 3.11.0 to 3.12.1
- Bump markupsafe from 2.1.5 to 3.0.2

### Fix
- Revert to myst-parser==3.0.1 to solve documentation compilation failures

## 0.10.6 - 2024-07-14
### Fix
- Fixed bug on predicted room temeprature publish, wrong key on DataFrame

## 0.10.5 - 2024-07-12
### Improvement
- Added support for pubishing thermal load data, namely the predicted room temperature

## 0.10.4 - 2024-07-10
### Improvement
- Added a new thermal modeling, see the new section in the documentation for help to implement this of model for thermal deferrable loads
- Improved documentation

## 0.10.3 - 2024-07-06
### Improvement
- Added improved support for `def_start_penalty` option
- Improved documentation

## 0.10.2 - 2024-07-06
### Improvement
- Weather forecast caching and Solcast method fix by @GeoDerp
- Added a new configuration parameter to control wether we compute PV curtailment or not
- Added hybrid inverter to data publish
- It is now possible to pass these battery parameters at runtime: `SOCmin`, `SOCmax`, `Pd_max` and `Pc_max`
### Fix
- Fixed problem with negative PV forecast values in optimization.py, by @GeoDerp

## 0.10.1 - 2024-06-03
### Fix
- Fixed PV curtailment maximum possible value constraint
- Added PV curtailement to variable to publish to HA

## 0.10.0 - 2024-06-02
### BREAKING CHANGE
- In this new version we have added support for PV curtailment computation. While doing this the nominal PV peak power is needed. The easiest way find this information is by directly using the `inverter_model` defined in the configuration. As this is needed in the optimization to correctly compute PV curtailment, this parameter need to be properly defined for your installation. Before this chage this parameter was only needed if using the PV forecast method `scrapper`, but now it is not optional as it is directly used in the optimization. 
Use the dedicated webapp to find the correct model for your inverter, if you cannot find your exact brand/model then just pick an inverter with the same nominal power as yours: [https://emhass-pvlib-database.streamlit.app/](https://emhass-pvlib-database.streamlit.app/)
### Improvement
- Added support for hybrid inverters and PV curtailment computation
- Implemented a new `continual_publish` service that avoid the need of setting a special automation for data publish. Thanks to @GeoDerp
- Implement a deferrable load start penalty functionality. Thanks to @werdnum
  - This feature also implement a `def_current_state` that can be passed at runtime to let the optimization consider that a deferrable load is currently scheduled or under operation when launching the optimization task
### Fix
- Fixed forecast methods to treat delta_forecast higher than 1 day
- Fixed solar.forecast wrong interpolation of nan values

## 0.9.1 - 2024-05-13
### Fix
- Fix patch for issue with paths to modules and inverters database
- Fixed code formatting, or at least trying to keep a unique format

## 0.9.0 - 2024-05-12
### Improvement
- On this new version we now have a new method to train a regression model using Scikit-Learn methods. This is the contribution of @gieljnssns. Check the dedicated section the documentation to this new feature: [https://emhass.readthedocs.io/en/latest/mlregressor.html](https://emhass.readthedocs.io/en/latest/mlregressor.html)
- Again another bunch of nice improvements by @GeoDerp:
  - Added Dictionary var containing EMHASS paths
  - MLForcaster error suppression
  - Add `freq` as runtime parameter
  - Improved documentation added README buttons
- Bumping dependencies:
  - Bump h5py from 3.10.0 to 3.11.0
  - Bump myst-parser from 2.0.0 to 3.0.1
  - Bump skforecast from 0.11.0 to 0.12.0

## 0.8.6 - 2024-04-07
### Fix
- Fixed bug from forecast out method related to issue 240
- Fix patch for some issues with package file paths

## 0.8.5 - 2024-04-01
### Improvement
- Simplified fetch urls to relatives
- Improved code for passed forecast data error handling in utils.py
- Added new tests for forecast longer than 24h by changing parameter `delta_forecast`
- Added new files for updated PV modules and inverters database for use with PVLib
- Added a new webapp to help configuring modules and inverters: [https://emhass-pvlib-database.streamlit.app/](https://emhass-pvlib-database.streamlit.app/)
- Added a new `P_to_grid_max` variable, different from the current `P_from_grid_max` option
### Fix
- style.css auto format and adjusted table styling
- Changed pandas datetime rounding to nonexistent='shift_forward' to help survive DST change
- Dropped support for Python 3.9

## 0.8.4 - 2024-03-13
### Improvement
- Improved documentation
- Improved logging errors on missing day info
### Fix
- Missing round treatment for DST survival in utils.py 
- Webui large icons fix

## 0.8.3 - 2024-03-11
### Fix
- Fixed web_server options_json bug in standalone fix 

## 0.8.2 - 2024-03-10
### Improvement
- Proposed a new solution to survive DST using special option of Pandas `round` method
- Added option to `web_server` to init `data_path` as an options param
- Styling docs and html files on webui
- Advanced and basic pages improvements on webui
### Fix
- Fixed support for ARM achitectures

## 0.8.1 - 2024-02-28
### Improvement
- Improved documentation
### Fix
- Persistent data storage fix
- Docker Standalone Publish Workspace Fix

## 0.8.0 - 2024-02-25
### Improvement
- Thanks to the great work from @GeoDerp we now have a unified/centralized Dockerfile that allows for testing different installation configuration methods in one place. This greatly helps testing, notably emulating the add-on environment. This will improve overall testing for both teh core code and the add-on. Again many thanks!
- There were also a lot of nice improveements from @GeoDerp to the webui, namely: styling, dynamic table, optimization feedback after button press, logging, a new clear button, etc.
- From now on we will unify the semantic versioning for both the main core code and the add-on.

## 0.6.6 - 2024-02-11
### Improvement
- Bumped the webui. Some great new features and styling. Now it is possible to pass data directly as lsit of values when using the buttons in the webui. Thanks to @GeoDerp
- Added two additional testing environment options. Thanks to @GeoDerp
### Fix
- Bump markupsafe from 2.1.4 to 2.1.5

## 0.6.5 - 2024-02-06
### Fix
- Fixed number of startups constraint for deferrable load at the begining of the optimization period
- Fixed list of bools from options.json
- Fixed some testing and debugging scripts

## 0.6.4 - 2024-02-04
### Fix
- Following new patch on "perform_backtest": "false" has no effect

## 0.6.3 - 2024-02-04
### Fix
- Fixed broken build params method. Reverting back to alternate PR from @GeoDerp

## 0.6.2 - 2024-02-04
Following update of EMHASS code v0.7.3
### Fix
- Fixed bug when booleans, solving "perform_backtest": "false" has no effect
- Refactored util.py method to handle optional parameters
- Updated web server, solving runtime issues
- Solved issue passing solcast and solar.forecast runtime params 
- Updated documentation requirements

## 0.6.1 - 2024-01-30
Patched new version with bug fixes on ptahs and missing list types

## 0.6.0 - 2024-01-28
Following update of EMHASS code v0.7.1
### Improvement
- Added a new feature to provide operating time windows for deferrable loads. Thanks to @michaelpiron
- Added lots of new options to be configured by the user. Thanks to @GeoDerp
- Updated stylesheet with mobile & dark theme by @GeoDerp
- Improved launch.json to fully test EMHASS on different configurations. Thanks to @GeoDerp
- Added new script to debug and develop new time series clustering feature
- Improved documentation. Thanks to @g1za
### Fix
- Updated github workflow actions/checkout to v4 and actions/setup-python to v5
- Changed default values for weight_battery_discharge and weight_battery_charge to zero
- Renamed classes to conform to PEP8
- Bump markupsafe from 2.1.3 to 2.1.4 

## 0.5.4 - 2023-12-19
Following update of EMHASS code v0.6.2
### Improvement
- Added option to pass additional weight for battery usage
- Improved coverage
### Fix
- Updated optimization constraints to solve conflict for `set_def_constant` and `treat_def_as_semi_cont` cases

## 0.5.3 - 2023-12-19
### Fix
- Stepping down to Python 3.9 for ARMHF architectures.

## 0.5.2 - 2023-12-18
### Fix
- Fixes following update of EMHASS code v0.6.1
- Added --break-system-packages option to buil docker image to solve for PEP 668

## 0.5.1 - 2023-12-17
### Fix
- Patching v0.5.0. Updated to Python 3.11 using bookworm debian version

## 0.5.0 - 2023-12-17
Improvements and fixes following update of EMHASS code v0.6.0
### Improvement
- Now Python 3.11 is fully supported, thanks to @pail23
- We now publish the optimization status on sensor.optim_status
- Bumped setuptools, skforecast, numpy, scipy, pandas
- A good bunch of documentation improvements thanks to @g1za
- Improved code coverage (a little bit ;-)
### Fix
- Some fixes managing time zones, thanks to @pail23
- Bug fix on grid cost function equation, thanks to @michaelpiron
- Applying a first set of fixes proposed by @smurfix:
  - Don't ignore HTTP errors
  - Handle missing variable correctly
  - Slight error message improvement
  - Just use the default solver
  - Get locations from environment in non-app mode
  - Tolerate running directly from source

## 0.4.2 - 2023-10-19
### Fix
- Updated requirements.txt with skforecast 0.10.1

## 0.4.1 - 2023-10-19
Improvements and fixes following update of EMHASS code v0.5.1
### Improvement
- Improved documentation, thanks to @g1za
- Bumped skforecast to 0.10.1
- Added a new initial script for exploration of time series clustering. This will one day replace the need to configure the house load sensor with substracted deferrable load consumption
### Fix
- Updated automated tesing, dropped support for Python 3.8
- Patched config for bad hour formatting preventing add-on to start, thanks to @jatty

## 0.4.0 - 2023-09-03
Improvements and fixes following update of EMHASS code v0.5.0
### Improvement
- Finally added support for ingress thanks to the work from @siku2
- Added a devcontainer and pave the way for ingress access
### Fix
- Added some code to fix some numerical syntax issues in tables

## 0.3.16 - 2023-08-11
Improvements and fixes following update of EMHASS code v0.4.15
### Improvement
- Bumped pvlib to 0.10.1
- Updated documentation for forecasts methods.
### Fix
- Fixed error message on utils.py

## 0.3.15 - 2023-07-17
Improvements and fixes following update of EMHASS code v0.4.14
### Improvement
- Bumped skforecast to latest 0.9.1.
- The standalone dockerfile was updated by @majorforg to include the CBC solver.
### Fix
- Fix rounding for price & cost forecasts by @purcell-lab

## 0.3.14 - 2023-06-29
Improvements and fixes following update of EMHASS code v0.4.13
### Improvement
- Added support for data reconstruction when missing values on last window for ML forecaster prediction.
- Added treatment of SOCtarget passed at runtime for day-ahead optimization.
- Added publish_prefix key to pass a common prefix to all published data.
### Fix
- Patched sensor rounding problem.
- Bump myst-parser from 1.0.0 to 2.0.0
- Fixed missing attributes is the sensors when using the custom IDs.

## 0.3.13 - 2023-06-03
Improvements and fixes following update of EMHASS code v0.4.12
### Improvement
- Added forecasts for unit_prod_price and unit_load_cost.
- Improved documentation.
### Fix
- Bump skforecast from 0.8.0 to 0.8.1

## 0.3.12 - 2023-05-30
### Fix
- Updated the EMHASS config.yaml template with missing entries.

## 0.3.11 - 2023-05-29
### Fix
- Fixed error in type entry on add-on config.yaml.

## 0.3.10 - 2023-05-27
Improvements and fixes following update of EMHASS code v0.4.11
### Improvement
- Adding new constraints to limit the dynamics (kW/sec) of deferrable loads and battery power. The LP formulation works correctly and a work should be done on integrating the user input parameters to control this functionality.
- Added new constraint to avoid battery discharging to the grid.
- Added possibility to set the logging level.
### Fix
- Bumped version of skforecast from 0.6.0 to 0.8.0. Doing this mainly implies changing how the exogenous data is passed to fit and predict methods.
- Fixed wrong path for csv files when using load cost and prod price forecasts.

## 0.3.9 - 2023-05-21
### Fix
- Following update of EMHASS code v0.4.10
- Fixed wrong name of new cost sensor.
- Fixed units of measurements of costs to €/kWh.
- Added color sequence to plot figures, now avery line should be plotted with a different color.

## 0.3.8 - 2023-05-20
### Fix
- Following update of EMHASS code v0.4.9
- Updated default value for total number of days for ML model training.
- Added publish of unit_load_cost and unit_prod_price sensors.
- Improved docs intro.
- Bump myst-parser from 0.18.1 to 1.0.0

## 0.3.7 - 2023-03-17
### Fix
- Fixed to correct index length for ML forecaster prediction series.

## 0.3.6 - 2023-03-16
### Fix
- Fixed wrong path for saved ML forecaster model.
- Fixed wrong column name for var_load when using predict with ML forecaster.

## 0.3.5 - 2023-03-10
### Fix
- Fixed default behavior for passed data.
- Added a new graph for tune results.

## 0.3.4 - 2023-03-10
### Fix
- Fixed missing emhass module.

## 0.3.3 - 2023-03-09
### Fix
- Added missing possibility to set the method for load forecast to 'mlforecaster'.
- Fixed logging formatting.

## 0.3.2 - 2023-03-09
### Fix
- Fixed logging.
- Fixed missing module on docker standalone mode.

## 0.3.1 - 2023-03-07
### Fix
- Fixed handling of default passed params.

## 0.3.0 - 2023-03-06
The new machine learning forecast module is here! Check the updated documentation with the dedicated section here: [https://emhass.readthedocs.io/en/latest/mlforecaster.html](https://emhass.readthedocs.io/en/latest/mlforecaster.html)

### Improvement
- A brand new load forecast module and more... The new forecast module can actually be used to foreast any Home Assistant variable. The API provides fit, predict and tune methods. By the default it provides a more efficient way to forecast the power load consumption. It is based on the skforecast module that uses scikit-learn regression models considering auto-regression lags as features. The hyperparameter optimization is proposed using bayesian optimization from the optuna module.
- A new documentation section covering the new forecast module.
- Improved the documentation and the in-code docstrings.
- Added the possibility to save the optimized model after a tuning routine.
- Added the possibility to publish predict results to a Home Assistant sensor.
- Added the possibility to provide custom entity_id, unit_of_measurement and friendly_name for each published data.

### Fix
- Fixed Solar.Forecast issues with lists of parameters.
- Fixed latex equations rendering on documentation, dropped Mathjax.
- Refactored images in documentation, now using only SVG for plotly figures.
- Bumped requirements to latest non-conflicting versions.

## 0.2.29 - 2023-01-31
### Fix
- Fixed access to injection_dict for the first time that emhass is used.
- Fixed message handling from request module.

## 0.2.28 - 2023-01-30
### Fix
- Fixed more bugs with paths, now using the official pathlib everywhere.

## 0.2.27 - 2023-01-30
### Fix
- Fixed bugs on handling data folder name.
- Add-on now suvives restarts properly.
- Improved warning messages when passing list of values with items detected as non digits.

## 0.2.26 - 2023-01-29
### Improvement
- Implemented data storage to survive add-on restarts.

## 0.2.25 - 2023-01-27
### Fix
- Fixed dependencies, uniform working versions of Numpy, Pandas and Tables.

## 0.2.24 - 2023-01-26
### Improvement
- Following new fixes and improvements on emhass v0.3.23

## 0.2.23 - 2022-11-05
### Improvement
- Following new fixes on emhass v0.3.21
- Improved docstrings
- Improved unittest for mock get requests
- Added github worflows for coverage and automatic package compiling
### Fix
- Fixing interpolation for Forecast.Solar data

## 0.2.22 - 2022-10-05
### Improvement
- Following new fixes on emhass v0.3.20
- Added more detailed examples to the forecast module documentation.
- Improved handling of datatime indexes in DataFrames on forecast module.
- Added warning messages if passed list values contains non numeric items.
- Added missing unittests for forecast module with request.get dependencies using MagicMock.
- Added the Solar.Forecast method.

## 0.2.21 - 2022-09-14
### Fix
- Updated default values for a working LP solver.
- Removed option to provide a custom web ui url.
- Following new fixes on emhass v0.3.19

## 0.2.20 - 2022-08-27
### Improvement
- Improving documentation, added more information on forecast page.
- Added support for SolCast PV production forecasts. 
- Added possibility to pass some optimization parameters at runtime.
- Added some unittest for passing data as list testing.
### Fix
- Fixed small bug on webserver using pandas sum function for non numeric data. This was throwing the following message: Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated.

## 0.2.19 - 2022-06-12
### Fix
- Following new fixes on emhass v0.3.17
- Fixed wrong variables names for mixed forecasts.
- Fixed handling of load sensor name in command line setup function.

## 0.2.18 - 2022-06-10
### Improvement
- Following new improvements on emhass v0.3.16
- Improving documentation, added "what is this" section and added some infographics.
- Added new forecasts methods chapter in documentation.
- Added publish of sensors for p_grid_forecast & total value of cost function.
- Implemented now/current value forecast correction when using MPC.

## 0.2.17 - 2022-06-06
### Fix
- Following new fixes on emhass v0.3.15

## 0.2.16 - 2022-06-05
### Fix
- Following new improvements and fixes on emhass v0.3.14

## 0.2.15 - 2022-05-30
### Improvement
- Following new improvements and fixes on emhass v0.3.12

## 0.2.14 - 2022-05-23
### Improvement
- Following new improvements on emhass v0.3.11

## 0.2.13 - 2022-05-19
### Fix
- Added correct config file.

## 0.2.12 - 2022-05-19
### Fix
- Following fixes on emhass v0.3.9

## 0.2.11 - 2022-05-17
### Fix
- Following fixes on emhass v0.3.8
- Fixing more problems when loading passed data as lists.

## 0.2.10 - 2022-05-16
### Fix
- Following fixes on emhass v0.3.6
- Properly unittested the MPC implementation.

## 0.2.9 - 2022-05-16
### Fix
- Following fixes on emhass v0.3.5

## 0.2.8 - 2022-05-16
### Fix
- Following fixes on emhass v0.3.4

## 0.2.7 - 2022-05-16
### Fix
- Fix small error in run args, following PR.

## 0.2.6 - 2022-05-15
### Fix
- Following emhass v0.3.3. Template package loading should be solved.

## 0.2.5 - 2022-05-14
### Fix
- Added 777 chmod permission to run file.

## 0.2.4 - 2022-05-14
### Fix
- Trying to fix s6 overlay issues.

## 0.2.3 - 2022-05-13
### Fix
- Trying to fix current problem using init=false in config.

## 0.2.2 - 2022-05-13
### Fix
- Following fixes on emhass v0.3.2

## 0.2.1 - 2022-05-13
### Fix
- Following fixes on emhass v0.3.1

## 0.2.0 - 2022-05-13
### Improvement
- New version of this add-on following revamping of emhass core module and release v0.3.0
- Moved the webserver to the core emhass module for easier development.
- Added Model Predictive Control optimization.

## 0.1.42 - 2022-05-05
### Fix
- Fixed issue on correct defferable load total energy computation, following emhass v0.2.14.

## 0.1.41 - 2022-05-04
### Improvement
- Added support for semi-continuous deferrable loads.
- Changed to plotting using stairs.
- Using now lists directly defined in the options.json file.
### Fix
- Fixed issue on add-on installing caused by changed parameter type to strings.

## 0.1.40 - 2022-05-01
### Improvement
- Added support to pass list of PV plant parameters. This will enable to simulate mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
### Fix
- Fixed issue computing correct final cost values. Updated to EMHASS >> v0.2.13

## 0.1.39 - 2022-04-29
### Improvement
- Added new parameter to consider that all PV power is injected to the grid.
### Fix
- Updated to core emhass module v0.2.12.

## 0.1.38 - 2022-04-28
### Fix
- Updated to core emhass module v0.2.11.
- Improved automated docker image publish. Now building each architecture separately.

## 0.1.37 - 2022-04-26
### Fix
- Solving six module not found issue.

## 0.1.36 - 2022-04-26
### Fix
- Added gfortran to try solve netcdf4 builds on armv7 arch.
- Updated version of core emhass to solve faulty forecast from list problem.

## 0.1.35 - 2022-04-25
### Fix
- Added pkg-config and python3-h5py to try solve netcdf4 builds on armv7 arch.

## 0.1.34 - 2022-04-25
### Fix
- Added missing libhdf5-dev, libhdf5-serial-dev, netcdf-bin and libnetcdf-dev to try solve netcdf4 builds on armv7 arch.

## 0.1.33 - 2022-04-25
### Fix
- Fixed error on if condition for correct list lengths.
- Added hdf5-helpers and hdf5-tools to try solve netcdf4 builds on armv7 arch.

## 0.1.32 - 2022-04-25
### Fix
- Fixed wrong logs when passing forecasts lists.
- Updated netcdf4 version to 1.5.4 probably fixing builds on armv7 arch.

## 0.1.31 - 2022-04-24
### Fix
- Reinstated build.yaml for automatic image builder.

## 0.1.30 - 2022-04-24
### Fix
- Fixing presumed problems with falsk caching module. Now using just simple pickle object save/load.
- Added fixed image name for automated docker images pubishing.

## 0.1.29 - 2022-04-23
### Improvement
- Added automated publish of add-on images using github actions.

## 0.1.28 - 2022-04-23
### Improvement
- Prepared for using a production WSGI server.
- Rearranged app_server functions for better code visibility.
### Fix
- Fixed return problems, dropped using jinja2, now using directly Flask render_template method.

## 0.1.27 - 2022-04-21
### Fix
- Fixing flask redirects and correct response returns.
- Updated to new emhass version using now pandas get_indexer method.

## 0.1.26 - 2022-04-21
### Fix
- Fixed missing imports in flask app.

## 0.1.25 - 2022-04-21
### Fix
- Fixed error using flask returns. It was not using redirect and url_for methods.

## 0.1.24 - 2022-04-20
### Fix
- Fixed 'index' did not return a valid response errors. Added appropiate returns to flask app.

## 0.1.23 - 2022-04-18
### Fix
- Updating to a new release to build with latest emhass version as a fatal errors on pubish_data were fixed.

## 0.1.22 - 2022-04-16
### Fix
- Fixed problem of solver not found on arm64 architectures by installing the glpk solver. The install is added to the add-on Dockerfile.

## 0.1.21 - 2022-04-16
### Fix
- Fix following the improved handling of errors in EMHASS concerning solver issues with Pulp. Added support for glpk solver. For now just using a try/catch strategy but should update to solver passed as a parameter to EMHASS.

## 0.1.20 - 2022-04-13
### Fix
- Added possibility to pass web ui url as a parameter AGAIN. This functionnality was removed by error.
- Merged pull request, now using relative url in index.html

## 0.1.19 - 2022-04-12
### Fix
- Removed possibility to pass web ui url as a parameter.
- Added the possibility to pass HA instance url and token as parameters.
- Fixed errors in manual buttons on index.html

## 0.1.18 - 2022-04-05
### Added
- Added support to post list of values for forecast methods.
### Fix
- Debugged RESTful API, fixed POST requests and data handling.

## 0.1.17 - 2022-03-31
### Added
- Added the option for used defined url for the web ui.

## 0.1.16 - 2022-03-28
### Fix
- Changed Dockerfile again, now using official Home Assistant docker images.
- Added build.yaml file for multi-arch builds
- Updated server code, now using supervisor to fecth config data.

## 0.1.1 - 2022-03-28
### Fix
- Changed Dockerfile, adding C++ compilers to solve numpy install on arm archs

## 0.1.0 - 2022-03-26
### Added
- Added the first version of the EMHASS add-on


# Notes
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
