"""dnd_town_builder_nautobot_plugin Plugin Initilization."""

from nautobot.extras.plugins import PluginConfig


class DndTownBuilderNautobotPluginConfig(PluginConfig):
    """Plugin configuration for the dnd_town_builder_nautobot_plugin plugin."""

    name = "dnd_town_builder_nautobot_plugin"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "dnd_town_builder_nautobot_plugin"  # Human-friendly name for the plugin.
    base_url = "dnd_town_builder_nautobot_plugin"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    default_settings = {}  # A dictionary of configuration parameters and their default values.
    caching_config = {}  # Plugin-specific cache configuration.


config = DndTownBuilderNautobotPluginConfig