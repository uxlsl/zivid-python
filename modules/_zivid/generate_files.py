import _zivid.generate_settings
import _zivid.generate_settings_2d
import _zivid.generate_to_internal_settings_converter
import _zivid.generate_to_settings_converter


def generate():
    _zivid.generate_settings_2d._start_traverse()
    _zivid.generate_settings._start_traverse()
    _zivid.generate_to_internal_settings_converter.start_traverse()
    _zivid.generate_to_settings_converter.start_traverse()
