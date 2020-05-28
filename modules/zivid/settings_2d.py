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

            if aperture is not None:
                self._aperture = _zivid.Settings2D.Acquisition.Aperture(aperture)
            else:
                self._aperture = _zivid.Settings2D.Acquisition.Aperture()
            if brightness is not None:
                self._brightness = _zivid.Settings2D.Acquisition.Brightness(brightness)
            else:
                self._brightness = _zivid.Settings2D.Acquisition.Brightness()
            if exposure_time is not None:
                self._exposure_time = _zivid.Settings2D.Acquisition.ExposureTime(
                    exposure_time
                )
            else:
                self._exposure_time = _zivid.Settings2D.Acquisition.ExposureTime()
            if gain is not None:
                self._gain = _zivid.Settings2D.Acquisition.Gain(gain)
            else:
                self._gain = _zivid.Settings2D.Acquisition.Gain()

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
            self._aperture = _zivid.Settings2D.Acquisition.Aperture(value)

        @brightness.setter
        def brightness(self, value):
            self._brightness = _zivid.Settings2D.Acquisition.Brightness(value)

        @exposure_time.setter
        def exposure_time(self, value):
            self._exposure_time = _zivid.Settings2D.Acquisition.ExposureTime(value)

        @gain.setter
        def gain(self, value):
            self._gain = _zivid.Settings2D.Acquisition.Gain(value)

        def __eq__(self, other):
            if (
                self._aperture == other._aperture
                and self._brightness == other._brightness
                and self._exposure_time == other._exposure_time
                and self._gain == other._gain
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

                    if blue is not None:
                        self._blue = _zivid.Settings2D.Processing.Color.Balance.Blue(
                            blue
                        )
                    else:
                        self._blue = _zivid.Settings2D.Processing.Color.Balance.Blue()
                    if green is not None:
                        self._green = _zivid.Settings2D.Processing.Color.Balance.Green(
                            green
                        )
                    else:
                        self._green = _zivid.Settings2D.Processing.Color.Balance.Green()
                    if red is not None:
                        self._red = _zivid.Settings2D.Processing.Color.Balance.Red(red)
                    else:
                        self._red = _zivid.Settings2D.Processing.Color.Balance.Red()

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
                    self._blue = _zivid.Settings2D.Processing.Color.Balance.Blue(value)

                @green.setter
                def green(self, value):
                    self._green = _zivid.Settings2D.Processing.Color.Balance.Green(
                        value
                    )

                @red.setter
                def red(self, value):
                    self._red = _zivid.Settings2D.Processing.Color.Balance.Red(value)

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
        processing=Processing(),
    ):

        if acquisitions is not None:
            self._acquisitions = _zivid.Settings2D.Acquisitions(acquisitions)
        else:
            self._acquisitions = _zivid.Settings2D.Acquisitions()
        self.processing = processing

    @property
    def acquisitions(self):
        return self._acquisitions.value

    @acquisitions.setter
    def acquisitions(self, value):
        self._acquisitions = _zivid.Settings2D.Acquisitions(value)

    def __eq__(self, other):
        if (
            self._acquisitions == other._acquisitions
            and self.processing == other.processing
        ):
            return True
        return False

    def __str__(self):
        return """Settings2D:
    acquisitions: {acquisitions}
    processing: {processing}
    """.format(
            acquisitions=self.acquisitions, processing=self.processing,
        )
