"""This file imports used classes, modules and packages."""
import inspect
from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple

@dataclass
class NodeData:
    is_leaf: bool
    path: Tuple[str]
    children: tuple

def _module_comment():
    return '"""Contains Settings class."""'


def _imports():
    return "import _zivid"


def _base_node(
    class_name, class_description, nested_classes, leaf_nodes, indentation_level
):
    eq_special_member_function = """
    def __eq__(self, other):
        if self.enabled == other.enabled:
            return True
        return False"""

    str_special_member_function = '''
    def __str__(self):
        return """SOme description""".format(
    self.enabled
    )
    '''
    init_special_member_function = '''def __init__(
        self, enabled=_zivid.Settings().filters.reflection.enabled.value
    ):
        """Initialize reflection filter.
        Args:
            enabled: a bool
        """
        #set self.whatever here
    '''
    unindented_class = """class {class_name}:
    {class_description}

{nested_classes}

    {init_special_member_function}

    {eq_special_member_function}

    {str_special_member_function}    
    
    
    """.format(
        class_name=class_name,
        class_description=class_description,
        nested_classes=nested_classes,
        init_special_member_function=init_special_member_function,
        eq_special_member_function=eq_special_member_function,
        str_special_member_function=str_special_member_function,
    )
    indented_lines = []
    for line in unindented_class.splitlines():
        indented_lines.append("    " * (indentation_level) + line)
    return "\n".join(indented_lines)


def _create_file():
    from _zivid._zivid import Settings

    settings_tree = _construct_tree_from_classes(_recursion(Settings))
    print(
        _base_node(
            class_name="Settings",
            class_description="some_description here",
            nested_classes=_base_node(
                class_name="nested",
                class_description="som other desc",
                nested_classes="",
                leaf_nodes="blablaba",
                indentation_level=1,
            ),
            leaf_nodes="enabled",
            indentation_level=0,
        )
    )
    return "{}\n{}\n\n{}".format(_module_comment(), _imports(), settings_tree)


def _traverse_settings():
    print("hello")
    # _start_traverse()
    print(_create_file())


def _recursion(current_class):
    rec_classes = []
    # print("this is current class")
    # print(current_class)
    for my_cls in inner_classes_list(current_class):
        rec_classes.extend(_recursion(my_cls))
    rec_classes.append(current_class)
    return rec_classes


def _start_traverse():
    from _zivid._zivid import Settings

    _construct_tree_from_classes(_recursion(Settings))


def _construct_tree_from_classes(class_tree):
    tree = []
    for container_or_leaf in class_tree:
        tree.append(container_or_leaf.path)
    tree.sort()
    for ele in tree:
        print(ele)
    return "\n".join(tree)


def inner_classes_list(cls):
    return [
        cls_attribute
        for cls_attribute in cls.__dict__.values()
        if inspect.isclass(cls_attribute)
    ]
    # and issubclass(cls_attribute, SuperBar)]


_traverse_settings()
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
        hdr,
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
