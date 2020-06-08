class DetectionResult:
    def __init__(self, internal_detection_result):
        pass

    def valid(self):
        pass

    def __bool__(self):
        pass

    def __str__(self):
        pass


def detect_feature_points(point_cloud):
    pass


# namespace Zivid
# {
#     class PointCloud;
#
#     namespace Calibration
#     {
#         /// <summary>
#         /// A result returned by the detectFeaturePoints(...) call
#         /// </summary>
#         class DetectionResult
#         {
#             ZIVID_PIMPL_VALUE_SEMANTICS(DetectionResult, ZIVID_CORE_EXPORT);
#
#         public:
#             /// <summary>Test if DetectionResult is valid.</summary>
#             /// <remarks>
#             /// DetectionResult is valid if all the feature points were detected.
#             /// </remarks>
#             /// <returns>True if DetectionResult is valid.</returns>
#             ZIVID_CORE_EXPORT bool valid() const;
#
#             /// <summary>Test if DetectionResult is valid.</summary>
#             /// <remarks>
#             /// DetectionResult is valid if all the feature points were detected.
#             /// </remarks>
#             /// <returns>True if DetectionResult is valid.</returns>
#             ZIVID_CORE_EXPORT explicit operator bool() const;
#
#             /// <summary>Get string representation of DetectionResult</summary>
#             /// <returns>DetectionResult as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#         };
#
#         /// <summary>Detects feature points from a calibration object in a point cloud.</summary>
#         /// <remarks>
#         /// The functionality is to be exclusively used in combination with Zivid verified checkerboards.
#         /// For further information please visit <a href="https://help.zivid.com">Zivid help page</a>.
#         /// </remarks>
#         /// <param name="cloud">Point cloud from a frame containing an image of a calibration object</param>
#         ZIVID_CORE_EXPORT DetectionResult detectFeaturePoints(const PointCloud &cloud);
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const DetectionResult &result);
#     } // namespace Calibration
# } // namespace Zivid
#
