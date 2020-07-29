from datetime import datetime
import pytest

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
    import datetime

    assert isinstance(frame_info.time_stamp, datetime.datetime)
    assert isinstance(str(frame_info.time_stamp), str)
    new_time_stamp = datetime.datetime(1992, 2, 7)
    frame_info.time_stamp = new_time_stamp
    assert isinstance(str(frame_info.time_stamp), str)
    assert isinstance(frame_info.time_stamp, datetime.datetime)
    assert frame_info.time_stamp == new_time_stamp


def test_set_illegal_time_stamp(frame_info):
    import datetime

    with pytest.raises(ValueError):
        frame_info.time_stamp = datetime.datetime(1337, 1, 1)
    with pytest.raises(ValueError):
        frame_info.time_stamp = datetime.datetime(1969, 12, 31)


def test_init_illegal_time_stamp():
    import datetime
    import zivid

    with pytest.raises(ValueError):
        _ = zivid.FrameInfo(time_stamp=datetime.datetime(1969, 12, 31))
    with pytest.raises(ValueError):
        _ = zivid.FrameInfo(time_stamp=datetime.datetime(1337, 1, 1))
