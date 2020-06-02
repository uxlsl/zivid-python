import zivid


def to_frame_info(internal_frame_info):
    def _to_software_version(internal_software_version):

        return zivid.FrameInfo.SoftwareVersion(
            core=internal_software_version.core.value,
        )

    return zivid.FrameInfo(
        software_version=_to_software_version(internal_frame_info.softwareversion),
        time_stamp=internal_frame_info.timestamp.value,
    )
