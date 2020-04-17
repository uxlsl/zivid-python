#pragma once

#include <Zivid/CaptureAssistant.h>

#include <pybind11/pybind11.h>

namespace ZividPython
{
    void wrapEnum(pybind11::enum_<Zivid::CaptureAssistant::SuggestSettingsParameters::AmbientLightFrequency> pyEnum);
} // namespace ZividPython
