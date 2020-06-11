#include <Zivid/Calibration/HandEye.h>
#include <Zivid/Calibration/Detector.h>
#include <Zivid/Calibration/Pose.h>
#include <Zivid/PointCloud.h>

#include <ZividPython/Calibration/Calibrate.h>
#include <ZividPython/Calibration/CalibrationResidual.h>
#include <ZividPython/Calibration/Detector.h>
#include <ZividPython/Calibration/Pose.h>
#include <ZividPython/ReleasablePointCloud.h>
#include <ZividPython/Wrappers.h>

#include <pybind11/pybind11.h>

#include <vector>

namespace ZividPython::Calibration
{
    void wrapAsSubmodule(pybind11::module &dest)
    {
        using namespace Zivid::Calibration;

        ZIVID_PYTHON_WRAP_CLASS(dest, Pose);
        ZIVID_PYTHON_WRAP_CLASS(dest, HandEyeOutput);
        ZIVID_PYTHON_WRAP_CLASS(dest, HandEyeInput);
        ZIVID_PYTHON_WRAP_CLASS(dest, DetectionResult);
        ZIVID_PYTHON_WRAP_CLASS(dest, HandEyeResidual);

        dest.def("detect_feature_points",
                 [](const ReleasablePointCloud &releasablePointCloud) {
                     return Zivid::Calibration::detectFeaturePoints(releasablePointCloud.impl());
                 })
            .def("calibrate_eye_in_hand", &Zivid::Calibration::calibrateEyeInHand)
            .def("calibrate_eye_to_hand", &Zivid::Calibration::calibrateEyeToHand);
    }
} // namespace ZividPython::Calibration