# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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