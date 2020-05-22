"""This file imports used classes, modules and packages."""
"""This file imports used classes, modules and packages."""
import inspect
from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple
import subprocess
import sys
from pathlib import Path
#print(sys.path.append(Path(__file__).parent.parent))
#print(sys.path)
import _zivid.generate_settings
import _zivid.generators.generate_settings_2d

_zivid.generate_settings.traverse_settings()
_zivid.generators.generate_settings_2d._traverse_settings()

try:
    from _zivid._zivid import (  # pylint: disable=import-error,no-name-in-module
        __version__,
        Application,
        Camera,
        CameraState,
        environment,
        firmware,
        hand_eye,
        capture_assistant,
        Frame,
        FrameInfo,
        PointCloud,
        Settings,
        version,
        Settings2D,
        Frame2D,
        Image,
    )
except ImportError as ex:
    import platform

    def __missing_sdk_error_message():
        error_message = """Failed to import the Zivid Python C-module, please verify that:
 - Zivid SDK is installed
 - Zivid SDK version is matching the SDK version part of the Zivid Python version """
        if platform.system() != "Windows":
            return error_message
        return (
            error_message
            + """
 - Zivid SDK libraries location is in system PATH"""
        )

    raise ImportError(__missing_sdk_error_message()) from ex
