from test.test_cases.plugin_discovery_instance.plugins.discovery_plugin import InstancePlugin


class DogPlugin(InstancePlugin):
    def __init__(self):
        super(DogPlugin, self).__init__("dog")


dog_plugin_instance = DogPlugin()
