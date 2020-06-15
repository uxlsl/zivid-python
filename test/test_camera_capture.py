# pylint: disable=import-outside-toplevel
import pytest


def test_one_acquistion_in_list(file_camera):
    import zivid

    acquistions = [zivid.Settings.Acquistion()]
    settings = zivid.Settings(acquistions=acquistions)
    assert isinstance(settings_collection, list)
    with file_camera.capture(settings) as frame:
        assert frame
        assert isinstance(frame, zivid.frame.Frame)


def test_five_acquistions_in_list(file_camera):
    import zivid

    acquistions = [
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
    ]
    settings = zivid.Settings(acquistions=acquistions)
    assert isinstance(settings_collection, list)
    with file_camera.capture(settings) as frame:
        assert frame
        assert isinstance(frame, zivid.frame.Frame)


def test_one_acquistion_in_tuple(file_camera):
    import zivid

    acquistions = (zivid.Settings.Acquistion(),)
    settings = zivid.Settings(acquistions=acquistions)
    assert isinstance(settings_collection, tuple)
    with file_camera.capture(settings) as frame:
        assert frame
        assert isinstance(frame, zivid.frame.Frame)


def test_five_acquistion_in_tuple(file_camera):
    import zivid

    acquistions = (
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
        zivid.Settings.Acquistion(),
    )
    settings = zivid.Settings(acquistions=acquistions)
    assert isinstance(settings_collection, tuple)
    with file_camera.capture(settings) as frame:
        assert frame
        assert isinstance(frame, zivid.frame.Frame)


def test_illegal_settings(file_camera):
    import zivid

    with pytest.raises(RuntimeError):
        file_camera.capture(zivid.Settings())

    with pytest.raises(TypeError):
        file_camera.capture([1, 2, 3, 4, 5])

    with pytest.raises(TypeError):
        file_camera.capture([zivid.Settings(), zivid.Settings(), 3])

    with pytest.raises(TypeError):
        file_camera.capture(file_camera.capture())


def test_empty_settings_list(file_camera):
    import _zivid

    with pytest.raises(TypeError):
        file_camera.capture([])
