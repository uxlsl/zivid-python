#include <ZividPython/Matrix.h>
#include <ZividPython/Calibration/MultiCamera.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace ZividPython
{
    void wrapClass(pybind11::class_<Zivid::Calibration::MultiCameraResidual> pyClass)
    {
        pyClass.def(py::init<float>(), py::arg("translation"))
        .def("translation", &Zivid::Calibration::MultiCameraResidual::translation);
    }
    void wrapClass(pybind11::class_<Zivid::Calibration::MultiCameraOutput> pyClass)
    {
        pyClass.def(py::init([](const std::vector<Eigen::Matrix<float, 4, 4, Eigen::RowMajor>> transforms, const std::vector<Zivid::Calibration::MultiCameraResidual> residuals) {
            auto converted_transforms = std::vector<Zivid::Matrix<float, 4, 4>>();
            for(const auto &transform: transforms)
            {
                converted_transforms.emplace_back(Conversion::toCpp(transform));
            }
            return std::make_unique<Zivid::Calibration::MultiCameraOutput>(converted_transforms, residuals);
        }));
    }
} // namespace ZividPython
