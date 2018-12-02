from example import self_registering_plugins
from example.self_registering_plugins.plugins.self_registering_plugin import SelfRegisteringPlugin
from module_discovery_utils.module_discovery_utils import load_all_modules_in_packages

if __name__ == '__main__':
    load_all_modules_in_packages(self_registering_plugins)

    plugins = SelfRegisteringPlugin.__subclasses__()
