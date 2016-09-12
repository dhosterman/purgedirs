import os
import shutil

import click

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("path", type=click.Path(exists=True, file_okay=False))
@click.option(
    "--include-provided-path",
    is_flag=True,
    help="Delete the path provided as well, assuming all other criteria are met."
)
@click.option(
    "-d",
    "--dry-run",
    is_flag=True,
    help="Just show directories that would be deleted, but don't delete them.")
def cli(path, dry_run, include_provided_path):
    """Delete all directories under the directory provided if they're empty."""

    if dry_run:
        click.echo(empty_directories(path))
    else:
        for path in empty_directories(path, include_provided_path):
            shutil.rmtree(path)
            click.echo("Removing: {0}".format(path))


def empty_directories(path, include_provided_path=False):
    directories = [os.path.abspath(x[0]) for x in os.walk(
        path, topdown=False) if not x[2]]
    if not include_provided_path:
        directories.pop()
    return directories
