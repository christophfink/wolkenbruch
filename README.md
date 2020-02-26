# Wolkenbruch

Checks the weather forecast for a configurable place and sends an e-mail
reminder to pack your rain gear if precipitation is forecast.

Wolkenbruch makes use of the [MET Norway API](https://api.met.no/), and uses [OpenStreetmap](https://osm.org/) to find the location from place names.

### Dependencies

Wolkenbruch is written in Python 3, and depends on the Python modules [geocoder](https://geocoder.readthedocs.io/) and [requests](https://2.python-requests.org/).

### Installation

- *using `pip` or similar:*

```shell
pip3 install wolkenbruch
```

- *OR: manually:*

    - Clone this repository

    ```shell
    git clone https://gitlab.com/christoph.fink/wolkenbruch.git
    ```

    - Change to the cloned directory
    - Use the Python `setuptools` to install the package:

    ```shell
    cd wolkenbruch
    python3 ./setup.py install
    ```

- *OR: (Arch Linux only) from [AUR](https://aur.archlinux.org/packages/python-wolkenbruch):*

```shell
# e.g. using yay
yay python-wolkenbruch
```


### Configuration

Copy the example configuration file [wolkenbruch.yml.example](https://gitlab.com/christoph.fink/wolkenbruch/-/raw/master/wolkenbruch.yml.example) to a suiteable location, depending on your operating system:

- on Linux systems:
    - system-wide configuration: `/etc/wolkenbruch.yml`
    - per-user configuration: 
        - `~/.config/wolkenbruch.yml` OR
        - `${XDG_CONFIG_HOME}/wolkenbruch.yml`
- on MacOS systems:
    - per-user configuration:
        - `${XDG_CONFIG_HOME}/wolkenbruch.yml`
- on Microsoft Windows systems:
    - per-user configuration:
        `%APPDATA%\wolkenbruch.yml`

Adapt the configuration:

- Change the place the forecast searches for. For bigger cities their name might be sufficient (Unicode is supported), e.g. “Helsinki”. When it comes to smaller places, or places that share their name with other places in different parts of the world, you might have to add a country, state or county name, e.g. ”Springfield, Fife”.
- Adapt the SMTP host and credentials (leave user and password empty if not authentication is required)
- Set the sender and receiver e-mail address (they can and often will be the same address)
- If you feel like it, change the subject line and message body of the e-mail. The message body can contain [Python string formatting code](https://docs.python.org/3/library/string.html#formatstrings) for a float variable `p` (the average precipitation rate over the next 14 hours, in mm/h).

```yaml
# example configuration file
# (/etc/wolkenbruch.yml, ~/.config/wolkenbruch.yml,
#    %APPDATA%/wolkenbruch.yml, ${XDG_CONFIG_HOME}/wolkenbruch.yml)
smtp:
    host:     localhost:587
    user:     foobar
    password: BARFOO
email:
    from:     me@wherever.com
    to:       myself@wherever.com
    subject:  Pack your rain gear!
    message:  The forecast precipitation rate for today is {p:.1f}.
place: Helsinki
```

### Usage

Run `wolkenbruch` to check the precipitation for the next 14 hours and send you an e-mail reminder. Ideally, set up a cron job or a systemd timer to run `wolkenbruch` e.g. every morning.


#### Systemd timer

Copy `wolkenbruch@.service` and `wolkenbruch@.timer` from [extras/systemd/](https://gitlab.com/christoph.fink/wolkenbruch/-/tree/master/extras/systemd/) to `/etc/systemd/system/` and enable the timer to run wolkenbruch for user `christoph` every morning:

```sh
sudo systemctl daemon-reload
sudo systemctl enable --now wolkenbruch@christoph.timer 
```
