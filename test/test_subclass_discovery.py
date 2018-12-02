from module_discovery_utils.module_discovery_utils import find_subclasses_in_packages
from test.test_cases import plugin_discovery_subclass
from test.test_cases.plugin_discovery_subclass.plugins.cat_plugin import CatPlugin
from test.test_cases.plugin_discovery_subclass.plugins.subclass_plugin import SubclassPlugin


def test_subclass_discovery():
    plugins = find_subclasses_in_packages(plugin_discovery_subclass, [SubclassPlugin])

    assert plugins == [CatPlugin]
