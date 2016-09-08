import os

import click


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=False))
@click.option(
    "--dry-run",
    is_flag=True,
    help="Just show directories that would be deleted, but don't delete them.")
def cli(path, dry_run):
    """Delete all directories under the directory provided if they're empty."""

    if dry_run:
        click.echo(empty_directories(path))
    else:
        click.echo(
            "If this were real, I'd have deleted all of these directories: {0}".
            format(empty_directories(path)))


def empty_directories(path):
    return [os.path.abspath(x[0]) for x in os.walk(
        path, topdown=False) if not x[2]]
