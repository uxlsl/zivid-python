from typing import Type
import _zivid
from zivid._settings_converter import to_internal_settings


class Settings:
    class Acquisition:
        class Patterns:
            class Sine:
                def __init__(
                    self,
                    bidirectional=_zivid.Settings()
                    .Acquisition.Patterns.Sine()
                    .Bidirectional()
                    .value,
                ):

                    if bidirectional is not None:
                        self._bidirectional = _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional(
                            bidirectional
                        )
                    else:
                        self._bidirectional = (
                            _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional()
                        )

                @property
                def bidirectional(self):
                    return self._bidirectional.value

                @bidirectional.setter
                def bidirectional(self, value):
                    self._bidirectional = _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional(
                        value
                    )

                def __eq__(self, other):
                    if self._bidirectional == other._bidirectional:
                        return True
                    return False

                def __str__(self):
                    return """Sine:
                bidirectional: {bidirectional}
                """.format(
                        bidirectional=self.bidirectional,
                    )

            def __init__(
                self, sine=Sine(),
            ):

                self.sine = sine

            def __eq__(self, other):
                if self.sine == other.sine:
                    return True
                return False

            def __str__(self):
                return """Patterns:
            sine: {sine}
            """.format(
                    sine=self.sine,
                )

        def __init__(
            self,
            aperture=_zivid.Settings().Acquisition().Aperture().value,
            brightness=_zivid.Settings().Acquisition().Brightness().value,
            exposure_time=_zivid.Settings().Acquisition().ExposureTime().value,
            gain=_zivid.Settings().Acquisition().Gain().value,
            patterns=Patterns(),
        ):

            if aperture is not None:
                self._aperture = _zivid.Settings.Acquisition.Aperture(aperture)
            else:
                self._aperture = _zivid.Settings.Acquisition.Aperture()
            if brightness is not None:
                self._brightness = _zivid.Settings.Acquisition.Brightness(brightness)
            else:
                self._brightness = _zivid.Settings.Acquisition.Brightness()
            if exposure_time is not None:
                self._exposure_time = _zivid.Settings.Acquisition.ExposureTime(
                    exposure_time
                )
            else:
                self._exposure_time = _zivid.Settings.Acquisition.ExposureTime()
            if gain is not None:
                self._gain = _zivid.Settings.Acquisition.Gain(gain)
            else:
                self._gain = _zivid.Settings.Acquisition.Gain()
            self.patterns = patterns

        @property
        def aperture(self):
            return self._aperture.value

        @property
        def brightness(self):
            return self._brightness.value

        @property
        def exposure_time(self):
            return self._exposure_time.value

        @property
        def gain(self):
            return self._gain.value

        @aperture.setter
        def aperture(self, value):
            self._aperture = _zivid.Settings.Acquisition.Aperture(value)

        @brightness.setter
        def brightness(self, value):
            self._brightness = _zivid.Settings.Acquisition.Brightness(value)

        @exposure_time.setter
        def exposure_time(self, value):
            self._exposure_time = _zivid.Settings.Acquisition.ExposureTime(value)

        @gain.setter
        def gain(self, value):
            self._gain = _zivid.Settings.Acquisition.Gain(value)

        def __eq__(self, other):
            if (
                self._aperture == other._aperture
                and self._brightness == other._brightness
                and self._exposure_time == other._exposure_time
                and self._gain == other._gain
                and self.patterns == other.patterns
            ):
                return True
            return False

        def __str__(self):
            return """Acquisition:
        aperture: {aperture}
        brightness: {brightness}
        exposure_time: {exposure_time}
        gain: {gain}
        patterns: {patterns}
        """.format(
                aperture=self.aperture,
                brightness=self.brightness,
                exposure_time=self.exposure_time,
                gain=self.gain,
                patterns=self.patterns,
            )

    class Processing:
        class Color:
            class Balance:
                def __init__(
                    self,
                    blue=_zivid.Settings().Processing.Color.Balance().Blue().value,
                    green=_zivid.Settings().Processing.Color.Balance().Green().value,
                    red=_zivid.Settings().Processing.Color.Balance().Red().value,
                ):

                    if blue is not None:
                        self._blue = _zivid.Settings.Processing.Color.Balance.Blue(blue)
                    else:
                        self._blue = _zivid.Settings.Processing.Color.Balance.Blue()
                    if green is not None:
                        self._green = _zivid.Settings.Processing.Color.Balance.Green(
                            green
                        )
                    else:
                        self._green = _zivid.Settings.Processing.Color.Balance.Green()
                    if red is not None:
                        self._red = _zivid.Settings.Processing.Color.Balance.Red(red)
                    else:
                        self._red = _zivid.Settings.Processing.Color.Balance.Red()

                @property
                def blue(self):
                    return self._blue.value

                @property
                def green(self):
                    return self._green.value

                @property
                def red(self):
                    return self._red.value

                @blue.setter
                def blue(self, value):
                    self._blue = _zivid.Settings.Processing.Color.Balance.Blue(value)

                @green.setter
                def green(self, value):
                    self._green = _zivid.Settings.Processing.Color.Balance.Green(value)

                @red.setter
                def red(self, value):
                    self._red = _zivid.Settings.Processing.Color.Balance.Red(value)

                def __eq__(self, other):
                    if (
                        self._blue == other._blue
                        and self._green == other._green
                        and self._red == other._red
                    ):
                        return True
                    return False

                def __str__(self):
                    return """Balance:
                blue: {blue}
                green: {green}
                red: {red}
                """.format(
                        blue=self.blue, green=self.green, red=self.red,
                    )

            def __init__(
                self, balance=Balance(),
            ):

                self.balance = balance

            def __eq__(self, other):
                if self.balance == other.balance:
                    return True
                return False

            def __str__(self):
                return """Color:
            balance: {balance}
            """.format(
                    balance=self.balance,
                )

        class Filters:
            class Experimental:
                class ContrastDistortion:
                    class Correction:
                        def __init__(
                            self,
                            enabled=_zivid.Settings()
                            .Processing.Filters.Experimental.ContrastDistortion.Correction()
                            .Enabled()
                            .value,
                            strength=_zivid.Settings()
                            .Processing.Filters.Experimental.ContrastDistortion.Correction()
                            .Strength()
                            .value,
                        ):

                            if enabled is not None:
                                self._enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled(
                                    enabled
                                )
                            else:
                                self._enabled = (
                                    _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled()
                                )
                            if strength is not None:
                                self._strength = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength(
                                    strength
                                )
                            else:
                                self._strength = (
                                    _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength()
                                )

                        @property
                        def enabled(self):
                            return self._enabled.value

                        @property
                        def strength(self):
                            return self._strength.value

                        @enabled.setter
                        def enabled(self, value):
                            self._enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Enabled(
                                value
                            )

                        @strength.setter
                        def strength(self, value):
                            self._strength = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Correction.Strength(
                                value
                            )

                        def __eq__(self, other):
                            if (
                                self._enabled == other._enabled
                                and self._strength == other._strength
                            ):
                                return True
                            return False

                        def __str__(self):
                            return """Correction:
                        enabled: {enabled}
                        strength: {strength}
                        """.format(
                                enabled=self.enabled, strength=self.strength,
                            )

                    class Removal:
                        def __init__(
                            self,
                            enabled=_zivid.Settings()
                            .Processing.Filters.Experimental.ContrastDistortion.Removal()
                            .Enabled()
                            .value,
                            threshold=_zivid.Settings()
                            .Processing.Filters.Experimental.ContrastDistortion.Removal()
                            .Threshold()
                            .value,
                        ):

                            if enabled is not None:
                                self._enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled(
                                    enabled
                                )
                            else:
                                self._enabled = (
                                    _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled()
                                )
                            if threshold is not None:
                                self._threshold = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold(
                                    threshold
                                )
                            else:
                                self._threshold = (
                                    _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold()
                                )

                        @property
                        def enabled(self):
                            return self._enabled.value

                        @property
                        def threshold(self):
                            return self._threshold.value

                        @enabled.setter
                        def enabled(self, value):
                            self._enabled = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Enabled(
                                value
                            )

                        @threshold.setter
                        def threshold(self, value):
                            self._threshold = _zivid.Settings.Processing.Filters.Experimental.ContrastDistortion.Removal.Threshold(
                                value
                            )

                        def __eq__(self, other):
                            if (
                                self._enabled == other._enabled
                                and self._threshold == other._threshold
                            ):
                                return True
                            return False

                        def __str__(self):
                            return """Removal:
                        enabled: {enabled}
                        threshold: {threshold}
                        """.format(
                                enabled=self.enabled, threshold=self.threshold,
                            )

                    def __init__(
                        self, correction=Correction(), removal=Removal(),
                    ):

                        self.correction = correction
                        self.removal = removal

                    def __eq__(self, other):
                        if (
                            self.correction == other.correction
                            and self.removal == other.removal
                        ):
                            return True
                        return False

                    def __str__(self):
                        return """ContrastDistortion:
                    correction: {correction}
                    removal: {removal}
                    """.format(
                            correction=self.correction, removal=self.removal,
                        )

                def __init__(
                    self, contrast_distortion=ContrastDistortion(),
                ):

                    self.contrast_distortion = contrast_distortion

                def __eq__(self, other):
                    if self.contrast_distortion == other.contrast_distortion:
                        return True
                    return False

                def __str__(self):
                    return """Experimental:
                contrast_distortion: {contrast_distortion}
                """.format(
                        contrast_distortion=self.contrast_distortion,
                    )

            class Noise:
                class Removal:
                    def __init__(
                        self,
                        enabled=_zivid.Settings()
                        .Processing.Filters.Noise.Removal()
                        .Enabled()
                        .value,
                        threshold=_zivid.Settings()
                        .Processing.Filters.Noise.Removal()
                        .Threshold()
                        .value,
                    ):

                        if enabled is not None:
                            self._enabled = _zivid.Settings.Processing.Filters.Noise.Removal.Enabled(
                                enabled
                            )
                        else:
                            self._enabled = (
                                _zivid.Settings.Processing.Filters.Noise.Removal.Enabled()
                            )
                        if threshold is not None:
                            self._threshold = _zivid.Settings.Processing.Filters.Noise.Removal.Threshold(
                                threshold
                            )
                        else:
                            self._threshold = (
                                _zivid.Settings.Processing.Filters.Noise.Removal.Threshold()
                            )

                    @property
                    def enabled(self):
                        return self._enabled.value

                    @property
                    def threshold(self):
                        return self._threshold.value

                    @enabled.setter
                    def enabled(self, value):
                        self._enabled = _zivid.Settings.Processing.Filters.Noise.Removal.Enabled(
                            value
                        )

                    @threshold.setter
                    def threshold(self, value):
                        self._threshold = _zivid.Settings.Processing.Filters.Noise.Removal.Threshold(
                            value
                        )

                    def __eq__(self, other):
                        if (
                            self._enabled == other._enabled
                            and self._threshold == other._threshold
                        ):
                            return True
                        return False

                    def __str__(self):
                        return """Removal:
                    enabled: {enabled}
                    threshold: {threshold}
                    """.format(
                            enabled=self.enabled, threshold=self.threshold,
                        )

                def __init__(
                    self, removal=Removal(),
                ):

                    self.removal = removal

                def __eq__(self, other):
                    if self.removal == other.removal:
                        return True
                    return False

                def __str__(self):
                    return """Noise:
                removal: {removal}
                """.format(
                        removal=self.removal,
                    )

            class Outlier:
                class Removal:
                    def __init__(
                        self,
                        enabled=_zivid.Settings()
                        .Processing.Filters.Outlier.Removal()
                        .Enabled()
                        .value,
                        threshold=_zivid.Settings()
                        .Processing.Filters.Outlier.Removal()
                        .Threshold()
                        .value,
                    ):

                        if enabled is not None:
                            self._enabled = _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled(
                                enabled
                            )
                        else:
                            self._enabled = (
                                _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled()
                            )
                        if threshold is not None:
                            self._threshold = _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold(
                                threshold
                            )
                        else:
                            self._threshold = (
                                _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold()
                            )

                    @property
                    def enabled(self):
                        return self._enabled.value

                    @property
                    def threshold(self):
                        return self._threshold.value

                    @enabled.setter
                    def enabled(self, value):
                        self._enabled = _zivid.Settings.Processing.Filters.Outlier.Removal.Enabled(
                            value
                        )

                    @threshold.setter
                    def threshold(self, value):
                        self._threshold = _zivid.Settings.Processing.Filters.Outlier.Removal.Threshold(
                            value
                        )

                    def __eq__(self, other):
                        if (
                            self._enabled == other._enabled
                            and self._threshold == other._threshold
                        ):
                            return True
                        return False

                    def __str__(self):
                        return """Removal:
                    enabled: {enabled}
                    threshold: {threshold}
                    """.format(
                            enabled=self.enabled, threshold=self.threshold,
                        )

                def __init__(
                    self, removal=Removal(),
                ):

                    self.removal = removal

                def __eq__(self, other):
                    if self.removal == other.removal:
                        return True
                    return False

                def __str__(self):
                    return """Outlier:
                removal: {removal}
                """.format(
                        removal=self.removal,
                    )

            class Reflection:
                class Removal:
                    def __init__(
                        self,
                        enabled=_zivid.Settings()
                        .Processing.Filters.Reflection.Removal()
                        .Enabled()
                        .value,
                    ):

                        if enabled is not None:
                            self._enabled = _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled(
                                enabled
                            )
                        else:
                            self._enabled = (
                                _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled()
                            )

                    @property
                    def enabled(self):
                        return self._enabled.value

                    @enabled.setter
                    def enabled(self, value):
                        self._enabled = _zivid.Settings.Processing.Filters.Reflection.Removal.Enabled(
                            value
                        )

                    def __eq__(self, other):
                        if self._enabled == other._enabled:
                            return True
                        return False

                    def __str__(self):
                        return """Removal:
                    enabled: {enabled}
                    """.format(
                            enabled=self.enabled,
                        )

                def __init__(
                    self, removal=Removal(),
                ):

                    self.removal = removal

                def __eq__(self, other):
                    if self.removal == other.removal:
                        return True
                    return False

                def __str__(self):
                    return """Reflection:
                removal: {removal}
                """.format(
                        removal=self.removal,
                    )

            class Smoothing:
                class Gaussian:
                    def __init__(
                        self,
                        enabled=_zivid.Settings()
                        .Processing.Filters.Smoothing.Gaussian()
                        .Enabled()
                        .value,
                        sigma=_zivid.Settings()
                        .Processing.Filters.Smoothing.Gaussian()
                        .Sigma()
                        .value,
                    ):

                        if enabled is not None:
                            self._enabled = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled(
                                enabled
                            )
                        else:
                            self._enabled = (
                                _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled()
                            )
                        if sigma is not None:
                            self._sigma = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma(
                                sigma
                            )
                        else:
                            self._sigma = (
                                _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma()
                            )

                    @property
                    def enabled(self):
                        return self._enabled.value

                    @property
                    def sigma(self):
                        return self._sigma.value

                    @enabled.setter
                    def enabled(self, value):
                        self._enabled = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Enabled(
                            value
                        )

                    @sigma.setter
                    def sigma(self, value):
                        self._sigma = _zivid.Settings.Processing.Filters.Smoothing.Gaussian.Sigma(
                            value
                        )

                    def __eq__(self, other):
                        if (
                            self._enabled == other._enabled
                            and self._sigma == other._sigma
                        ):
                            return True
                        return False

                    def __str__(self):
                        return """Gaussian:
                    enabled: {enabled}
                    sigma: {sigma}
                    """.format(
                            enabled=self.enabled, sigma=self.sigma,
                        )

                def __init__(
                    self, gaussian=Gaussian(),
                ):

                    self.gaussian = gaussian

                def __eq__(self, other):
                    if self.gaussian == other.gaussian:
                        return True
                    return False

                def __str__(self):
                    return """Smoothing:
                gaussian: {gaussian}
                """.format(
                        gaussian=self.gaussian,
                    )

            def __init__(
                self,
                experimental=Experimental(),
                noise=Noise(),
                outlier=Outlier(),
                reflection=Reflection(),
                smoothing=Smoothing(),
            ):

                self.experimental = experimental
                self.noise = noise
                self.outlier = outlier
                self.reflection = reflection
                self.smoothing = smoothing

            def __eq__(self, other):
                if (
                    self.experimental == other.experimental
                    and self.noise == other.noise
                    and self.outlier == other.outlier
                    and self.reflection == other.reflection
                    and self.smoothing == other.smoothing
                ):
                    return True
                return False

            def __str__(self):
                return """Filters:
            experimental: {experimental}
            noise: {noise}
            outlier: {outlier}
            reflection: {reflection}
            smoothing: {smoothing}
            """.format(
                    experimental=self.experimental,
                    noise=self.noise,
                    outlier=self.outlier,
                    reflection=self.reflection,
                    smoothing=self.smoothing,
                )

        def __init__(
            self, color=Color(), filters=Filters(),
        ):

            self.color = color
            self.filters = filters

        def __eq__(self, other):
            if self.color == other.color and self.filters == other.filters:
                return True
            return False

        def __str__(self):
            return """Processing:
        color: {color}
        filters: {filters}
        """.format(
                color=self.color, filters=self.filters,
            )

    def __init__(
        self,
        acquisitions=_zivid.Settings().Acquisitions().value,
        processing=Processing(),
    ):

        self._acquisitions = _convert_to_acquistions(acquisitions)
        self.processing = processing

    @property
    def acquisitions(self):
        return self._acquisitions

    @acquisitions.setter
    def acquisitions(self, value):
        self._acquisitions = _convert_to_acquistions(value)

    def __eq__(self, other):
        if (
            self._acquisitions == other._acquisitions
            and self.processing == other.processing
        ):
            return True
        return False

    def __str__(self):
        return """Settings:
    acquisitions: {acquisitions}
    processing: {processing}
    """.format(
            acquisitions="\n".join([str(element) for element in self.acquisitions]),
            processing=self.processing,
        )


def _convert_to_acquistions(inputs):
    temp = []  # Settings().Acquisitions()
    for acquisition_element in inputs:
        if isinstance(acquisition_element, Settings.Acquisition):
            temp.append(acquisition_element)
        elif isinstance(acquisition_element, Settings.Acquisition):
            # temp_settings = Settings()
            # temp_settings.acquisitions = [acquisition_element]
            # acuis = to_internal_settings(temp_settings).acquisitions
            # print(acuis.value[0])
            # temp.append(acuis.value[0])
            temp.append(_to_internal_acquisition(acquisition_element))
        else:
            raise TypeError(
                "Unsupported type {type_of_acquisition_element}".format(
                    type_of_acquisition_element=type(acquisition_element)
                )
            )
    print(temp)
    return temp


def _to_internal_acquisition(acquisition):
    internal_acquisition = _zivid.Settings.Acquisition()

    def _to_internal_patterns(patterns):
        internal_patterns = _zivid.Settings.Acquisition.Patterns()

        def _to_internal_sine(sine):
            internal_sine = _zivid.Settings.Acquisition.Patterns.Sine()
            if sine.bidirectional is not None:

                internal_sine.bidirectional = _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional(
                    sine.bidirectional
                )
            else:
                internal_sine.bidirectional = (
                    _zivid.Settings.Acquisition.Patterns.Sine.Bidirectional()
                )
            pass  # no children
            return internal_sine

        internal_patterns.sine = _to_internal_sine(patterns.sine)
        return internal_patterns

    if acquisition.aperture is not None:
        internal_acquisition.aperture = _zivid.Settings.Acquisition.Aperture(
            acquisition.aperture
        )
    else:
        internal_acquisition.aperture = _zivid.Settings.Acquisition.Aperture()
    if acquisition.brightness is not None:

        internal_acquisition.brightness = _zivid.Settings.Acquisition.Brightness(
            acquisition.brightness
        )
    else:
        internal_acquisition.brightness = _zivid.Settings.Acquisition.Brightness()
    if acquisition.exposure_time is not None:

        internal_acquisition.exposure_time = _zivid.Settings.Acquisition.ExposureTime(
            acquisition.exposure_time
        )
    else:
        internal_acquisition.exposure_time = _zivid.Settings.Acquisition.ExposureTime()
    if acquisition.gain is not None:

        internal_acquisition.gain = _zivid.Settings.Acquisition.Gain(acquisition.gain)
    else:
        internal_acquisition.gain = _zivid.Settings.Acquisition.Gain()

    internal_acquisition.patterns = _to_internal_patterns(acquisition.patterns)
    return internal_acquisition
