# Testing EMHASS-Add-on 
To test the EMHASS-Add-on integration, you will need a Home Assistant (with Supervisor) environment to test in. 

The common Home Assistant options are: 
- Adding EMHASS-Add-on into a pre-existing Home Assistant environment.
- Testing EMHASS-Add-on on a Home Assistant addon test environment *(Using VS-Code)*.   

See the following steps for both options. 

*The following examples are for testing the EMHASS-Add-on integration. To Develop/test the EMHASS itself, check EMHASS [Develop page](https://emhass.readthedocs.io/en/latest/develop.html)*.


## Develop on VS-Code DevContainer with Home Assistant test environment
Using VS-Code DevContainers, you can generate a Home Assistant test environment for the addon before release. We can pull a version of EMHASS from a DockerHub or from a github repo/branch. 

See the following steps:


- DockerHub:  
    - Edit the `version` line from from [`config.yml`](./emhass/config.yml) to pull different versions of EMHASS via DockerHub
- Git:  
    - Comment out the ```image: "davidusb/image-{arch}-emhass"``` line from [`config.yml`](./emhass/config.yml). This will tell the addon to build from the local Dockerfile and not pull Image from DockerHub.
    - Change `build_version: addon` in [_build.yaml_](./emhass/build.yaml) to `build_version: addon-git`. _(This overrides the pip verion of EMHASS specified via [requirements.txt](./emhass/requirements.txt))_
    - To specify the git repo and branch, edit the corresponding lines inside `#EMHASS-ADD-ON testing with git` section of the [_Dockerfile_](./emhass/Dockerfile).
        - repo: `RUN git clone https://github.com/davidusb-geek/emhass.git`
        - branch: `RUN git checkout master`
- Finally 
    - Run the VS-Code DevContainer _(if haven't already)_ *(Shortcut: `F1` > `Dev Containers: Rebuild and Reopen in Container`)*
        - This requires DevContainers to be operational. See [visualstudio.com - 
Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers) for more info
    - Start task to start Home Assistant (`ctrl+shift+p`>`Tasks: Run Task`> `Start Home Assistant`)
    - Login to the generated HA Portal `localhost:7123` 
    - head to Home Assistant: `Add-ons` > `ADD-ON STORE` 
    - Run and Test Add-on
        - See more information about the following steps on Home Assistant's [local addon testing](https://developers.home-assistant.io/docs/add-ons/testing).


## Adding EMHASS-Add-on into pre-existing Home Assistant environment
If you would like to test a version of EMHASS-Add-on inside a pre-existing Home Assistant (with Supervisor) environment, see the following steps:

- With your preferred method of choice, clone the emhass-add-on repository to the addons folder
    - One method is to use the `Home Assistant Add-on: SSH server` addon to add:
        - Install and click `OPEN WEB UI`
        - Type commands:
            ```bash
            cd ~/addons/
            git clone https://github.com/davidusb-geek/emhass-add-on
            ```
- With your preferred method of choice, edit the `versions` or `image` section of [`config.yml`](./emhass/config.yml) 
    - Comment out the line ```image: "davidusb/image-{arch}-emhass"``` if you wish to pull a EMHASS version from a git repo/branch 
        - ssh example:
            ```bash
            sed -i.bak '/image:/ s/./#&/' ~/addons/emhass-add-on/emhass/config.yml
            ```
    - Change version if you would like to pull in an older version of EMHASS from DockerHub
        - ssh example:
            ```bash
            emhassVersion=0.6.5
            sed -i.bak "s/version:.*/version: $emhassVersion/g"  ~/addons/emhass-add-on/emhass/config.yml
            ```
- If Using Git:
    - If you have chosen to pull from git, we tell the addon to use git, and specify what EMHASS repo and branch you  would like to pull.
        - To tell Docker to pull from git, change the build argument from `addon` to `addon-git` in the  [_build.yaml_](./emhass/build.yaml).
            - ssh example:
                ```bash
                sed -i.bak "s/build_version:.*/build_version: addon-git/g"  ~/addons/emhass-add-on/emhass/build.yaml
                ```
        - To specify the EMHASS git repository and branch edit lines `RUN git clone https://github.com/davidusb-geek/emhass.git` and `branch: RUN git checkout master` in the [_Dockerfile_](./emhass/Dockerfile).
            - ssh example:
                ```bash
                repo=https://github.com/davidusb-geek/emhass.git
                branch=master
                
                sed -i.bak "s%RUN git clone.*%RUN git clone $repo%g"  ~/addons/emhass-add-on/emhass/Dockerfile
                sed -i.bak "s/RUN git checkout.*/RUN git checkout $branch/g"  ~/addons/emhass-add-on/emhass/Dockerfile
                ```        
- On Both, Finally:
    - head to Home Assistant: `Add-ons` > `ADD-ON STORE` 
        - you should see an `EMHASS` addon under `Local add-ons`
            - If you don't, try hamburger button (3 dots) on top right > check updates > refresh page
    - Install and test addon
    - Use the Supervisor logs *(on the config/logs page)* to see any logs with the addon.        

