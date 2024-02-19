# Testing emhass-add-on on an HA development environment

We can use VS-Code DevContainers to generate a test environment for the addon before release.
See the Following steps:

_Make sure the `image:` is commented out from `config.yaml` before starting (to use local Dockerfile)_

## Change Docker Build Argument to `addon-git`

- In EMHASS Addon's default state, EMHASS is pulled inside a Docker container wth pip _(specified via requirements.txt)_. As we want to test with an diffrent version of EMHASS, we can change `build_version: addon` in _build.yaml_ to `build_version: addon-git`.
  - This will compile a version of EMHASS via a github repo and branch specified.
- We can then edit the git repo and branch inside `#EMHASS-ADD-ON testing with git` section of the _Dockerfile_.
- Next we will need to run the VS-Code DevContainer _(if haven't already)_, login to localhost:7123 and add/run the addon to test.
  - See the Home Assistant [local addon testing](https://developers.home-assistant.io/docs/add-ons/testing) for more info.
