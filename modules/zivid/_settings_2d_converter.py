"""Contains functions to convert between settings 2d and internal settings 2d."""
import _zivid
from zivid.settings_2d import Settings2D


import _zivid


def to_internal_settings_2d(settings2_d):
    internal_settings2_d = _zivid.Settings2D()

    def _to_internal_acquisition(acquisition):
        internal_acquisition = _zivid.Settings2D.Acquisition()

        if acquisition.aperture is not None:

            internal_acquisition.aperture = _zivid.Settings2D.Acquisition.Aperture(
                acquisition.aperture
            )
        else:
            internal_acquisition.aperture = _zivid.Settings2D.Acquisition.Aperture()
        if acquisition.brightness is not None:

            internal_acquisition.brightness = _zivid.Settings2D.Acquisition.Brightness(
                acquisition.brightness
            )
        else:
            internal_acquisition.brightness = _zivid.Settings2D.Acquisition.Brightness()
        if acquisition.exposure_time is not None:

            internal_acquisition.exposure_time = _zivid.Settings2D.Acquisition.ExposureTime(
                acquisition.exposure_time
            )
        else:
            internal_acquisition.exposure_time = (
                _zivid.Settings2D.Acquisition.ExposureTime()
            )
        if acquisition.gain is not None:

            internal_acquisition.gain = _zivid.Settings2D.Acquisition.Gain(
                acquisition.gain
            )
        else:
            internal_acquisition.gain = _zivid.Settings2D.Acquisition.Gain()
        pass  # no children
        return internal_acquisition

    def _to_internal_processing(processing):
        internal_processing = _zivid.Settings2D.Processing()

        def _to_internal_color(color):
            internal_color = _zivid.Settings2D.Processing.Color()

            def _to_internal_balance(balance):
                internal_balance = _zivid.Settings2D.Processing.Color.Balance()

                if balance.blue is not None:

                    internal_balance.blue = _zivid.Settings2D.Processing.Color.Balance.Blue(
                        balance.blue
                    )
                else:
                    internal_balance.blue = (
                        _zivid.Settings2D.Processing.Color.Balance.Blue()
                    )
                if balance.green is not None:

                    internal_balance.green = _zivid.Settings2D.Processing.Color.Balance.Green(
                        balance.green
                    )
                else:
                    internal_balance.green = (
                        _zivid.Settings2D.Processing.Color.Balance.Green()
                    )
                if balance.red is not None:

                    internal_balance.red = _zivid.Settings2D.Processing.Color.Balance.Red(
                        balance.red
                    )
                else:
                    internal_balance.red = (
                        _zivid.Settings2D.Processing.Color.Balance.Red()
                    )
                pass  # no children
                return internal_balance

            internal_color.balance = _to_internal_balance(color.balance)
            return internal_color

        internal_processing.color = _to_internal_color(processing.color)
        return internal_processing

    #if settings2_d.acquisitions is not None:
    #    internal_settings2_d.acquisitions = _zivid.Settings2D() # TODO
    #else:
    #    internal_settings2_d.acquisitions = _zivid.Settings2D().Acquisitions()

    if settings2_d.acquisitions is None:
        internal_settings2_d.acquisitions = _zivid.Settings().Acquisitions()  # TODO
    else:
        temp = _zivid.Settings2D().Acquisitions()
        for acq in settings2_d.acquisitions:
            temp.append(_to_internal_acquisition(acq))
        internal_settings2_d.acquisitions = temp

    internal_settings2_d.processing = _to_internal_processing(settings2_d.processing)
    return internal_settings2_d

def to_settings_2d(internal_settings_2d):
    """Convert internal settings 2d type to settings 2d.

    Args:
        internal_settings_2d: a internal settings 2d object

    Returns:
        a settings 2d object

    """

    return Settings2D(
        brightness=internal_settings_2d.brightness.value,
        exposure_time=internal_settings_2d.exposuretime.value,
        gain=internal_settings_2d.gain.value,
        iris=internal_settings_2d.iris.value,
    )
