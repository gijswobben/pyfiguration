# Command line tool
PyFiguration ships with a convenient command line tool that can generate documentation for the configuration of a script, and that can inspect a give configuration for errors and potential mistakes.

## Getting help
Run the following command to get the full usage instructions for the command line tool:

```console
$ pyfiguration --help
usage: pyfiguration [-h] {inspect} ...

PyFiguration commandline tool

Use this commandline tool to inspect scripts and have a look at the
configuration options that the script provides. Furthermore you can
inspect configuration files directly.

optional arguments:
  -h, --help  show this help message and exit

Commands:
  {inspect}
    inspect   Inspect configurations and scripts



$ pyfiguration inspect --help
usage: pyfiguration inspect [-h] {config,script} ...

Inspect configuration files, scripts or modules to see which values are
allowed, or to check if a provided configuration file is valid for a specific
script.

optional arguments:
  -h, --help       show this help message and exit

Commands:
  The type object you would like to inspect

  {config,script}
    config         Inspect a configuration file to see if it is valid for a
                   given script
    script         Inspect a script to see what configuration options are
                   available



$ pyfiguration inspect script --help
usage: pyfiguration inspect script [-h] [-s SCRIPT]

Provide a file or script to inspect it with PyFiguration. This command will
load the script from file and inspect the PyFiguration decorators to find out
what the configuration options are. Then, it will display all the option as
the output of this command. SCRIPT is the filename of the script to inspect
with PyFiguraton

optional arguments:
  -h, --help            show this help message and exit
  -s SCRIPT, --script SCRIPT
                        The script against which to inspect the config



$ pyfiguration inspect config --help
usage: pyfiguration inspect config [-h] [-c [CONFIG [CONFIG ...]]] [-s SCRIPT]

This command will load the SCRIPT and look at the defintion. Then it will load
the CONFIG file and makes sure the CONFIG file is valid for the provided
SCRIPT. SCRIPT is the filename of the SCRIPT to inspect with PyFiguraton,
CONFIG file is the configuration file to inspect, against the SCRIPT.

optional arguments:
  -h, --help            show this help message and exit
  -c [CONFIG [CONFIG ...]], --config [CONFIG [CONFIG ...]]
                        The configuration file to inspect
  -s SCRIPT, --script SCRIPT
                        The script against which to inspect the config
```

## Inspect a script/module
To inspect a script or module and find out what the allowed configurations are, the command line tool can be used. An example:


```console
$ pyfiguration inspect script -s basic.py
The following options can be used in a configuration file for the module 'basic.py':
db:
  host:
    allowedDataType: str
    default: localhost
    description: Location of the database, e.g. localhost
    required: true
  port:
    allowedDataType: int
    default: 8000
    description: Port of the database to connect on
    maxValue: 9999
    minValue: 80
    required: true
```

In this example we've inspected a script called `basic.py`. The output shows (in `YAML` format) which fields can be specified in a configuration file, what type the value should have, and how this value is checked (e.g. `minValue: 80` will check any configuration file to make sure the value for the field `port` is `>=` 80).


## Inspect a configuration file
If you have a script, and a configuration file, you can check the configuration file to see if it's valid for your script. Example:

```console
$ pyfiguration inspect config -s script.py -c config.yaml

$ pyfiguration inspect config -s script.py -c config_with_warnings.yaml
--------
 Errors
--------
   ✗ Value '500.0' is not of the correct type. The allowed data type is: int
----------
 Warnings
----------
   ! Key 'server.not_needed_key' doesn't exist in the definition and is not used in the module.
```

In this example we run the inspector 2 times. The first time with a valid configuration file (so nothing is returned). The second time we have a configuration file with errors. Apparently we've specified a float where we should have specified an integer. Also, we've defined a key in our configuration that is not used by the script. This will not break the script, but because it might result in unexpected behaviour it's raised as a warning.
