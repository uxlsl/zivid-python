import _zivid


class Settings:
    class Frame:
        def __init__(
            self,
            aperture=_zivid.Settings().Frame().Aperture().value,
            bidirectional=_zivid.Settings().Frame().Bidirectional().value,
            brightness=_zivid.Settings().Frame().Brightness().value,
            exposure_time=_zivid.Settings().Frame().ExposureTime().value,
            gain=_zivid.Settings().Frame().Gain().value,
        ):
            self.aperture = aperture
            self.bidirectional = bidirectional
            self.brightness = brightness
            self.exposure_time = exposure_time
            self.gain = gain

        def __eq__(self, other):
            if (
                self.aperture == other.aperture
                and self.bidirectional == other.bidirectional
                and self.brightness == other.brightness
                and self.exposure_time == other.exposure_time
                and self.gain == other.gain
            ):
                return True
            return False

        def __str__(self):
            return """Frame:
        aperture: {aperture}
        bidirectional: {bidirectional}
        brightness: {brightness}
        exposure_time: {exposure_time}
        gain: {gain}
        """.format(
                aperture=self.aperture,
                bidirectional=self.bidirectional,
                brightness=self.brightness,
                exposure_time=self.exposure_time,
                gain=self.gain,
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
                    self.blue = blue
                    self.green = green
                    self.red = red

                def __eq__(self, other):
                    if (
                        self.blue == other.blue
                        and self.green == other.green
                        and self.red == other.red
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
            class Contrast:
                class Removal:
                    def __init__(
                        self,
                        enabled=_zivid.Settings()
                        .Processing.Filters.Contrast.Removal()
                        .Enabled()
                        .value,
                        threshold=_zivid.Settings()
                        .Processing.Filters.Contrast.Removal()
                        .Threshold()
                        .value,
                    ):
                        self.enabled = enabled
                        self.threshold = threshold

                    def __eq__(self, other):
                        if (
                            self.enabled == other.enabled
                            and self.threshold == other.threshold
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
                    return """Contrast:
                removal: {removal}
                """.format(
                        removal=self.removal,
                    )

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
                            self.enabled = enabled
                            self.strength = strength

                        def __eq__(self, other):
                            if (
                                self.enabled == other.enabled
                                and self.strength == other.strength
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
                            self.enabled = enabled
                            self.threshold = threshold

                        def __eq__(self, other):
                            if (
                                self.enabled == other.enabled
                                and self.threshold == other.threshold
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
                        self.enabled = enabled
                        self.threshold = threshold

                    def __eq__(self, other):
                        if (
                            self.enabled == other.enabled
                            and self.threshold == other.threshold
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
                        self.enabled = enabled

                    def __eq__(self, other):
                        if self.enabled == other.enabled:
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
                        self.enabled = enabled
                        self.sigma = sigma

                    def __eq__(self, other):
                        if self.enabled == other.enabled and self.sigma == other.sigma:
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
                contrast=Contrast(),
                experimental=Experimental(),
                outlier=Outlier(),
                reflection=Reflection(),
                smoothing=Smoothing(),
            ):
                self.contrast = contrast
                self.experimental = experimental
                self.outlier = outlier
                self.reflection = reflection
                self.smoothing = smoothing

            def __eq__(self, other):
                if (
                    self.contrast == other.contrast
                    and self.experimental == other.experimental
                    and self.outlier == other.outlier
                    and self.reflection == other.reflection
                    and self.smoothing == other.smoothing
                ):
                    return True
                return False

            def __str__(self):
                return """Filters:
            contrast: {contrast}
            experimental: {experimental}
            outlier: {outlier}
            reflection: {reflection}
            smoothing: {smoothing}
            """.format(
                    contrast=self.contrast,
                    experimental=self.experimental,
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
        frames=_zivid.Settings().Frames().value,
        frame=Frame(),
        processing=Processing(),
    ):
        self.frames = frames
        self.frame = frame
        self.processing = processing

    def __eq__(self, other):
        if (
            self.frames == other.frames
            and self.frame == other.frame
            and self.processing == other.processing
        ):
            return True
        return False

    def __str__(self):
        return """Settings:
    frames: {frames}
    frame: {frame}
    processing: {processing}
    """.format(
            frames=self.frames, frame=self.frame, processing=self.processing,
        )
