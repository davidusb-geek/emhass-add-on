# Testing EMHASS-Add-on

To test EMHASS-Add-on integration, you will need a Home Assistant (with Supervisor) environment.

The common Home Assistant options are:

- Adding EMHASS-Add-on into a pre-existing Home Assistant environment.
- Testing EMHASS-Add-on on a Home Assistant inside a vertual test environment _(Using VS-Code)_.

See the following steps for both options.

_The following examples are for testing the EMHASS-Add-on integration _(Docker wrapper of EMHASS for Home Assistant)_. To develop/test the EMHASS Packadge itself, check EMHASS [Develop page](https://emhass.readthedocs.io/en/latest/develop.html)_.

_See [Test EMHASS-Add-On build](#Test-EMHASS-Add-On-build) for an example of testing Home Assistants Docker image build._

## Develop on VS-Code DevContainer with Home Assistant test environment

Using VS-Code DevContainers, you can generate a Home Assistant test environment for the addon before release. We can pull a version of the EMHASS package (required with EMHASS-Add-on) from a Git repo/branch, or via pip. Alternately, we can specify different pre-built EMHASS-Add-On versions _(EMHASS-Add-On Docker images)_ from DockerHub.

See the following steps:

- DockerHub:
  - Edit the `version` line from from [`config.yml`](./emhass/config.yml) to pull different versions of EMHASS-Add-On via DockerHub
- Git/pip:
  - Comment out `image: "davidusb/image-{arch}-emhass"` line from [`config.yml`](./emhass/config.yml). This will tell the addon to build from the local Dockerfile and not pull Image from DockerHub
  - Git
    - Change `build_version: addon` in [_build.yaml_](./emhass/build.yaml) to `build_version: addon-git`. _(This overrides the pip version of EMHASS specified via [requirements.txt](./emhass/requirements.txt))_
    - To specify the Git repo and branch, change lines accordingly in [*build.yaml*](/emhass/build.yaml).
      - repo: `#build_repo: https://github.com/davidusb-geek/emhass.git #addon-git mode`
      - branch: `#build_branch: master #addon-git mode`
  - pip
    - Change `emhass` version in [requirements.txt](/emhass/requirements.txt) to pull EMHASS via pip version.
      - You may need to modify the other python packages to different versions to match
- Finally
  - Run _(if not already)_  the VS-Code DevContainer _(Shortcut: `F1` > `Dev Containers: Rebuild and Reopen in Container`)_ - This requires DevContainers to be operational. See [visualstudio.com - Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers) for more info
  - Start VS-Code Task to start Home Assistant (`ctrl+shift+p`>`Tasks: Run Task`> `Start Home Assistant`)
    - Login to the generated HA Portal: `localhost:7123`
    - Navigate to Home Assistant: `Add-ons` > `ADD-ON STORE`
    - Install/Run and Test Add-on
      - For more infomation see Home Assistant's [local addon testing](https://developers.home-assistant.io/docs/add-ons/testing).

## Adding EMHASS-Add-on into pre-existing Home Assistant environment

If you would like to test a version of EMHASS-Add-on inside a pre-existing Home Assistant (with Supervisor) environment, see the following steps:

- With your preferred method of choice, clone the emhass-add-on repository to the addons folder
  - One method is to use the [`Home Assistant Add-on: SSH server`](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md) addon to add:
    - Install addon and click `OPEN WEB UI`
      - See [SSH Addon README](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md#installation) for install steps
    - Type commands:
      ```bash
      cd ~/addons/
      git clone https://github.com/davidusb-geek/emhass-add-on
      ```
- With your preferred method of choice, indicate which EMHASS package to build with (`image`), or specify what built DockerHub version of EMHASS-Add-on (`version`) to use,  in section of [`config.yml`](./emhass/config.yml) file:
  - Comment out the **image** line `image: "davidusb/image-{arch}-emhass"` if you wish to pull a EMHASS version from pip or Git repo/branch
    - ssh example:
      ```bash
      sed -i.bak '/image:/ s/./#&/' ~/addons/emhass-add-on/emhass/config.yml
      ```
  - Change **version** if you would like to pull in an older version of EMHASS-Add-on _(pre built Docker image)_ from DockerHub (Default state)
    - ssh example:
      ```bash
      emhassVersion=0.6.5
      sed -i.bak "s/version:.*/version: $emhassVersion/g"  ~/addons/emhass-add-on/emhass/config.yml
      ```
- If you want EMHASS from **pip**:
  - To specify the EMHASS pip version, modify the `emhass` version number in [requirements.txt](/emhass/requirements.txt)
    - ssh example:
        ```bash
        emhassVersion=0.7.7
        sed -i.bak "s/emhass==.*/emhass==$emhassVersion/g"  ~/addons/emhass-add-on/emhass/requirements.txt
        ```

- If you want EMHASS from **Git**:
  - Tell the addon to use Git, and specify what EMHASS repo and branch you would like to pull.

    - To tell Docker to pull from Git, change the build argument from `addon` to `addon-git` in the [_build.yaml_](./emhass/build.yaml).
      - ssh example:
        ```bash
        sed -i.bak "s/build_version:.*/build_version: addon-git/g"  ~/addons/emhass-add-on/emhass/build.yaml
        ```
    - To specify the EMHASS Git repository and branch values, _(optional)_ change lines in [*build.yaml*](/emhass/build.yaml):
      - `#build_repo: https://github.com/davidusb-geek/emhass.git #addon-git mode`
      - `#build_branch: master #addon-git mode`

      - ssh example:

        ```bash
        repo=https://github.com/daviasdasdsasddusb-geek/emhass.git
        branch=masaddasdasdter

        sed -i.bak "s%build_repo:\s.*%build_repo: $repo%g"  ~/addons/emhass-add-on/emhass/build.yaml
        sed -i.bak "s/build_branch:\s.*/build_repo: $branch/g"  ~/addons/emhass-add-on/emhass/build.yaml
        ```

- Finally:
  - head to Home Assistant: `Add-ons` > `ADD-ON STORE`
    - you should see an `EMHASS` addon under `Local add-ons`
      - If you don't, try hamburger button _(3 dots)_ on top right > check updates > refresh page
  - Install and test addon
  - Use the Supervisor logs _(on the config/logs page)_ to see any logs with the addon.

## Test EMHASS-Add-On build

You can test the EMHASS-Add-On docker image build using the Home Assistant builder.

**emhass-add-on local repo**

Linux example:

```bash
architecture=amd64 #your host machine architecture

docker run --rm --privileged -v ~/.docker:/root/.docker -v ${PWD}:/data ghcr.io/home-assistant/${architecture}-builder:latest --test --${architecture} --target /data/emhass
```

_confirm terminal directory is in root `emhass-add-on` folder_

**emhass-add-on Git repo**

Linux example:

```bash
architecture=amd64 #your host machine architecture

repo=https://github.com/davidusb-geek/emhass-add-on.git #repo example
branch=main #branch example

docker run --rm --privileged -v ~/.docker:/root/.docker ghcr.io/home-assistant/${architecture}-builder:latest --test --${architecture} --target emhass -r ${repo} -b ${branch}
```
