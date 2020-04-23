#include <ZividPython/AmbientLightFrequency.h>
#include <ZividPython/CaptureAssistant.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

namespace ZividPython
{
    void wrapEnum(pybind11::enum_<Zivid::CaptureAssistant::SuggestSettingsParameters::AmbientLightFrequency::ValueType> pyEnum)
    {
        pyEnum.value("hz50", Zivid::CaptureAssistant::SuggestSettingsParameters::AmbientLightFrequency::ValueType::hz50)
            .value("hz60", Zivid::CaptureAssistant::SuggestSettingsParameters::AmbientLightFrequency::ValueType::hz60)
            .value("none", Zivid::CaptureAssistant::SuggestSettingsParameters::AmbientLightFrequency::ValueType::none)
            .export_values();
    }
} // namespace ZividPython
