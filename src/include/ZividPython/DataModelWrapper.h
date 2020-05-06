#pragma once

#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include "DepdendentFalse.h"

#include <algorithm>

namespace py = pybind11;

namespace ZividPython
{
    namespace Detail
    {
        // Need this indirection to work around an ICE in MSVC
        template<typename Target, typename Source>
        auto getHelper(const Source &s)
        {
            return s.template get<Target>();
        }

        template<bool isRoot, typename Dest, typename Target>
        void wrapDataModel(Dest &dest, const Target &target)
        {
            py::class_<Target> pyClass{ dest, Target::name, py::dynamic_attr() };

            pyClass.def(py::init())
                .def("__repr__", &Target::toString)
                .def("to_string", &Target::toString)
                .def("set_from_string", 
                py::overload_cast<const std::string &>(&Target::setFromString), 
                py::arg("string_value"))
                .def(py::self == py::self) // NOLINT
                .def(py::self != py::self) // NOLINT
                .def_readonly_static("node_type", &Target::nodeType)
                .def_readonly_static("name", &Target::name)
                .def_readonly_static("path", &Target::path);

            if constexpr(isRoot)
            {
                //pyClass.def(py::init<const std::string &>(), py::arg("file_name"))
                //    .def("save", &Target::save, py::arg("file_name"))
                //    .def("load", &Target::load, py::arg("file_name")); //TODO: fix når save/load bare tar et argument
                pyClass.def("set_from_string", 
                py::overload_cast<const std::string &, const std::string &>(&Target::setFromString), 
                py::arg("path"),py::arg("string_value"));
            }

            // This is inside out because of bug in MSVC,
            // 'if constexpr' should really be inside the lambda
            if constexpr(Target::nodeType == Zivid::DataModel::NodeType::internal)
            {
                pyClass.def("__bool__", [](const Target & /* value*/) { return true; }); // reconsider bool(iris)
            }
            else if constexpr(Target::nodeType == Zivid::DataModel::NodeType::leafValue)
            {
                pyClass.def("__bool__", [](const Target &value) {
                    return Target{ typename Target::ValueType{} } != value; // NOLINT
                });
            }
            else
            {
                static_assert(DependentFalse<Target>::value, "Target NodeType is unsupported");
            }
            
            if constexpr(Target::nodeType == Zivid::DataModel::NodeType::internal)
            {
                target.forEach([&](const auto &member) {
                    wrapDataModel<false>(pyClass, member);

                    using MemberType = std::remove_const_t<std::remove_reference_t<decltype(member)>>;

                    std::string name{ MemberType::name };
                    std::transform(begin(name), end(name), begin(name), ::tolower);

                    pyClass.def_property(
                        name.c_str(),
                        [](const Target &source) { return Detail::getHelper<MemberType>(source); },
                        [](Target &dest, const MemberType &value) { return dest.set(value);});
                });
            }
            else if constexpr(Target::nodeType == Zivid::DataModel::NodeType::leafValue)
            {
                pyClass.def(py::init<const typename Target::ValueType &>(), py::arg("value"))
                    .def_property_readonly("value", &Target::value);

                if constexpr(!std::is_same_v<typename Target::ValueType, bool>)
                {
                    pyClass.def(py::self > py::self); // NOLINT
                    pyClass.def(py::self < py::self); // NOLINT
                }

                if constexpr(Zivid::DataModel::HasValidRangeConstraint<Target>::value)
                {
                    pyClass.def_property_readonly("valid_range", [](const Target &target) {
                        const auto range = typename Target::Constraints{}.validRange();
                        return std::make_pair(range.min(), range.max());
                    });
                }

                if constexpr(Zivid::DataModel::HasValidValuesConstraint<Target>::value)
                {
                    pyClass.def_property_readonly("valid_values", [](const Target &target) {
                        return typename Target::Constraints{}.validValues();
                    });
                }
                
                if constexpr(Zivid::DataModel::HasValidSizeConstraint<Target>::value)
                {
                    pyClass.def_property_readonly("valid_size", [](const Target &target) {
                        const auto size = typename Target::Constraints{}.validSize();
                        return std::make_pair(size.min(), size.max());
                    });
                }
            }

            else
            {
                static_assert(DependentFalse<Target>::value, "Target NodeType is unsupported");
            }
        }
    } // namespace Detail

    template<typename Dest, typename Target>
    void wrapDataModel(Dest &dest, const Target &target)
    {
        Detail::wrapDataModel<true>(dest, target);
    }
} // namespace ZividPython
