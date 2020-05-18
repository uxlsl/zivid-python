"""This file imports used classes, modules and packages."""
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



def _imports():
    return "    import _zivid\n"



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
        raw_text = _imports()
        raw_text += _create_settings_py(data_model)
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
        path_to_settings=(Path(__file__).resolve() / ".." / ".." / "zivid" / "settings__3d.py").resolve()
        path_to_settings.write_text(temp_file.read_text())


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
            default_value = f"_zivid.Settings().{f'{node_data.path}().' if node_data.path else ''}{member_var}().value"
            name = member_var
            variable_name = inflection.underscore(member_var)
            member_variables.append(
                MemberVariable(
                    name=name, default_value=default_value, variable_name=variable_name
                )
            )
    return member_variables


def _get_child_class_member_variables(node_data):
    import inflection

    child_class_members_variables = []
    if node_data.children:
        for child in node_data.children:
            child_class_members_variables.append(
                MemberVariable(
                    name=child.name,
                    variable_name=inflection.underscore(child.name),
                    default_value=f"{child.name}()",
                )
            )

    return child_class_members_variables


def _variable_names(node_data):
    member_variables = _get_member_variables(node_data)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    variable_names = list()
    for member in member_variables:
        variable_names.append(member.variable_name)
    for child_class in child_class_member_variables:
        variable_names.append(child_class.variable_name)
    return variable_names


def _create_init_special_member_function(node_data):
    member_variables = _get_member_variables(node_data)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    signature_vars = ""
    member_variable_set = ""
    for member in member_variables:
        signature_vars += f"{member.variable_name}={member.default_value},"
    for child_class in child_class_member_variables:
        signature_vars += f"{child_class.variable_name}={child_class.default_value},"
    for variable_name in _variable_names(node_data):
        member_variable_set += f"self.{variable_name} = {variable_name}\n        "
    # for member in member_variables:
    #     member_variable_set += (
    #         f"self.{member.variable_name} = {member.variable_name}\n        "
    #     )
    # for child_class in child_class_member_variables:
    #     member_variable_set += f"self.{child_class.variable_name}={child_class.variable_name}\n        "
    return """
    def __init__(
        self,
        {signature_vars}
    ):
        {member_variable_set}""".format(
        signature_vars=signature_vars, member_variable_set=member_variable_set
    )


def _create_eq_special_member_function(node_data):
    member_variables_equality = list()
    for variable_name in _variable_names(node_data):
        member_variables_equality.append(
            f"self.{variable_name} == other.{variable_name}"
        )
    equality_logic = " and ".join(member_variables_equality)
    return """def __eq__(self, other):
        if (
            {equality_logic}
        ):
            return True
        return False""".format(
        equality_logic=equality_logic
    )


def _create_str_special_member_function(node_data):
    member_variables_str = "    "
    formatting_string = ""
    for variable_name_str_to_be_formatted, variable_name in [
        (f"{element}: {{{element}}}\n    ", element) for element in _variable_names(node_data)
    ]:
        member_variables_str += variable_name_str_to_be_formatted
        formatting_string += "{variable_name}=self.{variable_name},".format(variable_name=variable_name)

    member_variables_str.strip()
    str_content = """'''{name}:
{member_variables_str}'''.format({formatting_string})""".format(
        name=node_data.name, member_variables_str=member_variables_str, formatting_string=formatting_string
    )
    return """def __str__(self):
            return {str_content}""".format(str_content=str_content)



def _create_class(node_data):
    nested_classes = [_create_class(element) for element in node_data.children]
    nested_classes_string = "\n".join(nested_classes)
    base_class = """
class {class_name}:
    {nested_classes}
    {init_special_member_function}
    {eq_special_member_function}
    {str_special_member_function}
""".format(
        class_name=node_data.name,
        nested_classes=nested_classes_string,
        init_special_member_function=_create_init_special_member_function(node_data),
        eq_special_member_function=_create_eq_special_member_function(node_data),
        str_special_member_function=_create_str_special_member_function(node_data),
    )
    indented_lines = list()
    first_line = True
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


# def _construct_tree_from_classes(class_tree):
#     print(class_tree)
#     tree = []
#     for container_or_leaf in class_tree:
#         tree.append(container_or_leaf.path)
#     tree.sort()
#     for ele in tree:
#         print(ele)
#     return "\n".join(tree)


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
