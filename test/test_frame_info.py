# pylint: disable=import-outside-toplevel


def test_time_stamp(frame_info):
    import datetime

    time_stamp = frame_info.time_stamp
    assert time_stamp
    assert isinstance(time_stamp, datetime.datetime)


def test_software_version(frame_info):
    import zivid

    software_version = frame_info.software_version
    assert software_version
    assert isinstance(software_version, zivid.frame_info.FrameInfo.SoftwareVersion)
    assert software_version.core
    assert isinstance(software_version.core, str)


def test_set_time_stamp(frame_info):
    import zivid
    import datetime

    assert isinstance(frame_info.time_stamp, datetime.datetime)
    assert isinstance(str(frame_info.time_stamp), str)
    frame_info.time_stamp = datetime.datetime(1337, 1, 1)
    assert isinstance(str(frame_info.time_stamp), str)
    assert isinstance(frame_info.time_stamp, datetime.datetime)
