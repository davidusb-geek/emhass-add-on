# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

## [0.1.0] - 2022-03-26
### Added
- Added the first version of the EMHASS add-on

[0.1.0]: https://github.com/davidusb-geek/emhass-add-on/releases/tag/v0.1.0