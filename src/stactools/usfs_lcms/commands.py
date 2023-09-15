import logging

import click
from click import Command, Group
from stactools.usfs_lcms import stac

logger = logging.getLogger(__name__)


def create_usfslcms_command(cli: Group) -> Command:
    """Creates the stactools-usfs-lcms command line utility."""

    @cli.group(
        "usfslcms",
        short_help=("Commands for working with stactools-usfs-lcms"),
    )
    def usfslcms() -> None:
        pass

    @usfslcms.command(
        "create-collection",
        short_help="Creates a STAC collection",
    )
    @click.argument("destination")
    def create_collection_command(destination: str) -> None:
        """Creates a STAC Collection

        Args:
            destination: An HREF for the Collection JSON
        """
        collection = stac.create_collection()
        collection.set_self_href(destination)
        collection.save_object()

    @usfslcms.command("create-item", short_help="Create a STAC item")
    @click.argument("source")
    @click.argument("destination")
    def create_item_command(source: str, destination: str) -> None:
        """Creates a STAC Item

        Args:
            source: HREF of the Asset associated with the Item
            destination: An HREF for the STAC Item
        """
        item = stac.create_item(source)
        item.save_object(dest_href=destination)

    return usfslcms
