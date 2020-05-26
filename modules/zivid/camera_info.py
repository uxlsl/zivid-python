import _zivid


class CameraInfo:
    class Revision:
        def __init__(
            self,
            major=_zivid.CameraInfo().Revision().Major().value,
            minor=_zivid.CameraInfo().Revision().Minor().value,
        ):
            self.major = major
            self.minor = minor

        def __eq__(self, other):
            if self.major == other.major and self.minor == other.minor:
                return True
            return False

        def __str__(self):
            return """Revision:
        major: {major}
        minor: {minor}
        """.format(
                major=self.major, minor=self.minor,
            )

    class UserData:
        def __init__(
            self, max_size_bytes=_zivid.CameraInfo().UserData().MaxSizeBytes().value,
        ):
            self.max_size_bytes = max_size_bytes

        def __eq__(self, other):
            if self.max_size_bytes == other.max_size_bytes:
                return True
            return False

        def __str__(self):
            return """UserData:
        max_size_bytes: {max_size_bytes}
        """.format(
                max_size_bytes=self.max_size_bytes,
            )

    def __init__(
        self,
        firmware_version=_zivid.CameraInfo().FirmwareVersion().value,
        model_name=_zivid.CameraInfo().ModelName().value,
        serial_number=_zivid.CameraInfo().SerialNumber().value,
        revision=Revision(),
        user_data=UserData(),
    ):
        self.firmware_version = firmware_version
        self.model_name = model_name
        self.serial_number = serial_number
        self.revision = revision
        self.user_data = user_data

    def __eq__(self, other):
        if (
            self.firmware_version == other.firmware_version
            and self.model_name == other.model_name
            and self.serial_number == other.serial_number
            and self.revision == other.revision
            and self.user_data == other.user_data
        ):
            return True
        return False

    def __str__(self):
        return """CameraInfo:
    firmware_version: {firmware_version}
    model_name: {model_name}
    serial_number: {serial_number}
    revision: {revision}
    user_data: {user_data}
    """.format(
            firmware_version=self.firmware_version,
            model_name=self.model_name,
            serial_number=self.serial_number,
            revision=self.revision,
            user_data=self.user_data,
        )