import zivid


def to_camera_info(internal_camera_info):
    def _to_revision(internal_revision):

        return zivid.CameraInfo.Revision(
            major=internal_revision.major.value, minor=internal_revision.minor.value,
        )

    def _to_user_data(internal_user_data):

        return zivid.CameraInfo.UserData(
            max_size_bytes=internal_user_data.maxsizebytes.value,
        )

    return zivid.CameraInfo(
        revision=_to_revision(internal_camera_info.revision),
        user_data=_to_user_data(internal_camera_info.userdata),
        firmware_version=internal_camera_info.firmwareversion.value,
        model_name=internal_camera_info.modelname.value,
        serial_number=internal_camera_info.serialnumber.value,
    )
