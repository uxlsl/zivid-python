class MultiCameraResidual:
    def __init__(self, translation):
        pass

    def translation(self):
        pass

    def __str__(self):
        pass


class MultiCameraOutput:
    def __init__(self, transforms, residuals):
        pass

    def valid(self):
        pass

    def __bool__(self):
        pass

    def transforms(self):
        pass

    def residuals(self):
        pass

    def __str__(self):
        pass


def calibrate_multi_camera(detection_results):
    pass

import zivid.calibration.hand_eye
zivid.calibration.calibrate_eye_in_hand

from zivid.calibration import calibrate_eye_in_hand
calibrate_eye_in_hand





# namespace Zivid
# {
#     namespace Calibration
#     {
#         /// <summary>
#         /// Representation of the estimated errors of a multi-camera calibration
#         /// </summary>
#         class MultiCameraResidual
#         {
#         public:
#             /// <summary>Constructs a multi-camera residual instance.</summary>
#             /// <param name="translation">Average overlap error in millimeters.</param>
#             ZIVID_CORE_EXPORT MultiCameraResidual(float translation);
#
#             /// <summary>Get the average overlap error</summary>
#             /// <returns>Average overlap error in millimeters.</returns>
#             ZIVID_CORE_EXPORT float translation() const;
#
#             /// <summary>Get string representation of the multi-camera residual</summary>
#             /// <returns>Multi-camera residual as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             float m_translation;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const MultiCameraResidual &residual);
#
#         /// <summary>
#         /// The results from a multi-camera calibration process
#         /// </summary>
#         class MultiCameraOutput
#         {
#         public:
#             /// <summary>Constructs a MultiCameraOutput instance.</summary>
#             /// <param name="transforms">Vector of transforms for each camera.</param>
#             /// <param name="residuals">Vector of multi-camera residuals for each camera.</param>
#             ZIVID_CORE_EXPORT MultiCameraOutput(const std::vector<Matrix4x4> &transforms,
#                                                 const std::vector<MultiCameraResidual> &residuals);
#
#             /// <summary>Test if MultiCameraOutput is valid.</summary>
#             /// <returns>True if MultiCameraOutput is valid.</returns>
#             ZIVID_CORE_EXPORT bool valid() const;
#
#             /// <summary>Test if MultiCameraOutput is valid.</summary>
#             /// <returns>True if MultiCameraOutput is valid.</returns>
#             ZIVID_CORE_EXPORT explicit operator bool() const;
#
#             /// <summary>Multi-camera calibration transforms.</summary>
#             /// <returns>Vector of affine transformations in the form of 4x4 matrices.</returns>
#             ZIVID_CORE_EXPORT const std::vector<Matrix4x4> &transforms() const;
#
#             /// <summary>Multi-camera calibration residuals.</summary>
#             /// <remarks>
#             /// The residuals provide a measure of the overlap error that can be expected
#             /// when transforming point clouds to the coordinate system of the primary camera.
#             ///
#             /// The residual for each camera is calculated by applying each transform to the
#             /// corresponding feature points used in the calibration process. The points are
#             /// then compared with the feature points of the primary camera, and the average
#             /// error between the two is calculated. By definition the first residual will
#             /// therefore always be zero.
#             /// </remarks>
#             /// <returns>Vector of multi-camera calibration residuals.</returns>
#             ZIVID_CORE_EXPORT const std::vector<MultiCameraResidual> &residuals() const;
#
#             /// <summary>Get string representation of the multi-camera calibration output</summary>
#             /// <returns>Calibration output as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             std::vector<Matrix4x4> m_transforms;
#             std::vector<MultiCameraResidual> m_residuals;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const MultiCameraOutput &multiCameraOutput);
#
#         /// <summary>Performs multi-camera calibration.</summary>
#         /// <remarks>
#         /// Multi-camera calibration is used in a multi-camera setup to find the
#         /// pose of secondary cameras in the frame of a designated primary camera,
#         /// e.g. to combine points clouds into a single frame of reference.
#         ///
#         /// The input is generated by imaging the same checkerboard from each camera
#         /// and inserting the resulting point clouds into <see cref="detectFeaturePoints" />.
#         /// Add the resulting <see cref="DetectionResult" /> objects to a vector with the first
#         /// element corresponding to the primary camera.
#         ///
#         /// The returned object contains a vector of transforms, which provides the pose of
#         /// camera[i] in the frame of camera[0]. Apply transform[i] to the points from
#         /// camera[i] to get the same points in the frame of camera[0]. The returned object
#         /// also contains a vector of residuals corresponding to each transform.
#         /// </remarks>
#         /// <param name="detectionResults">Vector of DetectionResult instances.</param>
#         /// <returns>A <see cref="MultiCameraOutput" /> instance.</returns>
#         ZIVID_CORE_EXPORT MultiCameraOutput calibrateMultiCamera(const std::vector<DetectionResult> &detectionResults);
#     } // namespace Calibration
# } // namespace Zivid
#
