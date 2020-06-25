# Writing configuration

## Specifying configurations
The recommended way to define configurations with PyFiguration is to decorate the function that uses the configuration. This way you always have the definition of the configuration close to where the configuration is used. PyFiguration comes with a set of decorators that create different types of fields.