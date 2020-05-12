#include <ZividPython/ReleasablePointCloud.h>

#include <pybind11/pybind11.h>

namespace py = pybind11;

#define IS_SAME_MEMBER(T1, T2, m)                                                                                      \
    (std::is_same_v<decltype(T1::m), decltype(T2::m)> && offsetof(T1, m) == offsetof(T2, m))

namespace
{
#pragma pack(push)
    struct DataType
    {
        float x, y, z;
        float contrast;
        uint32_t b, g, r, a;
    };
#pragma pack(pop)

    py::buffer_info makeBufferInfo(ZividPython::ReleasablePointCloud &pointCloud)
    {
        const auto data = pointCloud.copyData();


        using NativeDataType = decltype(data);

        static_assert(sizeof(NativeDataType) == sizeof(DataType), "Unexpected point cloud format");
//        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, x), "Unexpected point cloud format");
//        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, y), "Unexpected point cloud format");
//        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, z), "Unexpected point cloud format");
//        static_assert(IS_SAME_MEMBER(NativeDataType, DataType, contrast), "Unexpected point cloud format");
//        static_assert(offsetof(NativeDataType, rgba) == offsetof(DataType, b), "Unexpected point cloud format");
//        static_assert(sizeof(NativeDataType::rgba)
//                          == sizeof(DataType::r) + sizeof(DataType::g) + sizeof(DataType::b) + sizeof(DataType::a),
//                      "Unexpected point cloud format");
//
//        return py::buffer_info{ data,
//                                sizeof(DataType),
//                                py::format_descriptor<DataType>::format(),
//                                2,
//                                { pointCloud.height(), pointCloud.width() },
//                                { sizeof(DataType) * pointCloud.width(), sizeof(DataType) } };
auto my_vec = std::vector<int>{};
return py::buffer_info{ my_vec.data(),
                                sizeof(int),
                                py::format_descriptor<int>::format(),
                                2,
                                {0, 0 },
                                {sizeof(int), sizeof(int)} };
                                //{ sizeof(DataType) * pointCloud.width(), sizeof(DataType) } };
    }
} // namespace

namespace ZividPython
{
    void wrapClass(pybind11::class_<ReleasablePointCloud> pyClass)
    {
        PYBIND11_NUMPY_DTYPE(DataType, x, y, z, contrast, b, g, r, a);

        pyClass.def(py::init<>())
            .def_buffer(makeBufferInfo)
            .def("width", &ReleasablePointCloud::width)
            .def("height", &ReleasablePointCloud::height);
    }
} // namespace ZividPython
