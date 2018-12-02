from module_discovery_utils.module_discovery_utils import find_instances_in_packages
from test.test_cases import plugin_discovery_instance
from test.test_cases.plugin_discovery_instance.plugins.discovery_plugin import InstancePlugin
from test.test_cases.plugin_discovery_instance.plugins.dog_plugin import dog_plugin_instance


def test_discover_instances():
    plugins = find_instances_in_packages(plugin_discovery_instance, [InstancePlugin])

    assert plugins == [dog_plugin_instance]
