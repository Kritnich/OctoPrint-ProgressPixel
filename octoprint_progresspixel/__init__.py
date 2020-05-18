from __future__ import absolute_import
from subprocess import call
import octoprint.plugin
import os


class ProgressPixelPlugin(
    octoprint.plugin.ShutdownPlugin,
    octoprint.plugin.ProgressPlugin,
    octoprint.plugin.EventHandlerPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin
    ):

    SCRIPT = os.path.dirname(os.path.realpath(__file__)) + "/progresspixel.py "

    def set_neopixel(self, argument):
        cmd = "sudo python %s %s %s %s %s %s %s" % (
            self.SCRIPT,
            self._settings.get(["led_count"]),
            self._settings.get(["led_pin"]),
            self._settings.get(["led_brightness"]),
            argument,
            self._settings.get(["led_background_color"]).strip("#"),
            self._settings.get(["led_bar_color"]).strip("#")
        )
        self._logger.debug("Executing command: %s" % (cmd))
        call(cmd, shell=True)

    def get_settings_defaults(self):
        return dict(
            led_count=13,
            led_brightness=255,
            led_pin=18,
            led_background_color="#ffffff",
            led_bar_color="#0000ff"
        )

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/jscolor.js"]
        )

    def on_print_progress(self, storage, path, progress):
        self.set_neopixel(progress)

    def on_event(self, event, payload):
        # Shutting all LEDs down if a print ends for whatever reason
        if event in ("PrintFailed", "PrintDone", "PrintCancelled"):
            self._logger.debug("Clearing LEDs after event %s" % event)
            self.set_neopixel("clear")

    def on_shutdown(self):
        # Turn all LEDs off
        self._logger.debug("Clearing LEDs on shutdown")
        self.set_neopixel("clear")


__plugin_implementation__ = ProgressPixelPlugin()
__plugin_pythoncompat__ = ">=2.7,<4"
