import inspect
from typing import List, Tuple
from dataclasses import dataclass
import inflection


@dataclass
class MemberVariable:
    camel_case: str
    snake_case: str
    # variable_name: str
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
    member_variables: Tuple[MemberVariable]
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
            print(member_var)
            default_value = f"_zivid.{settings_type}().{f'{node_data.path}().' if node_data.path else ''}{member_var.camel_case}().value"
            # camel_case = member_var
            # snake_case
            # variable_name = member_var.snake_case#inflection.underscore(member_var)
            member_variables.append(
                MemberVariable(
                    camel_case=member_var.camel_case,
                    default_value=default_value,
                    snake_case=member_var.snake_case,
                )
            )
    print(member_variables)
    return member_variables


def _get_child_class_member_variables(node_data):
    child_class_members_variables = []
    if node_data.children:
        for child in node_data.children:
            child_class_members_variables.append(
                MemberVariable(
                    camel_case=child.name,
                    snake_case=inflection.underscore(child.name),
                    # default_value=f"{child.name}()",
                    default_value="None",
                )
            )

    return child_class_members_variables


def _variable_names(node_data, settings_type: str):
    member_variables = _get_member_variables(node_data, settings_type)
    child_class_member_variables = _get_child_class_member_variables(node_data)
    variable_names = list()
    for member in member_variables:
        variable_names.append(member.snake_case)
    for child_class in child_class_member_variables:
        variable_names.append(child_class.snake_case)
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
        signature_vars += f"{member.snake_case}={member.default_value},"
        member_variable_set += f"\n        if {member.snake_case} is not None:"
        member_variable_set += f"\n            self._{member.snake_case} = _zivid.{settings_type}{path}.{member.camel_case}({member.snake_case})"
        member_variable_set += f"\n        else:"
        member_variable_set += f"\n            self._{member.snake_case} = _zivid.{settings_type}{path}.{member.camel_case}()"

    for child_class in child_class_member_variables:
        signature_vars += f"{child_class.snake_case}={child_class.default_value},"
        member_variable_set += f"\n        if {child_class.snake_case} is None:"
        member_variable_set += f"\n            {child_class.snake_case} = zivid.{settings_type}{path}.{child_class.camel_case}()"
        member_variable_set += f"\n        if not isinstance({child_class.snake_case}, zivid.{settings_type}{path}.{child_class.camel_case}):"
        member_variable_set += f"\n            raise TypeError('Unsupported type: {{value}}'.format(value=type({child_class.snake_case})))"
        member_variable_set += (
            f"\n        self._{child_class.snake_case} = {child_class.snake_case}"
        )

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
            f"self._{member.snake_case} == other._{member.snake_case}"
        )
    for child in child_class_member_variables:
        member_variables_equality.append(
            f"self._{child.snake_case} == other._{child.snake_case}"
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
        element = member.snake_case
        member_variables_str += f"{element}: {{{element}}}\n    "
        formatting_string += "{variable_name}=self.{variable_name},".format(
            variable_name=element
        )

    for child in child_class_member_variables:
        element = child.snake_case
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

    get_member_property_template = (
        "    @property\n    def {member}(self):\n        return self._{member}.value\n"
    )
    set_member_property_template = "    @{member}.setter\n    def {member}(self,value):\n        self._{member} = _zivid.{settings_type}{path}.{non_snake_member}(value)\n"
    for member in node_data.member_variables:
        path = ".{path}".format(path=node_data.path,) if node_data.path else ""
        get_properties += get_member_property_template.format(member=member.snake_case)
        set_properties += set_member_property_template.format(
            member=member.snake_case,
            path=path,
            non_snake_member=member.camel_case,
            settings_type=settings_type,
        )
    set_child_property_template = "    @{member}.setter\n    def {member}(self,value):\n        if not isinstance(value, zivid.{settings_type}{path}.{non_snake_member}):\n            raise TypeError('Unsupported type {{value}}'.format(value=type(value)))\n        self._{member} = value\n"
    get_child_property_template = (
        "    @property\n    def {member}(self):\n        return self._{member}\n"
    )
    for child in node_data.children:
        path = ".{path}".format(path=node_data.path,) if node_data.path else ""
        get_properties += get_child_property_template.format(
            member=inflection.underscore(child.name)
        )
        set_properties += set_child_property_template.format(
            member=inflection.underscore(child.name),
            path=path,
            non_snake_member=child.name,
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
            print(child.name)
            print(type(child.name))
            member_variables.append(
                MemberVariable(
                    camel_case=child.name,
                    snake_case=inflection.underscore(child.name),
                    default_value="None",
                )
            )
            to_be_removed.append(child)
    child_classes = [
        element for element in child_classes if element not in to_be_removed
    ]
    print(current_class.name)
    print(dir(current_class))

    if hasattr(current_class, "valid_values") and hasattr(current_class, "enum"):

        print("this is a enum thingy")
        path = current_class.path.replace("/", ".")
        is_enum = True
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
            print(getattr(current_class.enum, member).name)
            enum_vars.append((member, getattr(current_class.enum, member).name))

    else:
        path = current_class.path.replace("/", ".")
        is_enum = False
        print("this is not a enum thingy")
        enum_vars = []
        enum_default_value = None

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


def create_to_not_internal_converter(node_data, settings_type: str):
    temp_internal_name = "internal_{name}".format(
        name=inflection.underscore(node_data.name)
    )
    nested_converters = [
        create_to_not_internal_converter(element, settings_type=settings_type)
        for element in node_data.children
    ]
    nested_converters_string = "\n".join(nested_converters)
    return_class = "zivid.{settings_type}{path}".format(
        temp_internal_name=temp_internal_name,
        settings_type=settings_type,
        path=".{path}".format(path=node_data.path,) if node_data.path else "",
    )
    member_convert_logic = ""
    for member in node_data.member_variables:
        member_convert_logic += "{member} = {temp_internal_name}.{member}.value,".format(
            member=inflection.underscore(member),
            # member_not_snake_case=member.lower(),
            temp_internal_name=temp_internal_name,
        )

    global_functions = ""
    child_convert_logic = ""
    for child in node_data.children:
        child_convert_logic += "{child}=_to_{child}({temp_internal_name}.{child}),".format(
            child=inflection.underscore(child.name),
            # child_not_snake_case=child.name.lower(),
            temp_internal_name=temp_internal_name,
        )
        global_functions += "\n    global to{path}{child}".format(
            path=f'_{inflection.underscore(node_data.path.replace(".", "_"))}_'.replace(
                "__", "_"
            ),
            child=inflection.underscore(child.name),
        )
        global_functions += "\n    to{path}{child} = _to_{child}".format(
            path=f'_{inflection.underscore(node_data.path.replace(".", "_"))}_'.replace(
                "__", "_"
            ),
            child=inflection.underscore(child.name),
        )

    base_class = """
def _to_{target_name}(internal_{target_name}):
    {nested_converters}
    {global_functions}
    return {return_class}({child_convert_logic} {member_convert_logic})
    
    
""".format(
        target_name=inflection.underscore(node_data.name),
        nested_converters=nested_converters_string,
        return_class=return_class,
        member_convert_logic=member_convert_logic,
        child_convert_logic=child_convert_logic,
        global_functions=global_functions,
    )
    indented_lines = list()
    for line in base_class.splitlines():
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)


def create_to_internal_converter(node_data, settings_type: str):
    temp_internal_name = "internal_{name}".format(
        name=inflection.underscore(node_data.name)
    )
    nested_converters = [
        create_to_internal_converter(element, settings_type=settings_type)
        for element in node_data.children
    ]
    nested_converters_string = "\n".join(nested_converters)
    convert_member_logic = ""
    if node_data.member_variables:
        for member in node_data.member_variables:
            convert_member_logic += "\n    if {name}.{member} is not None:\n".format(
                name=inflection.underscore(node_data.name),
                member=inflection.underscore(member),
            )

            convert_member_logic += "\n        {temp_internal_name}.{member} = _zivid.{settings_type}{path}".format(
                temp_internal_name=temp_internal_name,
                member=inflection.underscore(member),
                path=".{path}.{member_as_class}({name}.{member})".format(
                    path=node_data.path,
                    member_as_class=member,
                    name=inflection.underscore(node_data.name),
                    member=inflection.underscore(member),
                )
                if node_data.path
                else "()",
                settings_type=settings_type,
            )
            convert_member_logic += "\n    else:"
            convert_member_logic += "\n        {temp_internal_name}.{member} = _zivid.{settings_type}{path}".format(
                temp_internal_name=temp_internal_name,
                member=inflection.underscore(member),
                path=".{path}.{member_as_class}()".format(
                    path=node_data.path, member_as_class=member,
                )
                if node_data.path
                else "()",
                settings_type=settings_type,
            )

    convert_children_logic = ""
    global_functions = ""
    if node_data.children:
        for child in node_data.children:
            convert_children_logic += "\n    {temp_internal_name}.{child} = _to_internal_{child}({name}.{child})".format(
                temp_internal_name=temp_internal_name,
                child=inflection.underscore(child.name),
                name=inflection.underscore(node_data.name),
            )
            # expose internal_function through global
            global_functions += "\n    global to_internal{path}{child}".format(
                path=f'_{inflection.underscore(node_data.path.replace(".", "_"))}_'.replace(
                    "__", "_"
                ),
                child=inflection.underscore(child.name),
            )
            global_functions += "\n    to_internal{path}{child} = _to_internal_{child}".format(
                path=f'_{inflection.underscore(node_data.path.replace(".", "_"))}_'.replace(
                    "__", "_"
                ),
                child=inflection.underscore(child.name),
            )
    # else:
    #     convert_children_logic = "pass # no children"

    base_class = """
def _to_internal_{target_name}({target_name}):
    {temp_internal_name} = _zivid.{settings_type}{path}
    {nested_converters}
    {global_functions}
    {convert_member_logic}
    {convert_children_logic}
    return {temp_internal_name}
""".format(
        target_name=inflection.underscore(node_data.name),
        nested_converters=nested_converters_string,
        convert_member_logic=convert_member_logic,
        convert_children_logic=convert_children_logic,
        path="." + node_data.path + "()" if node_data.path else "()",
        temp_internal_name=temp_internal_name,
        global_functions=global_functions,
        settings_type=settings_type,
    )
    indented_lines = list()
    for line in base_class.splitlines():
        indented_lines.append("    " + line)
    return "\n".join(indented_lines)
