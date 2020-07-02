# pylint: disable=import-outside-toplevel


def test_to_internal_suggest_settings_parameters_to_suggest_settings_parameters_modified():
    import datetime
    from zivid.capture_assistant import SuggestSettingsParameters
    from zivid._suggest_settings_parameters_converter import (
        to_suggest_settings_parameters,
        to_internal_suggest_settings_parameters,
    )

    modified_suggest_settings_parameters = SuggestSettingsParameters(model_name="hello")

    converted_suggest_settings_parameters = to_suggest_settings_parameters(
        to_internal_suggest_settings_parameters(modified_suggest_settings_parameters)
    )
    assert modified_suggest_settings_parameters == converted_suggest_settings_parameters
    assert isinstance(
        converted_suggest_settings_parameters, suggest_settings_parameters
    )
    assert isinstance(modified_suggest_settings_parameters, suggest_settings_parameters)


def test_to_internal_suggest_settings_parameters_to_suggest_settings_parameters_default():
    from zivid.capture_assistant import SuggestSettingsParameters
    from zivid._suggest_settings_parameters_converter import (
        to_suggest_settings_parameters,
        to_internal_suggest_settings_parameters,
    )

    default_suggest_settings_parameters = SuggestSettingsParameters()
    converted_suggest_settings_parameters = to_suggest_settings_parameters(
        to_internal_suggest_settings_parameters(default_suggest_settings_parameters)
    )
    assert default_suggest_settings_parameters == converted_suggest_settings_parameters
    assert isinstance(
        converted_suggest_settings_parameters, suggest_settings_parameters
    )
    assert isinstance(default_suggest_settings_parameters, suggest_settings_parameters)


#
