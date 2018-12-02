from example.self_registering_plugins.plugins.self_registering_plugin import SelfRegisteringPlugin


class RockPlugin(SelfRegisteringPlugin):
    def __init__(self):
        super(RockPlugin, self).__init__("beryl")
