import inspect
from typing import List
from dataclasses import dataclass
import inflection


@dataclass
class MemberVariable:
    name: str
    variable_name: str
    default_value: str


@dataclass
class NodeData:
    name: str
    is_leaf: bool
    path: str
    children: tuple
    member_variables: tuple
    indentation_level: int


def _inner_classes_list(cls) -> List:
    return [
        cls_attribute
        for cls_attribute in cls.__dict__.values()
        if inspect.isclass(cls_attribute)
    ]


def _imports(internal: bool, settings: bool) -> str:
    imports = ""
    if internal:
        imports += "    import _zivid\n"
    if settings:
        imports += "    import zivid\n"
    return imports


def _get_member_variables(node_data, settings_type: str):
    member_variables = []
    if node_data.member_variables:
        for member_var in node_data.member_variables:
            default_value = f"_zivid.{settings_type}().{f'{node_data.path}().' if node_data.path else ''}{member_var}().value"
            name = member_var
            variable_name = inflection.underscore(member_var)
            member_variables.append(
                MemberVariable(
                    name=name, default_value=default_value, variable_name=variable_name
                )
            )
    return member_variables


def _get_child_class_member_variables(node_data):
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


def _variable_names(node_data, settings_type: str):
    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    variable_names = list()
    for member in member_variables:
        variable_names.append(member.variable_name)
    for child_class in child_class_member_variables:
        variable_names.append(child_class.variable_name)
    return variable_names


def _create_init_special_member_function(node_data, settings_type: str):
    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    signature_vars = ""
    member_variable_set = ""
    for member in member_variables:
        signature_vars += f"{member.variable_name}={member.default_value},"
    for child_class in child_class_member_variables:
        signature_vars += f"{child_class.variable_name}={child_class.default_value},"
    for variable_name in _variable_names(node_data, settings_type):
        member_variable_set += f"self.{variable_name} = {variable_name}\n        "

    return """
    def __init__(
        self,
        {signature_vars}
    ):
        {member_variable_set}""".format(
        signature_vars=signature_vars, member_variable_set=member_variable_set
    )


def _create_eq_special_member_function(node_data, settings_type: str):
    member_variables_equality = list()
    for variable_name in _variable_names(node_data, settings_type):
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


def _create_str_special_member_function(node_data, settings_type: str):
    member_variables_str = "    "
    formatting_string = ""
    for variable_name_str_to_be_formatted, variable_name in [
        (f"{element}: {{{element}}}\n    ", element)
        for element in _variable_names(node_data, settings_type=settings_type)
    ]:
        member_variables_str += variable_name_str_to_be_formatted
        formatting_string += "{variable_name}=self.{variable_name},".format(
            variable_name=variable_name
        )

    member_variables_str.strip()
    str_content = """'''{name}:
{member_variables_str}'''.format({formatting_string})""".format(
        name=node_data.name,
        member_variables_str=member_variables_str,
        formatting_string=formatting_string,
    )
    return """def __str__(self):
            return {str_content}""".format(
        str_content=str_content
    )


def _create_class(node_data, settings_type: str):
    nested_classes = [
        _create_class(element, settings_type=settings_type)
        for element in node_data.children
    ]
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
        init_special_member_function=_create_init_special_member_function(
            node_data, settings_type=settings_type
        ),
        eq_special_member_function=_create_eq_special_member_function(
            node_data, settings_type=settings_type
        ),
        str_special_member_function=_create_str_special_member_function(
            node_data, settings_type=settings_type
        ),
    )
    indented_lines = list()
    for line in base_class.splitlines():
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)


def _recursion(current_class, indentation_level):
    child_classes = list()

    for my_cls in _inner_classes_list(current_class):
        child_classes.append(
            _recursion(my_cls, indentation_level=indentation_level + 1)
        )
    is_leaf = not bool(_inner_classes_list(current_class))

    member_variables = list()
    to_be_removed = list()
    for child in child_classes:
        if child.is_leaf:
            member_variables.append(child.name)
            to_be_removed.append(child)
    child_classes = [
        element for element in child_classes if element not in to_be_removed
    ]

    my_class = NodeData(
        name=current_class.name,
        is_leaf=is_leaf,
        path=current_class.path.replace("/", "."),
        children=child_classes,
        member_variables=member_variables,
        indentation_level=indentation_level,
    )
    return my_class
