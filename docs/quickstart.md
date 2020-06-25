# Quickstart
The following instructions will get you up and running in no time.

## Install PyFiguration
Run the following command to install PyFiguration:

```console
$ pip install pyfiguration
```
Or add PyFiguration to your `requirements.txt` or `setup.py`.

## Import PyFiguration in your script
Add the following line to any script to start making use of PyFiguration:

```python
from pyfiguration import conf
```

## Create new configuration options
Decorate your functions to define which configurations should be made available, and how to check if the provided values are valid. Example:

```python
@conf.add_int_field("port", minValue=80, maxValue=9999, default=8000)
def my_function():
    ...
```

## Use configuration in your code
The `conf` object will contain all the parsed configurations. Just access the value like this:

```python
port = conf["port"]
```

## Write a config file
Running with default values can be fine, but of course you want to be able to overwrite them. Define a `YAML` or `JSON` file with your config, and provide the file as an argument to your script when running:

```yaml
# config.yaml
port: 6000
```

```console
$ python my_script.py --config config.yaml
```
