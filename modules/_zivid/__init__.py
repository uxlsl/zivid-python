"""This file imports used classes, modules and packages."""
import inspect
from collections import namedtuple
from dataclasses import dataclass
from typing import Tuple
import subprocess


@dataclass
class NodeData:
    name: str
    is_leaf: bool
    path: str
    children: tuple
    member_variables: tuple
    indentation_level: int


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

    settings_tree = _recursion(Settings)
    print(settings_tree)

    # print(
    #     _base_node(
    #         class_name="Settings",
    #         class_description="some_description here",
    #         nested_classes=_base_node(
    #             class_name="nested",
    #             class_description="som other desc",
    #             nested_classes="",
    #             leaf_nodes="blablaba",
    #             indentation_level=1,
    #         ),
    #         leaf_nodes="enabled",
    #         indentation_level=0,
    #     )
    # )
    # return "{}\n{}\n\n{}".format(_module_comment(), _imports(), settings_tree)


def _traverse_settings():
    print("hello")
    _start_traverse()
    # print(_create_file())


# def class_to_node_data(target_class):


def _recursion(current_class, indentation_level):
    child_classes = list()

    for my_cls in inner_classes_list(current_class):
        child_classes.append(
            _recursion(my_cls, indentation_level=indentation_level + 1)
        )

        # rec_classes.extend(_recursion(my_cls))
    is_leaf = not bool(inner_classes_list(current_class))

    # my_class = NodeData(name=current_class, is_leaf=is_leaf, path=current_class.path, child_classes)
    # print(dir(current_class))
    member_variables = list()
    to_be_removed = list()
    for child in child_classes:
        if child.is_leaf:
            member_variables.append(child.name)
            to_be_removed.append(child)
    child_classes = [
        element for element in child_classes if element not in to_be_removed
    ]
    # for child in to_be_removed:
    #     child_classes.remove()
    # is_leaf = not bool(child_classes)

    my_class = NodeData(
        name=current_class.name,
        is_leaf=is_leaf,
        path=current_class.path.replace("/", "."),
        children=child_classes,
        member_variables=member_variables,
        indentation_level=indentation_level,
    )

    #
    #     #rec_classes.append(current_class)
    return my_class


def _start_traverse():
    from _zivid._zivid import Settings
    import tempfile
    from pathlib import Path

    # _construct_tree_from_classes()
    data_model = _recursion(Settings, indentation_level=0)
    with tempfile.NamedTemporaryFile(suffix=".py") as temp_file:
        temp_file = Path(temp_file.name)
        raw_text = _create_settings_py(data_model)
        new_lines = []
        for line in raw_text.splitlines():
            new_lines.append(line[4:])

        temp_file.write_text("\n".join(new_lines))
        print(temp_file)
        print(temp_file.exists())
        print(str(temp_file))
        print(temp_file.read_text())
        subprocess.check_output((f"black {temp_file}"), shell=True)
        print(temp_file.read_text())
        
    # print()


@dataclass
class MemberVariable:
    name: str
    variable_name: str
    default_value: str


def _get_member_variables(node_data):
    import inflection

    member_variables = []
    if node_data.member_variables:
        for member_var in node_data.member_variables:
            default_value = f"_zivid.Settings().{f'{node_data.path}.' if node_data.path else ''}{member_var}.value"
            name = member_var
            variable_name = inflection.underscore(member_var)
            member_variables.append(
                MemberVariable(
                    name=name, default_value=default_value, variable_name=variable_name
                )
            )
    return member_variables


def _create_init_special_member_function(node_data):
    member_variables = _get_member_variables(node_data)
    signature_vars = ""
    for member in member_variables:
        signature_vars += f"{member.variable_name}={member.default_value},"
    return '''
    def __init__(
        self,
        {signature_vars}
    ):
        """Initialize contrast filter.
    
        Args:
            enabled: a bool
            threshold: a real number
    
        """
    
        self.enabled = enabled
        self.threshold = threshold'''.format(
        signature_vars=signature_vars
    )


def _create_class(node_data):
    nested_classes = [_create_class(element) for element in node_data.children]
    nested_classes_string = "\n".join(nested_classes)
    base_class = """
class {class_name}:
    {nested_classes}
    {init_special_member_function}
""".format(
        class_name=node_data.name,
        nested_classes=nested_classes_string,
        init_special_member_function=_create_init_special_member_function(node_data),
    )
    indented_lines = list()
    first_line=True
    for line in base_class.splitlines():
        # if first_line:
        #     indented_lines.append("    " * node_data.indentation_level + line)
        #     first_line = False
        #     continue
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)


def _create_settings_py(data_model):
    indentation_level = 0
    return _create_class(data_model)


def _construct_tree_from_classes(class_tree):
    print(class_tree)
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
