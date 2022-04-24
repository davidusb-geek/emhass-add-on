# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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