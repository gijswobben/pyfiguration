from __future__ import annotations

import os
import io

from typing import TYPE_CHECKING
from contextlib import redirect_stdout
from behave import given, when, then
from pyfiguration.cli import inspectScript


# Import the Context class for type checking purposes only
if TYPE_CHECKING:
    from behave.runner import Context


@given('we have example script "{script}" in the folder "{folder}"')
def step(context: Context, script: str, folder: str):
    """ Step that provides the condition of an example script.

    Args:
        context (Context): The run context
        script (str): The script
        folder (str): The folder where the script can be found

    Raises:
        scriptNotFound
    """

    # Make sure the file exists
    assert os.path.isfile(os.path.join(folder, script)), "Script not found"

    # Set the path of the script on the context for later use
    context.script = os.path.join(folder, script)


@when("we inspect the script with pyfiguration")
def step(context: Context):
    """ Step that uses PyFiguration to inspect a script.

    Args:
        context (Context): The run context
    """

    # Capture the output on stdout (printing) because this is a CLI tool
    f = io.StringIO()
    with redirect_stdout(f):

        # Inspect the script
        inspectScript(script=context.script)

    # Store the printed output on the context
    context.output = f.getvalue()


@then('the output should start with "{text}"')
def step(context: Context, text: str):
    """ Step that tests the output of the tests for a specific string.

    Args:
        context (Context): The run context
        text (str): The text that should be at the beginning of the output
    """

    # Make sure there are no errors
    assert context.failed is False

    # Test the inspect output
    assert context.output.startswith(text), text
