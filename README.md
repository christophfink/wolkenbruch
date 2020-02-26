# Wolkenbruch

Checks the weather forecast for a configurable place and sends an e-mail
reminder to pack your rain gear if precipitation is forecast.

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
place: Helsinki
```
