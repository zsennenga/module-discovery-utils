from test.test_cases import plugin_discovery_instance
from test.test_cases.plugin_discovery_instance.plugins.discovery_plugin import InstancePlugin
from module_discovery_utils.module_discovery_utils import find_instances_in_packages

if __name__ == '__main__':
    plugins = find_instances_in_packages(plugin_discovery_instance, [InstancePlugin])
