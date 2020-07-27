"""Contains the PointCloud class."""
import numpy

import _zivid


class PointCloud:
    """A point cloud."""

    def __init__(self, internal_point_cloud):
        """Create a point cloud from an internal point cloud.

        Args:
            internal_point_cloud: a internal point cloud

        Raises:
            TypeError: unsupported type provided for internal point cloud

        """
        if not isinstance(internal_point_cloud, _zivid.PointCloud):
            raise TypeError(
                "Unsupported type for argument internal_point_cloud. Got {}, expected {}".format(
                    type(internal_point_cloud), type(_zivid.PointCloud)
                )
            )
        self.__impl = internal_point_cloud

    def copy_data(self, data_format):
        """Convert point cloud to numpy array.

        Returns:
            a numpy array

        """
        self.__impl.assert_not_released()
        if data_format == "xyzrgba":
            return numpy.array(self.__impl)
        raise ValueError(
            "Unsupported data format: {data_format}".format(data_format=data_format)
        )

    @property
    def height(self):
        """Return height (number of rows) of point cloud.

        Returns:
            a positive integer

        """
        return self.__impl.height()

    @property
    def width(self):
        """Return width (number of columns) of point cloud.

        Returns:
            a positive integer

        """
        return self.__impl.width()

    def release(self):
        """Release the underlying resources."""
        self.__impl.release()

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.release()

    def __del__(self):
        self.release()
