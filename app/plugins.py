from click import Group
from litestar.plugins import CLIPluginProtocol

from app.commands import messages_group


class CLIPlugin(CLIPluginProtocol):
    def on_cli_init(self, cli: Group) -> None:
        cli.add_command(messages_group)
