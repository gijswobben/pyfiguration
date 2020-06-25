# Command line tool
PyFiguration ships with a convenient command line tool that can generate documentation for the configuration of a script, and that can inspect a give configuration for errors and potential mistakes.

## Getting help
Run the following command to get the full usage instructions for the command line tool:

```console
$ pyfiguration --help
Usage: pyfiguration [OPTIONS] COMMAND [ARGS]...

  PyFiguration commandline tool

  Use this commandline tool to inspect scripts and have a look at the
  configuration options that the script provides. Furthermore you can
  inspect configuration files directly.

Options:
  --debug / --no-debug
  --help                Show this message and exit.

Commands:
  config  Inspect a configuration file This command will load the MODULE
          and...

  module  Inspect a module Provide a file or module to inspect it with...

$ pyfiguration config --help
Usage: pyfiguration config [OPTIONS] MODULE

  Inspect a configuration file

  This command will load the MODULE and look at the defintion. Then it will
  load the CONFIGFILE and makes sure the CONFIGFILE is valid for the
  provided MODULE.

  MODULE is the filename of the module to inspect with PyFiguraton
  CONFIGFILE is the configuration file to inspect, against the MODULE

Options:
  --help  Show this message and exit.

$ pyfiguration module --help
Usage: pyfiguration module [OPTIONS] MODULE

  Inspect a module

  Provide a file or module to inspect it with PyFiguration. This command
  will load the script from file and inspect the PyFiguration decorators to
  find out what the configuration options are. Then, it will display all the
  option as the output of this command.

  MODULE is the filename of the module to inspect with PyFiguraton

Options:
  --help  Show this message and exit.
```

## Inspect a script/module
To inspect a script or module and find out what the allowed configurations are, the command line tool can be used. An example:


```console
$ pyfiguration module basic.py 
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
$ pyfiguration config script.py --config config.yaml

$ pyfiguration config script.py --config config_with_warnings.yaml 
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
