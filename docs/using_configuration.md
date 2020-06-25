# Using configurations
When you've defined the configuration your script needs, using the decorators, and you've written a configuration file it's time to use this configuration with your script. PyFiguration will automatically parse the `--config CONFIGFILES` arguments to your script and use them (in order!) to load the configuration for your script.

## Simple configurations
In the simplest form you can use a single config file with your script like this:

```yaml
# config.yaml
database:
  host: localhost
  port: 8000
```

```python
# script.py
from pyconfiguration import conf

@conf.add_string_field("database.host", description="The database URL")
@conf.add_int_field("database.port", description="The port to connect to on the database")
def connect():
    host = conf["database"]["host"]
    port = conf["database"]["port"]
    print(f"Host: {host}")
    print(f"Port: {port}")
    ...
```

```console
$ python script.py --config config.yaml
Host: localhost
Port: 8000
...
```

## Configuration inheritance
When you specify more than 1 configuration file to be used with your script, PyFiguration will go over the specified files one by one, and load all of them. The order in which you provide the configuration files matters! Configurations from the first file will be overwritten with configurations from the second, and so on.

This allows patterns like this:

```console
$ ls .
config.yaml        defaults.yaml       script.py

$ python script.py --config defaults.yaml config.yaml
```

In this example PyFiguration will first load the defaults from `defaults.yaml` and will then overwrite the configuration that are also specified in `config.yaml`.


## From directories
PyFiguration is also able to accept a directory of configuration files on the command line. If a directory is specified, PyFiguration will go through the directory and load all `.yaml`, `.yml`, and `.json` files, also from subdirectories. Note that the order is not guaranteed!

This allows patterns like this:

```console
$ ls
defaults/          deployments/        script.py

$ ls defaults/
database.yaml      server.yaml

$ ls deployments/
deployment_a.yaml  deployment_b.yaml

$ python script.py --config defaults/ deployments/deployment_a.yaml
```

In this example we have default configurations for the server and the database in separate files in the `defaults/` folder. We provide our script with the folder so it will load both. Then we provide the script with one of the deployment files to overwrite some of the defaults.
