Feature: Inspect a script with PyFiguration

  Scenario Outline: Inspect an example script
     Given we have example script "<script>" in the folder "<folder>"
      When we inspect the script with pyfiguration
      Then the output should start with "The following options can be used in a configuration file for the module"

    Examples:
        | script     | folder             |
        | script.py  | ./examples/simple  |
        | basic.py   | ./examples/basic   |
