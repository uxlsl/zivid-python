#include <ZividPython/ReleasableCamera.h>
#include <ZividPython/ReleasableFrame.h>

#include <pybind11/pybind11.h>

#include <variant>
#include <vector>

namespace py = pybind11;

namespace ZividPython
{
    void wrapClass(pybind11::class_<ReleasableCamera> pyClass)
    {
        pyClass.def(py::init())
            .def(py::self == py::self) // NOLINT
            .def(py::self != py::self) // NOLINT
            .def("disconnect", &ReleasableCamera::disconnect)
            .def("capture", &ReleasableCamera::capture, py::arg("settings"))
            .def("capture_2d", &ReleasableCamera::capture2D, py::arg("settings_2d") = Zivid::Settings2D{})
            .def_property_readonly("state", &ReleasableCamera::state)
            .def_property_readonly("info", &ReleasableCamera::info)
            .def("write_user_data", &ReleasableCamera::writeUserData)
            .def_property_readonly("user_data", &ReleasableCamera::userData);
    }
} // namespace ZividPython
