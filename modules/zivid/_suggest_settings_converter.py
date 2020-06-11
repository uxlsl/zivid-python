import _zivid


def to_internal_suggest_settings_parameters(suggest_settings_parameters):
    internal_suggest_settings_parameters = (
        _zivid.capture_assistant.SuggestSettingsParameters()
    )

    def _to_internal_ambient_light_frequency(ambient_light_frequency):
        # internal_ambient_light_frequency = (
        #    _zivid.capture_assistant.SuggestSettingsParameters.AmbientLightFrequency()
        # )
        #
        # pass  # no children
        # return internal_ambient_light_frequency
        print(ambient_light_frequency.value)
        print(ambient_light_frequency._value)
        return ambient_light_frequency._valid_values[ambient_light_frequency.value]

    if suggest_settings_parameters.max_capture_time is not None:

        internal_suggest_settings_parameters.max_capture_time = (
            _zivid.capture_assistant.SuggestSettingsParameters()
        )
    else:
        internal_suggest_settings_parameters.max_capture_time = (
            _zivid.capture_assistant.SuggestSettingsParameters()
        )

    internal_suggest_settings_parameters.ambient_light_frequency = _to_internal_ambient_light_frequency(
        suggest_settings_parameters.ambient_light_frequency
    )
    return internal_suggest_settings_parameters
