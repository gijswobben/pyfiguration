from click.testing import CliRunner
from pyfiguration import cli


def test_cli_module():
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "config",
            "./examples/basic/basic.py",
            "--config",
            "./examples/basic/config/defaults",
            "./examples/basic/config/deployments/a.yaml",
        ],
    )
    assert result.exit_code == 0
    assert result.output == ""
