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
