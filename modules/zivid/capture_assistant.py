"""Contains capture assistant functions and classes."""
import _zivid
import zivid._settings_converter as _settings_converter
from zivid._make_enum_wrapper import _make_enum_wrapper


class SuggestSettingsParameters:
    class AmbientLightFrequency:
        hz50 = "hz50" # class
        hz60 = "hz60"
        none = "none"

        _valid_values = {"hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50,
        "hz60" :_zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz60,
        "none" :_zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.none,}
        #hz50 = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50
        #)
        #hz60 = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz60
        #)
        #none = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.none
        #)
        @property
        def valid_values():
            return [hz50, hz60, none]#[to_ambient_light_frequency(value) for value in _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency().valid_values()]


        # @property.setter
        # def hz50(self,value):
        #     if in dict("hz50": _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50):
        #        self._value = _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency.enum.hz50
        #     else:
        #         raise ValueError(f"{value} is not in {self.valid_values()}")
        #         #raise sosdmksm

        


        def __init__(self, value=none):
            self._value = value

        def __eq__(self, other):
            if self._value == other._value:
                return True
            return False

        def __str__(self):
            return """AmbientLightFrequency: {value}""".format(value=self._value.name)

    def __init__(
        self,
        max_capture_time=_zivid.capture_assistant.SuggestSettingsParameters()
        .MaxCaptureTime()
        .value,
        ambient_light_frequency=AmbientLightFrequency(),
    ):

        if max_capture_time is not None:
            self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
                max_capture_time
            )
        else:
            self._max_capture_time = (
                _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime()
            )
        self.ambient_light_frequency = ambient_light_frequency

    @property
    def max_capture_time(self):
        return self._max_capture_time.value

    @max_capture_time.setter
    def max_capture_time(self, value):
        self._max_capture_time = _zivid.capture_assistant.SuggestSettingsParameters.MaxCaptureTime(
            value
        )

    def __eq__(self, other):
        if (
            self._max_capture_time == other._max_capture_time
            and self.ambient_light_frequency == other.ambient_light_frequency
        ):
            return True
        return False

    def __str__(self):
        return """SuggestSettingsParameters:
    max_capture_time: {max_capture_time}
    ambient_light_frequency: {ambient_light_frequency}
    """.format(
            max_capture_time=self.max_capture_time,
            ambient_light_frequency=self.ambient_light_frequency,
        )


# class SuggestSettingsParameters:  # pylint: disable=too-few-public-methods
#     AmbientLightFrequency = _make_enum_wrapper(
#         _zivid.capture_assistant.SuggestSettingsParameters().AmbientLightFrequency(),
#         "Ensure compatibility with the frequency of the ambient light in the scene.",
#     )
#     """Input to the Capture Assistant algorithm.
#
#     Used to specify a constraint on the total capture time for the settings suggested by the Capture Assistant,
#     and optionally specify the ambient light frequency.
#     The capture time constraint assumes a computer meeting Zivid's recommended minimum compute power.
#
#     """
#
#     def __init__(self, max_capture_time, ambient_light_frequency=None):
#         """Initialize SuggestSettingsParameters.
#
#         Args:
#             max_capture_time: an instance of datetime.timedelta
#             ambient_light_frequency: a member of the enum zivid.capture_assistant.AmbientLightFrequency
#
#         """
#         if ambient_light_frequency is None:
#             self.__impl = _zivid.capture_assistant.SuggestSettingsParameters(
#                 max_capture_time
#             )
#         else:
#             self.__impl = _zivid.capture_assistant.SuggestSettingsParameters(
#                 max_capture_time,
#                 ambient_light_frequency._to_internal(),  # pylint: disable=protected-access
#             )
#
#     @property
#     def max_capture_time(self):
#         """Get max capture time.
#
#         Returns:
#             Instance of datetime.timedelta
#
#         """
#         return self.__impl.maxCaptureTime()
#
#     @property
#     def ambient_light_frequency(self):
#         """Get ambient light frequency.
#
#         Returns:
#             Instance of AmbientLightFrequency
#
#         """
#         return AmbientLightFrequency(self.__impl.ambientLightFrequency().name)
#
#     def __str__(self):
#         return self.__impl.to_string()


def suggest_settings(camera, suggest_settings_parameters):
    """Find settings for the current scene based on the suggest_settings_parameters.

    The suggested settings returned from this function should be passed into hdr.capture to perform the actual capture.

    Args:
        camera: an instance of zivid.Camera
        suggest_settings_parameters: an instance of zivid.capture_assistant.SuggestSettingsParameters which provides
                                     parameters (e.g., max capture time constraint) to the suggest_settings algorithm.

    Returns:
        List of Settings.

    """
    internal_settings = _zivid.capture_assistant.suggest_settings(
        camera._Camera__impl,  # pylint: disable=protected-access
        suggest_settings_parameters._SuggestSettingsParameters__impl,  # pylint: disable=protected-access
    )
    return [_settings_converter.to_settings(internal) for internal in internal_settings]
