"""Contains the PointCloud class."""
import numpy

import _zivid


class PointCloud:
    """Point cloud with x, y, z, RGB and color laid out on a 2D grid.
    
    An instance of this class is a handle to a point cloud stored on the compute device memory.
    This class provides several methods to copy point cloud data from the compute device
    memory to host (CPU) system memory (RAM)."""

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
        """Get the height of the point cloud (number of rows).

        Returns:
            a positive integer

        """
        return self.__impl.height()

    @property
    def width(self):
        """Get the width of the point cloud (number of columns).

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
