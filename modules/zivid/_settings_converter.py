"""Contains functions to convert between settings and internal settings."""
import _zivid
from zivid.settings import Settings


def to_settings(internal_settings):
    """Convert internal settings type to settings.

    Args:
        internal_settings: a internal settings object

    Returns:
        a settings object

    """

    def to_filters(internal_filters):
        def to_contrast(internal_contrast):
            return Settings.Filters.Contrast(
                enabled=internal_contrast.enabled.value,
                threshold=internal_contrast.threshold.value,
            )

        def to_outlier(internal_outlier):
            return Settings.Filters.Outlier(
                enabled=internal_outlier.enabled.value,
                threshold=internal_outlier.threshold.value,
            )

        def to_saturated(internal_saturated):
            return Settings.Filters.Saturated(enabled=internal_saturated.enabled.value)

        def to_reflection(internal_reflection):
            return Settings.Filters.Reflection(
                enabled=internal_reflection.enabled.value
            )

        def to_gaussian(internal_gaussian):
            return Settings.Filters.Gaussian(
                enabled=internal_gaussian.enabled.value,
                sigma=internal_gaussian.sigma.value,
            )

        return Settings.Filters(
            contrast=to_contrast(internal_filters.contrast),
            outlier=to_outlier(internal_filters.outlier),
            saturated=to_saturated(internal_filters.saturated),
            reflection=to_reflection(internal_filters.reflection),
            gaussian=to_gaussian(internal_filters.gaussian),
        )

    return Settings(
        bidirectional=internal_settings.bidirectional.value,
        blue_balance=internal_settings.bluebalance.value,
        brightness=internal_settings.brightness.value,
        exposure_time=internal_settings.exposuretime.value,
        filters=to_filters(internal_settings.filters),
        gain=internal_settings.gain.value,
        iris=internal_settings.iris.value,
        red_balance=internal_settings.redbalance.value,
    )


import _zivid


def to_internal_settings(settings):
    internal_settings = _zivid.Settings()

    def _to_internal_frames(frames):
        internal_frames = _zivid.Settings.Frames()

        def _to_internal_frame(frame):
            internal_frame = _zivid.Settings.Frames.Frame()

            if frame.aperture is not None:

                internal_frame.aperture = _zivid.Settings.Frames.Frame.Aperture(frame.aperture)
            else:
                internal_frame.aperture = _zivid.Settings.Frames.Frame.Aperture()
            if frame.bidirectional is not None:

                internal_frame.bidirectional = _zivid.Settings.Frames.Frame.Bidirectional(
                    frame.bidirectional
                )
            else:
                internal_frame.bidirectional = _zivid.Settings.Frames.Frame.Bidirectional()
            if frame.brightness is not None:

                internal_frame.brightness = _zivid.Settings.Frames.Frame.Brightness(
                    frame.brightness
                )
            else:
                internal_frame.brightness = _zivid.Settings.Frames.Frame.Brightness()
            if frame.exposure_time is not None:

                internal_frame.exposure_time = _zivid.Settings.Frames.Frame.ExposureTime(
                    frame.exposure_time
                )
            else:
                internal_frame.exposure_time = _zivid.Settings.Frames.Frame.ExposureTime()
            if frame.gain is not None:

                internal_frame.gain = _zivid.Settings.Frames.Frame.Gain(frame.gain)
            else:
                internal_frame.gain = _zivid.Settings.Frames.Frame.Gain()
            pass  # no children
            return internal_frame

        internal_frames.frame = _to_internal_frame(frames.frame)
        return internal_frames

    def _to_internal_processing(processing):
        internal_processing = _zivid.Settings.Processing()

        def _to_internal_color(color):
            internal_color = _zivid.Settings.Processing.Color()

            def _to_internal_balance(balance):
                internal_balance = _zivid.Settings.Processing.Color.Balance()

                if balance.blue is not None:

                    internal_balance.blue = _zivid.Settings.Processing.Color.Balance.Blue(
                        balance.blue
                    )
                else:
                    internal_balance.blue = (
                        _zivid.Settings.Processing.Color.Balance.Blue()
                    )
                if balance.green is not None:

                    internal_balance.green = _zivid.Settings.Processing.Color.Balance.Green(
                        balance.green
                    )
                else:
                    internal_balance.green = (
                        _zivid.Settings.Processing.Color.Balance.Green()
                    )
                if balance.red is not None:

                    internal_balance.red = _zivid.Settings.Processing.Color.Balance.Red(
                        balance.red
                    )
                else:
                    internal_balance.red = (
                        _zivid.Settings.Processing.Color.Balance.Red()
                    )
                pass  # no children
                return internal_balance

            internal_color.balance = _to_internal_balance(color.balance)
            return internal_color

        def _to_internal_filters(filters):
            internal_filters = _zivid.Settings.Processing.Filters()

            def _to_internal_contrast(contrast):
                internal_contrast = _zivid.Settings.Processing.Filters.Contrast()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Contrast.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Contrast.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Contrast.Removal.Enabled()
                        )
                    if removal.threshold is not None:

                        internal_removal.threshold = _zivid.Settings.Processing.Filters.Contrast.Removal.Threshold(
                            removal.threshold
                        )
                    else:
                        internal_removal.threshold = (
                            _zivid.Settings.Processing.Filters.Contrast.Removal.Threshold()
                        )
                    pass  # no children
                    return internal_removal

                internal_contrast.removal = _to_internal_removal(contrast.removal)
                return internal_contrast

            def _to_internal_experimental(experimental):
                internal_experimental = (
                    _zivid.Settings.Processing.Filters.Experimental()
                )

                def _to_internal_contrast_distortion(contrast_distortion):
                    internal_contrast_distortion = (
                        _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion()
                    )

                    def _to_internal_correction(correction):
                        internal_correction = (
                            _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction()
                        )

                        if correction.enabled is not None:

                            internal_correction.enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled(
                                correction.enabled
                            )
                        else:
                            internal_correction.enabled = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled()
                            )
                        if correction.strength is not None:

                            internal_correction.strength = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength(
                                correction.strength
                            )
                        else:
                            internal_correction.strength = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength()
                            )
                        pass  # no children
                        return internal_correction

                    def _to_internal_removal(removal):
                        internal_removal = (
                            _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal()
                        )

                        if removal.enabled is not None:

                            internal_removal.enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled(
                                removal.enabled
                            )
                        else:
                            internal_removal.enabled = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled()
                            )
                        if removal.threshold is not None:

                            internal_removal.threshold = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold(
                                removal.threshold
                            )
                        else:
                            internal_removal.threshold = (
                                _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold()
                            )
                        pass  # no children
                        return internal_removal

                    internal_contrast_distortion.correction = _to_internal_correction(
                        contrast_distortion.correction
                    )
                    internal_contrast_distortion.removal = _to_internal_removal(
                        contrast_distortion.removal
                    )
                    return internal_contrast_distortion

                internal_experimental.contrast_distortion = _to_internal_contrast_distortion(
                    experimental.contrast_distortion
                )
                return internal_experimental

            def _to_internal_outlier(outlier):
                internal_outlier = _zivid.Settings.Processing.Filters.Outlier()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Outlier.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled()
                        )
                    if removal.threshold is not None:

                        internal_removal.threshold = _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold(
                            removal.threshold
                        )
                    else:
                        internal_removal.threshold = (
                            _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold()
                        )
                    pass  # no children
                    return internal_removal

                internal_outlier.removal = _to_internal_removal(outlier.removal)
                return internal_outlier

            def _to_internal_reflection(reflection):
                internal_reflection = _zivid.Settings.Processing.Filters.Reflection()

                def _to_internal_removal(removal):
                    internal_removal = (
                        _zivid.Settings.Processing.Filters.Reflection.Removal()
                    )

                    if removal.enabled is not None:

                        internal_removal.enabled = _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled(
                            removal.enabled
                        )
                    else:
                        internal_removal.enabled = (
                            _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled()
                        )
                    pass  # no children
                    return internal_removal

                internal_reflection.removal = _to_internal_removal(reflection.removal)
                return internal_reflection

            def _to_internal_smoothing(smoothing):
                internal_smoothing = _zivid.Settings.Processing.Filters.Smoothing()

                def _to_internal_gaussian(gaussian):
                    internal_gaussian = (
                        _zivid.Settings.Processing.Filters.Smoothing.Gaussian()
                    )

                    if gaussian.enabled is not None:

                        internal_gaussian.enabled = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled(
                            gaussian.enabled
                        )
                    else:
                        internal_gaussian.enabled = (
                            _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled()
                        )
                    if gaussian.sigma is not None:

                        internal_gaussian.sigma = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma(
                            gaussian.sigma
                        )
                    else:
                        internal_gaussian.sigma = (
                            _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma()
                        )
                    pass  # no children
                    return internal_gaussian

                internal_smoothing.gaussian = _to_internal_gaussian(smoothing.gaussian)
                return internal_smoothing

            internal_filters.contrast = _to_internal_contrast(filters.contrast)
            internal_filters.experimental = _to_internal_experimental(
                filters.experimental
            )
            internal_filters.outlier = _to_internal_outlier(filters.outlier)
            internal_filters.reflection = _to_internal_reflection(filters.reflection)
            internal_filters.smoothing = _to_internal_smoothing(filters.smoothing)
            return internal_filters

        internal_processing.color = _to_internal_color(processing.color)
        internal_processing.filters = _to_internal_filters(processing.filters)
        return internal_processing

    internal_settings.frames = _to_internal_frames(settings.frames)
    internal_settings.processing = _to_internal_processing(settings.processing)
    return internal_settings
