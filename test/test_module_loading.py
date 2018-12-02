from module_discovery_utils.module_discovery_utils import load_all_modules_in_packages
from test import test_cases
from test.test_cases import plugin_discovery_instance, plugin_discovery_subclass


def test_list_wrapping():
    modules_list = load_all_modules_in_packages([test_cases])

    modules_single = load_all_modules_in_packages(test_cases)

    assert modules_list == modules_single


def test_load_multiple_modules():
    modules_multiple = load_all_modules_in_packages([plugin_discovery_instance, plugin_discovery_subclass])

    assert modules_multiple == [
        plugin_discovery_instance,
        plugin_discovery_subclass,
        plugin_discovery_instance.main,
        plugin_discovery_instance.plugins,
        plugin_discovery_instance.plugins.discovery_plugin,
        plugin_discovery_instance.plugins.dog_plugin,
        plugin_discovery_subclass.main,
        plugin_discovery_subclass.plugins,
        plugin_discovery_subclass.plugins.cat_plugin,
        plugin_discovery_subclass.plugins.subclass_plugin,
    ]
