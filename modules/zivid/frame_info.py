import _zivid


class FrameInfo:
    class SoftwareVersion:
        def __init__(
            self, core=_zivid.FrameInfo().SoftwareVersion().Core().value,
        ):

            if core is not None:
                self._core = _zivid.FrameInfo.SoftwareVersion.Core(core)
            else:
                self._core = _zivid.FrameInfo.SoftwareVersion.Core()

        @property
        def core(self):
            return self._core.value

        @core.setter
        def core(self, value):
            self._core = _zivid.FrameInfo.SoftwareVersion.Core(value)

        def __eq__(self, other):
            if self._core == other._core:
                return True
            return False

        def __str__(self):
            return """SoftwareVersion:
        core: {core}
        """.format(
                core=self.core,
            )

    def __init__(
        self,
        time_stamp=_zivid.FrameInfo().TimeStamp().value,
        software_version=SoftwareVersion(),
    ):

        if time_stamp is not None:
            self._time_stamp = _zivid.FrameInfo.TimeStamp(time_stamp)
        else:
            self._time_stamp = _zivid.FrameInfo.TimeStamp()
        self.software_version = software_version

    @property
    def time_stamp(self):
        return self._time_stamp.value

    @time_stamp.setter
    def time_stamp(self, value):
        self._time_stamp = _zivid.FrameInfo.TimeStamp(value)

    def __eq__(self, other):
        if (
            self._time_stamp == other._time_stamp
            and self.software_version == other.software_version
        ):
            return True
        return False

    def __str__(self):
        return """FrameInfo:
    time_stamp: {time_stamp}
    software_version: {software_version}
    """.format(
            time_stamp=self.time_stamp, software_version=self.software_version,
        )