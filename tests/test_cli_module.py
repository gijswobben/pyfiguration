from click.testing import CliRunner
from pyfiguration import cli


def test_cli_module():
    runner = CliRunner()
    result = runner.invoke(cli, ["module", "./examples/basic/basic.py"])
    assert result.exit_code == 0
    assert result.output.startswith(
        "The following options can be used in a configuration file for the module"
    )
