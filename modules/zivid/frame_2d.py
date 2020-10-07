"""Contains the Frame class."""
import _zivid

import zivid._settings2_d_converter as _settings_converter
import zivid._camera_state_converter as _camera_state_converter
import zivid._frame_info_converter as _frame_info_converter
from zivid.image import Image


class Frame2D:
    """A 2D frame captured by a Zivid camera.

    Contains a 2D image as well as metadata, settings and state of the API at the time of capture.
    """

    def __init__(self, impl):  # noqa: D107
        if isinstance(impl, _zivid.Frame2D):
            self.__impl = impl
        else:
            raise TypeError(
                "Unsupported type for argument internal frame_2d. Got {}, expected {}.".format(
                    type(impl).__name__, _zivid.Frame2D
                )
            )

    def __str__(self):
        return str(self.__impl)

    def image_rgba(self):
        """Get color (RGBA) image from the frame.

        Returns:
            An image instance containing RGBA data
        """
        return Image(self.__impl.image_rgba())

    @property
    def settings(self):
        """Get the settings used to capture this frame.

        Returns:
            A Settings2D instance
        """
        return _settings_converter.to_settings2_d(  # pylint: disable=protected-access
            self.__impl.settings
        )

    @property
    def state(self):
        """Get the camera state data at the time of the frame capture.

        Returns:
            A CameraState instance
        """
        return _camera_state_converter.to_camera_state(  # pylint: disable=protected-access
            self.__impl.state
        )

    @property
    def info(self):
        """Get information collected at the time of the capture.

        Returns:
            A FrameInfo instance
        """
        return _frame_info_converter.to_frame_info(  # pylint: disable=protected-access
            self.__impl.info
        )

    def release(self):
        """Release the underlying resources."""
        try:
            impl = self.__impl
        except AttributeError:
            pass
        else:
            impl.release()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.release()

    def __del__(self):
        self.release()
