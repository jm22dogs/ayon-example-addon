import os

from openpype.modules import AYONAddon, ITrayModule, IPluginPaths

from qtpy import QtWidgets


class ExampleTrayWrapper:

    def __init__(self, module): ...

    def tray_menu(self, tray_menu):
        custom_menu = QtWidgets.QMenu("Custom Menu", tray_menu)
        custom_menu.addAction("Custom Action")
        custom_menu.addSeparator()
        custom_menu.addAction("Another Custom Action")
        tray_menu.addMenu(custom_menu)


class TrayMenuExample(AYONAddon, ITrayModule, IPluginPaths):
    name = "TrayMenuExample"
    enabled = True
    tray_wrapper = None

    def initialize(self, modules_settings):
        module_settings = modules_settings.get(self.name, dict())

    def tray_init(self):
        self.tray_wrapper = ExampleTrayWrapper(self)

    def tray_start(self):
        # Tray startup logic, here you can do things like logins
        ...

    def tray_exit(self, *args, **kwargs):
        return self.tray_wrapper

    def tray_menu(self, tray_menu):
        return self.tray_wrapper.tray_menu(tray_menu)

    def get_plugin_paths(self):
        # This method must exists, otherwise Ayon Launcher won't initialize it
        return dict()
