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
    is_enum: bool
    enum_vars: tuple
    enum_default_value: str
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
    if node_data.is_enum:
        return "\n    def __init__(self,value=none):\n        self._value = value\n"
    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    signature_vars = ""
    member_variable_set = ""
    path = ".{path}".format(path=node_data.path,) if node_data.path else ""
    for member in member_variables:
        signature_vars += f"{member.variable_name}={member.default_value},"
        member_variable_set += f"\n        if {member.variable_name} is not None:"
        member_variable_set += f"\n            self._{member.variable_name} = _zivid.{settings_type}{path}.{inflection.camelize(member.variable_name)}({member.variable_name})"
        member_variable_set += f"\n        else:"
        member_variable_set += f"\n            self._{member.variable_name} = _zivid.{settings_type}{path}.{inflection.camelize(member.variable_name)}()"

    for child_class in child_class_member_variables:
        signature_vars += f"{child_class.variable_name}={child_class.default_value},"
        member_variable_set += f"\n        self.{inflection.underscore(child_class.name)} = {inflection.underscore(child_class.name)}"

    # for variable_name in _variable_names(node_data, settings_type):
    #    path = ".{path}".format(path=node_data.path,) if node_data.path else ""
    #    member_variable_set += f"\n        if {variable_name} is not None:"
    #    member_variable_set += f"\n            self._{variable_name} = _zivid.{settings_type}{path}({variable_name})"

    return """
    def __init__(
        self,
        {signature_vars}
    ):
        {member_variable_set}""".format(
        signature_vars=signature_vars, member_variable_set=member_variable_set
    )


def _create_eq_special_member_function(node_data, settings_type: str):
    if node_data.is_enum:
        return "\n    def __eq__(self,other):\n        if self.value == other.value:\n            return True\n        return False"
    member_variables_equality = list()
    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    for member in member_variables:
        member_variables_equality.append(
            f"self._{member.variable_name} == other._{member.variable_name}"
        )
    for child in child_class_member_variables:
        member_variables_equality.append(
            f"self.{child.variable_name} == other.{child.variable_name}"
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

    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    for member in member_variables:
        element = member.variable_name
        member_variables_str += f"{element}: {{{element}}}\n    "
        formatting_string += "{variable_name}=self.{variable_name},".format(
            variable_name=element
        )

    for child in child_class_member_variables:
        element = child.variable_name
        member_variables_str += f"{element}: {{{element}}}\n    "
        formatting_string += "{variable_name}=self.{variable_name},".format(
            variable_name=element
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


def _create_properties(node_data, settings_type: str):
    get_properties = "\n"
    set_properties = "\n"

    get_property_template = (
        "    @property\n    def {member}(self):\n        return self._{member}.value\n"
    )
    set_property_template = "    @{member}.setter\n    def {member}(self,value):\n        self._{member} = _zivid.{settings_type}{path}.{non_snake_member}(value)\n"
    for member in node_data.member_variables:
        path = ".{path}".format(path=node_data.path,) if node_data.path else ""
        get_properties += get_property_template.format(
            member=inflection.underscore(member)
        )
        set_properties += set_property_template.format(
            member=inflection.underscore(member),
            path=path,
            non_snake_member=member,
            settings_type=settings_type,
        )
    return f"{get_properties}\n{set_properties}"


def _create_class_variables(node_data):
    sub_strings = []
    for enum_key, enum_value in node_data.enum_vars:
        sub_strings.append(
            f"{enum_key} = _zivid.capture_assistant.SuggestSettingsParameters.{node_data.path}.enum.{enum_value}"
        )  # {enum_value}")
    return "\n    ".join(
        sub_strings
    )  # + f"# _zivid.capture_assistant.{node_data.path}.enum"


def _create_class(node_data, settings_type: str):
    nested_classes = [
        _create_class(element, settings_type=settings_type)
        for element in node_data.children
    ]
    nested_classes_string = "\n".join(nested_classes)
    base_class = """
class {class_name}:
    {nested_classes}
    {class_variables}
    {init_special_member_function}
    {get_set_properties}
    {eq_special_member_function}
    {str_special_member_function}
""".format(
        class_name=node_data.name,
        nested_classes=nested_classes_string,
        class_variables=_create_class_variables(node_data),
        init_special_member_function=_create_init_special_member_function(
            node_data, settings_type=settings_type
        ),
        eq_special_member_function=_create_eq_special_member_function(
            node_data, settings_type=settings_type
        ),
        str_special_member_function=_create_str_special_member_function(
            node_data, settings_type=settings_type
        ),
        get_set_properties=_create_properties(node_data, settings_type=settings_type),
    )
    indented_lines = list()
    for line in base_class.splitlines():
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)


def _recursion(current_class, indentation_level):
    child_classes = list()
    if not (hasattr(current_class, "valid_values") and hasattr(current_class, "enum")):
        for my_cls in _inner_classes_list(current_class):
            child_classes.append(
                _recursion(my_cls, indentation_level=indentation_level + 1)
            )
        is_leaf = not bool(_inner_classes_list(current_class))
    else:
        is_leaf = False

    member_variables = list()
    to_be_removed = list()
    for child in child_classes:
        if child.is_leaf:
            member_variables.append(child.name)
            to_be_removed.append(child)
    child_classes = [
        element for element in child_classes if element not in to_be_removed
    ]
    # import enum
    # if isinstance(current_class, enum.Enum):
    #     print("is enum")
    # else:
    #     print("is not enum")
    # try:
    print(current_class.name)
    print(dir(current_class))
    # print(dir(current_class.name))
    if hasattr(current_class, "valid_values") and hasattr(current_class, "enum"):
        # _ = current_class.path
        # print("has path")
        print("this is a enum thingy")
        path = current_class.path.replace("/", ".")
        is_enum = True
        # print(current_class.enum)
        # print(dir(current_class.enum))
        # print(current_class.enum.hz50)
        # print(dir(current_class.enum.hz50))
        # print(current_class.enum.hz50.name)
        print("defaultvalue:")
        print(current_class().value)
        print(dir(current_class().value))
        print(current_class().value.name)
        enum_default_value = current_class().value.name
        enum_vars = []
        members = [a for a in dir(current_class.enum)]
        for member in members:
            if str(member).startswith("__"):
                continue
            if str(member) == "name":
                continue
            print("this is member: " + member)
            # print("___")
            print(getattr(current_class.enum, member).name)
            enum_vars.append((member, getattr(current_class.enum, member).name))
            # print("--")
            # print(dir(getattr(current_class.enum, member)))
        #
        # enum_vars = []#current_class.enum

    else:
        path = current_class.path.replace("/", ".")
        is_enum = False
        # print("does not have path")
        print("this is not a enum thingy")
        enum_vars = []
        enum_default_value = None
    #   path = None
    #   is_enum=True
    # except Exception:
    #   print("hello2")
    #   path = current_class.path.replace("/", ".")
    #   is_enum=False
    print(enum_vars)
    print(is_enum)
    print("-----------------------\n-------------------------")

    my_class = NodeData(
        name=current_class.name,
        is_leaf=is_leaf,
        is_enum=is_enum,
        enum_vars=enum_vars,
        enum_default_value=enum_default_value,
        path=path,
        children=child_classes,
        member_variables=member_variables,
        indentation_level=indentation_level,
    )
    return my_class
