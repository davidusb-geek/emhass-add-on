# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.12] - 2022-05-19
### Fix
- Following fixes on emhass v0.3.9

## [0.2.11] - 2022-05-17
### Fix
- Following fixes on emhass v0.3.8
- Fixing more problems when loading passed data as lists.

## [0.2.10] - 2022-05-16
### Fix
- Following fixes on emhass v0.3.6
- Properly unittested the MPC implementation.

## [0.2.9] - 2022-05-16
### Fix
- Following fixes on emhass v0.3.5

## [0.2.8] - 2022-05-16
### Fix
- Following fixes on emhass v0.3.4

## [0.2.7] - 2022-05-16
### Fix
- Fix small error in run args, following PR.

## [0.2.6] - 2022-05-15
### Fix
- Following emhass v0.3.3. Template package loading should be solved.

## [0.2.5] - 2022-05-14
### Fix
- Added 777 chmod permission to run file.

## [0.2.4] - 2022-05-14
### Fix
- Trying to fix s6 overlay issues.

## [0.2.3] - 2022-05-13
### Fix
- Trying to fix current problem using init=false in config.

## [0.2.2] - 2022-05-13
### Fix
- Following fixes on emhass v0.3.2

## [0.2.1] - 2022-05-13
### Fix
- Following fixes on emhass v0.3.1

## [0.2.0] - 2022-05-13
### Improvement
- New version of this add-on following revamping of emhass core module and release v0.3.0
- Moved the webserver to the core emhass module for easier development.
- Added Model Predictive Control optimization.

## [0.1.42] - 2022-05-05
### Fix
- Fixed issue on correct defferable load total energy computation, following emhass v0.2.14.

## [0.1.41] - 2022-05-04
### Improvement
- Added support for semi-continuous deferrable loads.
- Changed to plotting using stairs.
- Using now lists directly defined in the options.json file.
### Fix
- Fixed issue on add-on installing caused by changed parameter type to strings.

## [0.1.40] - 2022-05-01
### Improvement
- Added support to pass list of PV plant parameters. This will enable to simulate mixed orientation systems, for example one east-facing array (azimuth=90) and one west-facing array (azimuth=270).
### Fix
- Fixed issue computing correct final cost values. Updated to EMHASS >> v0.2.13

## [0.1.39] - 2022-04-29
### Improvement
- Added new parameter to consider that all PV power is injected to the grid.
### Fix
- Updated to core emhass module v0.2.12.

## [0.1.38] - 2022-04-28
### Fix
- Updated to core emhass module v0.2.11.
- Improved automated docker image publish. Now building each architecture separately.

## [0.1.37] - 2022-04-26
### Fix
- Solving six module not found issue.

## [0.1.36] - 2022-04-26
### Fix
- Added gfortran to try solve netcdf4 builds on armv7 arch.
- Updated version of core emhass to solve faulty forecast from list problem.

## [0.1.35] - 2022-04-25
### Fix
- Added pkg-config and python3-h5py to try solve netcdf4 builds on armv7 arch.

## [0.1.34] - 2022-04-25
### Fix
- Added missing libhdf5-dev, libhdf5-serial-dev, netcdf-bin and libnetcdf-dev to try solve netcdf4 builds on armv7 arch.

## [0.1.33] - 2022-04-25
### Fix
- Fixed error on if condition for correct list lengths.
- Added hdf5-helpers and hdf5-tools to try solve netcdf4 builds on armv7 arch.

## [0.1.32] - 2022-04-25
### Fix
- Fixed wrong logs when passing forecasts lists.
- Updated netcdf4 version to 1.5.4 probably fixing builds on armv7 arch.

## [0.1.31] - 2022-04-24
### Fix
- Reinstated build.yaml for automatic image builder.

## [0.1.30] - 2022-04-24
### Fix
- Fixing presumed problems with falsk caching module. Now using just simple pickle object save/load.
- Added fixed image name for automated docker images pubishing.

## [0.1.29] - 2022-04-23
### Improvement
- Added automated publish of add-on images using github actions.

## [0.1.28] - 2022-04-23
### Improvement
- Prepared for using a production WSGI server.
- Rearranged app_server functions for better code visibility.
### Fix
- Fixed return problems, dropped using jinja2, now using directly Flask render_template method.

## [0.1.27] - 2022-04-21
### Fix
- Fixing flask redirects and correct response returns.
- Updated to new emhass version using now pandas get_indexer method.

## [0.1.26] - 2022-04-21
### Fix
- Fixed missing imports in flask app.

## [0.1.25] - 2022-04-21
### Fix
- Fixed error using flask returns. It was not using redirect and url_for methods.

## [0.1.24] - 2022-04-20
### Fix
- Fixed 'index' did not return a valid response errors. Added appropiate returns to flask app.

## [0.1.23] - 2022-04-18
### Fix
- Updating to a new release to build with latest emhass version as a fatal errors on pubish_data were fixed.

## [0.1.22] - 2022-04-16
### Fix
- Fixed problem of solver not found on arm64 architectures by installing the glpk solver. The install is added to the add-on Dockerfile.

## [0.1.21] - 2022-04-16
### Fix
- Fix following the improved handling of errors in EMHASS concerning solver issues with Pulp. Added support for glpk solver. For now just using a try/catch strategy but should update to solver passed as a parameter to EMHASS.

## [0.1.20] - 2022-04-13
### Fix
- Added possibility to pass web ui url as a parameter AGAIN. This functionnality was removed by error.
- Merged pull request, now using relative url in index.html

## [0.1.19] - 2022-04-12
### Fix
- Removed possibility to pass web ui url as a parameter.
- Added the possibility to pass HA instance url and token as parameters.
- Fixed errors in manual buttons on index.html

## [0.1.18] - 2022-04-05
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

## [0.1.0] - 2022-03-26
### Added
- Added the first version of the EMHASS add-on

[0.1.0]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.0
[0.1.18]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.18
[0.1.19]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.19
[0.1.20]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.20
[0.1.21]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.21
[0.1.22]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.22
[0.1.23]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.23
[0.1.24]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.24
[0.1.25]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.25
[0.1.26]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.26
[0.1.27]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.27
[0.1.28]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.28
[0.1.29]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.29
[0.1.30]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.30
[0.1.31]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.31
[0.1.32]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.32
[0.1.33]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.33
[0.1.34]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.34
[0.1.35]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.35
[0.1.36]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.36
[0.1.37]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.37
[0.1.38]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.38
[0.1.39]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.39
[0.1.40]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.40
[0.1.41]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.41
[0.1.42]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.42
[0.2.0]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.2.0