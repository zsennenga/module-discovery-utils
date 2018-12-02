from example import plugin_discovery_subclass
from example.plugin_discovery_subclass.plugins.subclass_plugin import SubclassPlugin
from module_discovery_utils.module_discovery_utils import find_subclasses_in_packages

if __name__ == '__main__':
    plugins = find_subclasses_in_packages(plugin_discovery_subclass, [SubclassPlugin])
