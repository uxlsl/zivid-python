import _zivid


class Settings2D:
    class Acquisition:
        def __init__(
            self,
            aperture=_zivid.Settings2D().Acquisition().Aperture().value,
            brightness=_zivid.Settings2D().Acquisition().Brightness().value,
            exposure_time=_zivid.Settings2D().Acquisition().ExposureTime().value,
            gain=_zivid.Settings2D().Acquisition().Gain().value,
        ):
            self.aperture = aperture
            self.brightness = brightness
            self.exposure_time = exposure_time
            self.gain = gain

        def __eq__(self, other):
            if (
                self.aperture == other.aperture
                and self.brightness == other.brightness
                and self.exposure_time == other.exposure_time
                and self.gain == other.gain
            ):
                return True
            return False

        def __str__(self):
            return """Acquisition:
        aperture: {aperture}
        brightness: {brightness}
        exposure_time: {exposure_time}
        gain: {gain}
        """.format(
                aperture=self.aperture,
                brightness=self.brightness,
                exposure_time=self.exposure_time,
                gain=self.gain,
            )

    class Processing:
        class Color:
            class Balance:
                def __init__(
                    self,
                    blue=_zivid.Settings2D().Processing.Color.Balance().Blue().value,
                    green=_zivid.Settings2D().Processing.Color.Balance().Green().value,
                    red=_zivid.Settings2D().Processing.Color.Balance().Red().value,
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

        def __init__(
            self, color=Color(),
        ):
            self.color = color

        def __eq__(self, other):
            if self.color == other.color:
                return True
            return False

        def __str__(self):
            return """Processing:
        color: {color}
        """.format(
                color=self.color,
            )

    def __init__(
        self,
        acquisitions=_zivid.Settings2D().Acquisitions().value,
        acquisition=Acquisition(),
        processing=Processing(),
    ):
        self.acquisitions = acquisitions
        self.acquisition = acquisition
        self.processing = processing

    def __eq__(self, other):
        if (
            self.acquisitions == other.acquisitions
            and self.acquisition == other.acquisition
            and self.processing == other.processing
        ):
            return True
        return False

    def __str__(self):
        return """Settings2D:
    acquisitions: {acquisitions}
    acquisition: {acquisition}
    processing: {processing}
    """.format(
            acquisitions=self.acquisitions,
            acquisition=self.acquisition,
            processing=self.processing,
        )
