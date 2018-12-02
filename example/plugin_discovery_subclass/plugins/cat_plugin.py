from example.plugin_discovery_subclass.plugins.subclass_plugin import SubclassPlugin


class CatPlugin(SubclassPlugin):
    def __init__(self):
        super(CatPlugin, self).__init__("cat")
