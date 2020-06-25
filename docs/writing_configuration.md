# Writing configuration

## Specifying configurations
The recommended way to define configurations with PyFiguration is to decorate the function that uses the configuration. This way you always have the definition of the configuration close to where the configuration is used. PyFiguration comes with a set of decorators that create different types of fields.

The sections below show examples of how fields can be specified. For the full list of options per type, check out the [API](api) section of this documentation.

### Integers
```python
@conf.add_int_field("port", description="The port number of a server")
@conf.add_int_field("port", minValue=80, maxValue=999)
@conf.add_int_field("port", default=10)
@conf.add_int_field("port", required=False)
```

### Floats
```python
@conf.add_float_field("length", description="The length in cm")
@conf.add_float_field("length", minValue=10.0, maxValue=100.0)
@conf.add_float_field("length", default=10.0)
@conf.add_float_field("length", required=False)
```

### Strings
```python
@conf.add_string_field("host", description="The url of the host to connect to")
@conf.add_string_field("host", allowedValues=["localhost", "remotehost"])
@conf.add_string_field("host", required=False)
```

### Booleans
```python
@conf.add_boolean_field("isRemote", description="Whether or not something is true")
@conf.add_boolean_field("isRemote", required=False)
```

### Lists
```python
@conf.add_list_field("users", description="A list of users that should have access")
@conf.add_list_field("users", allowedValues=["admin", "myusername"])
@conf.add_list_field("users", required=False)
```

## Nested fields
It is possible to nest configurations (e.g. in sections). This is standard practice in `YAML` and `JSON` files and is supported by PyFiguration. Just define the configuration field in "dot-notation". Combine all the sections of the path to the key you would like to define with ".". Here is an example:

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
```
