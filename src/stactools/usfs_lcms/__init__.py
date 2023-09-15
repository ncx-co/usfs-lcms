import stactools.core
from stactools.cli.registry import Registry
from stactools.usfs_lcms.stac import create_collection, create_item

__all__ = ["create_collection", "create_item"]

stactools.core.use_fsspec()


def register_plugin(registry: Registry) -> None:
    from stactools.usfs_lcms import commands

    registry.register_subcommand(commands.create_usfslcms_command)
