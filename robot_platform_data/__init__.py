"""robot_platform_data Plugin Initilization."""

from nautobot.extras.plugins import PluginConfig

# Import version data from the setup.py file used to build this plugin
try:
    from importlib import metadata
except ImportError: 
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)


class RobotPlatformDataConfig(PluginConfig):
    """Plugin configuration for the robot_platform_data plugin."""

    name = "robot_platform_data"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "Robot Platform Data"  # Human-friendly name for the plugin.
    base_url = "robot_platform_data"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    default_settings = {}  # A dictionary of configuration parameters and their default values.
    caching_config = {}  # Plugin-specific cache configuration.
    version = __version__
    author = "Daniel Himes"
    description = "NIDM plugin to manage robot platform data"


config = RobotPlatformDataConfig