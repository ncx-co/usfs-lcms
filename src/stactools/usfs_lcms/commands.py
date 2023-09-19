import logging
import os
import pathlib
from typing import List

import click
from click import Command, Group, Path
from stactools.usda_cdl import tile
from stactools.usfs_lcms import stac
from stactools.usfs_lcms.download import download_zips

logger = logging.getLogger(__name__)


def create_usfslcms_command(cli: Group) -> Command:
    """Creates the stactools-usfs-lcms command line utility."""

    @cli.group(
        "usfs-lcms",
        short_help=("Commands for working with stactools-usfs-lcms"),
    )
    def usfs_lcms() -> None:
        pass

    @usfs_lcms.command(
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

    @usfs_lcms.command("create-item", short_help="Create a STAC item")
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

    @usfs_lcms.command("tile", short_help="Tile a geotiff (zipped or not zipped)")
    @click.argument("infile")
    @click.argument("destination")
    @click.option(
        "-s",
        "--size",
        help="Size, in pixels, of each tile",
        default=tile.DEFAULT_WINDOW_SIZE,
        show_default=True,
    )
    def tile_file(infile: Path, destination: Path, size: int) -> None:
        """Tiles the input file, placing the tiles in the destination directory."""
        os.makedirs(str(destination), exist_ok=True)
        infile_as_path = pathlib.Path(str(infile))
        if infile_as_path.suffix == ".zip":
            tile.tile_zipfile(infile_as_path, pathlib.Path(str(destination)), size)
        else:
            tile.tile_geotiff(infile_as_path, pathlib.Path(str(destination)), size)

    @usfs_lcms.command("download", short_help="Download zipped source GeoTIFFs")
    @click.argument("years", nargs=-1, type=int)
    @click.argument("regions", nargs=-1, type=str)
    @click.argument("destination", nargs=1)
    def download(years: List[int], regions: List[str], destination: Path) -> None:
        """Downloads the USFS LCMS zip files to the destination directory. It's a
        lot of data, so this will take a while.

        If you just want to download specific years' data, provide those years
        on the command line before the destination directory.
        """
        download_zips(years, regions, pathlib.Path(str(destination)))

    return usfs_lcms
