# Testing EMHASS-Add-on

To fully test EMHASS and its EMHASS-Add-on integration, you will likely want to test the EMHASS addon in a Home Assistant Operating System environment (HAOS/Supervisor).

The common Home Assistant options are:

- Adding EMHASS-Add-on into a pre-existing Home Assistant environment.
- Testing EMHASS-Add-on on a Home Assistant with virtual test environment with VS-Code Dev Containers.

See the following steps for both options.

_Note: The following examples are for testing the EMHASS-Add-on integration with Home Assistant. To develop/test the EMHASS Package and its Docker container itself, check the EMHASS [Develop page](https://emhass.readthedocs.io/en/latest/develop.html)_.

## Develop on VS-Code Dev Container with Home Assistant test environment

Using VS-Code Dev Containers, you can generate a Home Assistant test environment for the EMHASS Add-on before release. The steps to achieve this are as follows:  
</br>
_Note: These following steps require VS-Code and the Dev Container Extension to be installed and operational. See ['Developing inside a Container'](https://code.visualstudio.com/docs/DevContainers/containers) for more information._


1) Git clone `EMHASS-Add-on` repository and open VS-code 
    ```bash
    git clone https://github.com/davidusb-geek/emhass-add-on.git
    cd emhass-add-on
    code .
    ```

2) Adjust the EMHASS image to the version you would like to test. To adjust the image, you may select one of three options:
    - Change the EMHASS Docker image version tag
    - Change the EMHASS Docker image repository
    - Build a custom image of EMHASS locally  

    See [Customizing EMHASS](##Customizing-EMHASS) for more information.

3) Run Home Assistant Environment
    - Run _(if not already)_  the VS-Code Dev Container
      - Shortcut: `F1` > `Dev Containers: Rebuild and Reopen in Container`
    - Start VS-Code Task to start Home Assistant 
      - `ctrl+shift+p`>`Tasks: Run Task`> `Start Home Assistant`
      - Login to the generated HA Portal: `localhost:7123`
      - Navigate to Home Assistant: 
        - `Add-ons` > `ADD-ON STORE`
      - Install/Run and Test Add-on
        - For more information see Home Assistant's [Local add-on testing](https://developers.home-assistant.io/docs/add-ons/testing).

_Note: If, on run, the emhass version looks off. Try: uninstalling Add-on, `check for updates` on Add-on Store page, and re-installing._

## Adding EMHASS-Add-on into pre-existing Home Assistant environment

If you would like to test a version of EMHASS-Add-on inside a pre-existing Home Assistant (with Supervisor) environment, see the following steps:

1) With your preferred method of choice, clone the emhass-add-on repository to the addons folder
    - One method is to use the [`Home Assistant Add-on: SSH server`](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md) addon to add:
      - Install addon and click `OPEN WEB UI`
        - See [SSH Addon README](https://github.com/home-assistant/addons/blob/master/ssh/DOCS.md#installation) for install steps
      - Type commands to clone repository:
        ```bash
        cd ~/addons
        git clone https://github.com/davidusb-geek/emhass-add-on
        cd ./emhass-add-on
        ```
2) Adjust the EMHASS image to the version you would like to test. To adjust the image, you may select one of three options:
    - Change the EMHASS Docker image version tag
    - Change the EMHASS Docker image repository
    - Build a custom image of EMHASS locally  

    See [Customizing EMHASS](##Customizing-EMHASS) for more information.

3) Run EMHASS addon:
    - head to Home Assistant: `Add-ons` > `ADD-ON STORE`
      - you should see an `EMHASS` Add-on under `Local add-ons`
        - If you do not, try hamburger icon ☰ on top right > `check updates` > refresh page
    - Install and test Add-on
    - Use the Supervisor logs _(on the config/logs page)_ to see any logs with the Add-on.

</br>

_Note: If, on run, the emhass version looks off. Try: uninstalling Add-on, check for updates on the Add-on Store page, and re-install._

## Customizing EMHASS 
If you are testing EMHASS-Add-on, it is likely that you would want to select a particular version of EMHASS to run and test.
There are different methods of achieving this, depending on where the source of the desired EMHASS package resigns. See examples bellow: 

### Change the EMHASS Docker image version tag
If you would like to solely change the EMHASS version _(i.e. Image tag)_ of the EMHASS package. (keeping the Docker repository to [ghcr.io/davidusb-geek/emhass](https://github.com/davidusb-geek/emhass/pkgs/container/emhass)). Follow the steps bellow:

1) Change the `version:` line in the emhass-add-on `config.yml`:
    ```bash
    emhassVersion=v0.20.0
    sed -i.bak "s/version:.*/version: $emhassVersion/g"  ~/addons/emhass-add-on/emhass/config.yml
    ```
*Make sure the version you select matches one of the tagged images in https://github.com/davidusb-geek/emhass/pkgs/container/emhass*

### Change the EMHASS Docker image repository
If you would like to test your own forked version of EMHASS, the container repository can be changed to match your forked repository. The steps to accomplish this include:  
 _(building your own EMHASS image)_

1) If not already, enable the Github Actions in your EMHASS fork 
    - Head to the actions tag on your github fork (E.g. https://github.com/YOURUSERNAME/emhass/actions)
    - Read the warnings and observe the workflow files on the repo (https://github.com/YOURUSERNAME/emhass/tree/master/.github/workflows)
    - If you understand the workflows and accept the warnings, press `I understand my workflows, go ahead and enable them`

2) Create a github release of your EMHASS fork
    - In your EMHASS fork, draft a new release to trigger the github action to build the docker image 
      - Head the releases page of your fork and draft a new release (https://github.com/YOURUSERNAME/emhass/releases/new)
    - In `choose a new tag` create a new suitable tag name (E.g. `v2.0.0`)
    - Change `Target` if you wish to select a branch that is not the default `master`
    - When happy, click `publish release`
    - Head to the Actions page of your fork again to observe the `publish_docker` workflow running. Once its finished, if successful, a new Docker image should be available in the packages page of your Github repo (https://github.com/YOURUSERNAME/emhass/pkgs/container/emhass) 

3) In your home assistant environment change the `version:` and `image:` lines in the addons config.yml
    - In the package page on Github copy the repository url and tag name provided (E.g. Repo:`ghcr.io/YOURUSERNAME/emhass` Tag:`v2.0.0`)
    - Edit the version/tag and image/repo sections of the config.yaml
      ```bash
      emhassVersion=v2.0.0
      emhassRepo="ghcr.io/YOURUSERNAME/emhass"
      sed -i.bak "s%version:.*%version: $emhassVersion%g"  ~/addons/emhass-add-on/emhass/config.yml
      sed -i.bak "s%image:.*%image: $emhassRepo%g"  ~/addons/emhass-add-on/emhass/config.yml
      ```

 ### Build a custom image of EMHASS locally
 The last option requires merging the EMHASS-Add-on and EMHASS repository together, allowing the user to build EMHASS, and the Docker container locally. The best use case for this method if for rapid testing. Since you can adjust the emhass source files and rebuild the addon. This is the most complicated approach and the example bellow is not guaranteed to work.

```bash
cd ~/addons/emhass-add-on/
# git clone EMHASS repo (or forked emhass repo)
git clone https://github.com/davidusb-geek/emhass.git ./emhass-git
# copy required EMHASS files to the emhass-add-on root
cp ./emhass-git/Dockerfile ./emhass/
cp ./emhass-git/requirements.txt ./emhass/
cp ./emhass-git/README.md ./emhass/README.md
cp -R ./emhass-git/src ./emhass/
cp -R ./emhass-git/setup.py ./emhass/
cp -R ./emhass-git/data ./emhass/
# comment out the `image:` line of the emhass-add-on config.yml file. To tell Home Assistant to build the Dockerfile locally
sed -i.bak '/image:/ s/./#&/' ~/addons/emhass-add-on/emhass/config.yml
# Replace TARGETARCH with BUILD_ARCH (Home Assistant Build ARG) in Dockerfile 
sed -i.bak "s/TARGETARCH/BUILD_ARCH/g"  ~/addons/emhass-add-on/emhass/Dockerfile
```
*Note: It is recommended to regularly adjust the `version:` tag_(in `config.yml`)_ after a change and before a test. This helps the user to check if Home Assistant has received the update.*
