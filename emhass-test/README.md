<!-- markdown file presented on the main addon info tab -->

# EMHASS Add-on

### A Home Assistant Add-on for the EMHASS module: Energy Management for Home Assistant

</br>

<div style="display: flex;">
This add-on uses the EMHASS core module from the following GitHub repository:
&nbsp; &nbsp;
<a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass">
    <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_button.svg" alt="EMHASS">
</a>
</div>

</br>

<div style="display: flex;">
The complete documentation for this module can be found here:
&nbsp; &nbsp;
<a style="text-decoration:none" href="https://emhass.readthedocs.io/en/latest/">
    <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Documentation_button.svg" alt="Documentation">
</a>
</div>

</br>

<div style="display: flex;">
For any questions on EMHASS or EMHASS-Add-on:
&nbsp; &nbsp;
<a style="text-decoration:none" href="https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant/338126">
    <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Community_button.svg" alt="Community">
</a>
</div>

</br>

<div style="display: flex;">
For any Issues/Feature Requests for the EMHASS core module, create a new issue here:
&nbsp; &nbsp;
<a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass/issues">
    <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Issues_button.svg" alt="Issues">
</a>
</div>

## Installation

The steps to install EMHASS as an Home Assistant addon:

1) Add the EMHASS-Add-on repository to the HAOS add-on store

    - To install add the EMHASS Add-on repository in the Home Assistant store, follow [these steps](https://www.home-assistant.io/common-tasks/os/#installing-third-party-add-ons)

    - This will be: Configuration > Add-ons & Backups open the add-on store > Add the URL of the repository (e.g https://github.com/davidusb-geek/emhass-add-on) and then press "Add".

2) Install the EMHASS Add-on 
    - Look for the EMHASS Add-on tab and when inside the Add-on click on `install`.
      - The installation may take some time depending on your hardware.

3) Start the EMHASS addon
    - Once installed, head into the EMHASS addon
    - click `start` to start the EMHASS web server
      -  For consistent use, it is recommended that you enable: `Show in sidebar`,`Watchdog` and `Start on boot `

4) Open the EMHASS web interface, and configure parameters
    - Click `OPEN WEB UI` to enter the EMHASS web server
    - Click the cog icon ⚙️  to to enter the emhass configuration page
    - Insert your user specific parameters
      - For users who wish to use `Solcast` or `Forecast.Solar` insert your secrets in the Home Assistant EMHASS configuration page, under `Show unused optional configuration options`. (E.g: `localhost:8123/hassio/addon/emhass/config`)

## Installation Method 2 - Manually changing EMHASS version
This method allows the user to select which EMHASS version to run _(via adjusting the Docker version tag)_. This second method of installation may be more preferable for users who wish to test EMHASS or rollback to a older stable version.   
_Warning: This method will override the Docker image tag, and therefore will require the user to manually adjust the tag to update. The user will also need to regularly check to see if the EMHASS-Add-on repository is up to date with the Github `main` branch_

1) Have a method of inserting commands
    - Two Addon options are [Terminal & SSH](https://github.com/home-assistant/addons/tree/master/ssh) and Community Add-on: [Studio Code Server](https://github.com/hassio-addons/addon-vscode)

2) Clone the `EMHASS-Add-on` repository into your `/addons` directory 
    ```bash
    cd ~/addons/
    git clone https://github.com/davidusb-geek/emhass-add-on.git
    ```

3) Specify what EMHASS version image to use
    - in the `emhass-add-on/emhass/config.yml` adjust the `version:` line to match the version of choice:
      ```bash
      # set version here 
      emhassVersion=v0.20.0
      # sed command to replace version line in config.yml 
      sed -i.bak "s/version:.*/version: $emhassVersion/g"  ~/addons/emhass-add-on/emhass/config.yml
      ```
4) Head to the Home Assistant add-on store and refresh addon cache
    - Settings > Add-ons > Add-on Store
    - Refresh Addon cache with: hamburger icon ☰ > Check for updates
    - Wait half a minute and refresh the page 

5) Install local version of EMHASS 
    - From here a new Addon Source under the name `Local add-ons` should appear _(if not repeat step 4)_
    - Install the EMHASS addon, Note: after clicking the EMHASS addon, the `Current version: ` Tag on the top left of the EMHASS card.


## Developing EMHASS/EMHASS-Add-on

#### **EMHASS**
For those who want to develop the EMHASS package itself. Have a look at the [Develop page](https://emhass.readthedocs.io/en/latest/develop.html). _(EMHASS docs)_ 

#### **EMHASS-Add-on**
For those who want to test the EMHASS addon _(EMHASS inside of a virtual Home Assistant Environment)_. Have a look at [Test Markdown](./Test.md).

## License

MIT License

Copyright (c) 2021-2025 David HERNANDEZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
