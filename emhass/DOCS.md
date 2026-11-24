<!-- markdown file presented on the documentation tab -->

# EMHASS Add-on

<div>
 <a style="text-decoration:none" href="https://emhass.readthedocs.io/en/latest/">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Documentation_button.svg" alt="EMHASS Documentation">
  </a>
   <a style="text-decoration:none" href="https://community.home-assistant.io/t/emhass-an-energy-management-for-home-assistant/338126">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Community_button.svg" alt="Community">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass/issues">
      <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/Issues_button.svg" alt="Issues">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass-add-on">
     <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_Add_on_button.svg" alt="EMHASS Add-on">
  </a>
  <a style="text-decoration:none" href="https://github.com/davidusb-geek/emhass">
     <img src="https://raw.githubusercontent.com/davidusb-geek/emhass/master/docs/images/EMHASS_button.svg" alt="EMHASS">
  </a>
</div>

---

### A Home Assistant Add-on for the EMHASS (Energy Management for Home Assistant) module

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

## Planning with another EMHASS

EMHASS's coordinated backend can plan this home together with another EMHASS, for example one running a garage. The settings are on the add-on's Configuration page:

- **This EMHASS serves a coordinator:** set `participant_token` (at least 16 characters) and, in the EMHASS configuration, `participant_api`. The coordinator reaches this EMHASS at `http://<home-assistant-host>:5000/participant`, not through ingress.
- **This EMHASS coordinates another one:** add an entry to `remote_solver_tokens` for each remote solver in your `site` configuration. `name` is the remote's `token_secret`, and `token` is that EMHASS's `participant_token`. A remote reached over plain `http://` on another machine also needs `"trusted_network": true` on its `solver`, or this EMHASS won't send it the token; use `https://` where you can. Use **HTTPS** whenever possible. Plain HTTP sends the token unencrypted and exposes it to anyone on the network path. Only enable `trusted_network` on a private network that you fully control.

> **Note on token precedence and rotation:** Values defined in `secrets_emhass.yaml` override the Configuration-page options for both `participant_token` and `remote_solver_tokens` entries. When rotating either token, update or remove the matching key in `secrets_emhass.yaml` (including for remote token names) so the new value takes effect.

See the [coordinated backend documentation](https://github.com/davidusb-geek/emhass/blob/master/docs/coordinated_backend.md) for the `site` configuration.

## Developing EMHASS/EMHASS-Add-on

#### **EMHASS**
For those who want to develop the EMHASS package itself. Have a look at the [Develop page](https://emhass.readthedocs.io/en/latest/develop.html). _(EMHASS docs)_ 

#### **EMHASS-Add-on**
For those who want to test the EMHASS addon _(EMHASS inside of a virtual Home Assistant Environment)_. Have a look at [Test Markdown](./emhass/Test.md).

## License

MIT License

Copyright (c) 2021-2026 David HERNANDEZ TORRES

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
