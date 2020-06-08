class HandEyeInput:
    def __init__(self, robot_pose, detection_result):
        pass

    def pose(self):
        pass

    def detection_result(self):
        pass

    def __str__(self):
        pass


class HandEyeResidual:
    def __init__(self, rotation, translation):
        pass

    def rotation(self):
        pass

    def translation(self):
        pass

    def __str__(self):
        pass


class HandEyeOutput:
    def __init__(self, transform, residuals):
        pass

    def valid(self):
        pass

    def __bool__(self):
        pass

    def transform(self):
        pass

    def residuals(self):
        pass

    def __str__(self):
        pass


def calibrate_eye_in_hand(input):
    pass


def calibrate_eye_to_hand(input):
    pass


# namespace Zivid
# {
#     namespace Calibration
#     {
#         /// <summary>
#         /// Binds together a robot pose and the detection result acquired from the pose
#         /// </summary>
#         class HandEyeInput
#         {
#         public:
#             /// <summary>Constructs a HandEyeInput instance.</summary>
#             /// <param name="robotPose">Robot pose for detected feature points.</param>
#             /// <param name="detectionResult">Feature detection result.</param>
#             ZIVID_CORE_EXPORT HandEyeInput(const Pose &robotPose, const DetectionResult &detectionResult);
#
#             /// <summary>Robot pose for detected feature points.</summary>
#             /// <returns>Robot pose.</returns>
#             ZIVID_CORE_EXPORT const Pose &robotPose() const;
#
#             /// <summary>Feature detection result.</summary>
#             /// <returns>Detection result.</returns>
#             ZIVID_CORE_EXPORT const DetectionResult &detectionResult() const;
#
#             /// <summary>Get string representation of the hand-eye calibration input</summary>
#             /// <returns>Hand-eye calibration input as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             Pose m_robotPose;
#             DetectionResult m_result;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const HandEyeInput &handEyeInput);
#
#         /// <summary>
#         /// Representaton of the estimated errors of a calibrated hand-eye transform
#         /// </summary>
#         class HandEyeResidual
#         {
#         public:
#             /// <summary>Constructs a hand-eye residual instance.</summary>
#             /// <param name="rotation">Residual for rotation part.</param>
#             /// <param name="translation">Residual for translation part.</param>
#             ZIVID_CORE_EXPORT HandEyeResidual(float rotation, float translation);
#
#             /// <summary>Rotational residual in degrees.</summary>
#             /// <returns>Rotational residual.</returns>
#             ZIVID_CORE_EXPORT float rotation() const;
#
#             /// <summary>Translational residual in millimeters.</summary>
#             /// <returns>Translational residual.</returns>
#             ZIVID_CORE_EXPORT float translation() const;
#
#             /// <summary>Get string representation of the hand-eye residual</summary>
#             /// <returns>Hand-eye residual as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             float m_rotation;
#             float m_translation;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const HandEyeResidual &residual);
#
#         /// <summary>
#         /// The hand-eye calibration result containing the computed pose and reprojection errors for all the input poses
#         /// </summary>
#         class HandEyeOutput
#         {
#         public:
#             /// <summary>Constructs a HandEyeOutput instance.</summary>
#             /// <param name="transform">Computed hand-eye calibration transform.</param>
#             /// <param name="residuals">Per pose hand-eye residuals.</param>
#             ZIVID_CORE_EXPORT HandEyeOutput(const Matrix4x4 &transform, const std::vector<HandEyeResidual> &residuals);
#
#             /// <summary>Test if HandEyeOutput is valid.</summary>
#             /// <returns>True if HandEyeOutput is valid.</returns>
#             ZIVID_CORE_EXPORT bool valid() const;
#
#             /// <summary>Test if HandEyeOutput is valid.</summary>
#             /// <returns>True if HandEyeOutput is valid.</returns>
#             ZIVID_CORE_EXPORT explicit operator bool() const;
#
#             /// <summary>Hand-eye transform.</summary>
#             /// <remarks>
#             /// A 4x4 matrix describing hand-eye calibration transform (either eye-in-hand or eye-to-hand).
#             /// An exception is thrown if the result is not valid.
#             /// </remarks>
#             /// <returns>Pose instance.</returns>
#             ZIVID_CORE_EXPORT const Matrix4x4 &transform() const;
#
#             /// <summary>Hand-eye calibration residuals.</summary>
#             /// <remarks>
#             /// Feature points (for each input pose) are transformed into a common frame.
#             /// A rigid transform between feature points and corresponding centroids are
#             /// utilized to compute residuals for rotational and translational parts.
#             /// An exception is thrown if the result is not valid.
#             /// </remarks>
#             /// <returns>Vector of hand-eye calibration residuals.</returns>
#             ZIVID_CORE_EXPORT const std::vector<HandEyeResidual> &residuals() const;
#
#             /// <summary>Get string representation of the hand-eye calibration output</summary>
#             /// <returns>Calibration output as string</returns>
#             ZIVID_CORE_EXPORT std::string toString() const;
#
#         private:
#             Matrix4x4 m_transform;
#             std::vector<HandEyeResidual> m_residuals;
#         };
#
#         /// <summary>Serialize the value to a stream</summary>
#         ZIVID_CORE_EXPORT std::ostream &operator<<(std::ostream &stream, const HandEyeOutput &handEyeOutput);
#
#         /// <summary>Performs eye-in-hand calibration.</summary>
#         /// <remarks>
#         /// The procedure requires feature point sets acquired at the minimum from two poses.
#         /// All the input poses have to be different. The feature point sets cannot be empty.
#         /// All the feature point sets have to have same number of feature points.
#         /// An exception will be thrown if the above requirements are not fulfilled.
#         /// </remarks>
#         /// <param name="input">Vector of HandEyeInput instances.</param>
#         /// <returns>Instance of HandEyeOutput.</returns>
#         ZIVID_CORE_EXPORT HandEyeOutput calibrateEyeInHand(const std::vector<HandEyeInput> &input);
#
#         /// <summary>Performs eye-to-hand calibration.</summary>
#         /// <remarks>
#         /// The procedure requires feature point sets acquired at the minimum from two poses.
#         /// All the input poses have to be different. The feature point sets cannot be empty.
#         /// All the feature points have to have same number of elements.
#         /// An exception will be thrown if the above requirements are not fulfilled.
#         /// </remarks>
#         /// <param name="input">Vector of HandEyeInput instances.</param>
#         /// <returns>Instance of HandEyeOutput.</returns>
#         ZIVID_CORE_EXPORT HandEyeOutput calibrateEyeToHand(const std::vector<HandEyeInput> &input);
#
#     } // namespace Calibration
# } // namespace Zivid
#
