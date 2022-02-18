import stactools.core

from stactools.can_flood.stac import create_collection, create_item

__all__ = ['create_collection', 'create_item']

stactools.core.use_fsspec()


def register_plugin(registry):
    from stactools.can_flood import commands
    registry.register_subcommand(commands.create_canflood_command)


__version__ = "0.1.0"
