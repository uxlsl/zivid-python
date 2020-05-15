"""Hand-eye calibration sample."""
import datetime
import code

import numpy as np
import zivid.hand_eye


def _acquire_checkerboard_frame(camera):
    print("Capturing checkerboard image... ")
    settings = Settings(
        frames=[
            Settings.Frame(
                iris=17,
                exposure_time=datetime.timedelta(microseconds=20000),
                gain=1.0,
                filters=Settings.Frame.Filters(
                    outlier=Outlier(enabled=True, threshold=5)
                ),
            )
        ],
        filters = Settings.Filters(Settings.Filters.Gaussian(enabled=True))
    )
    print("OK")
    return camera.capture(settings)


def _enter_robot_pose(index):
    inputted = input(
        "Enter pose with id={} (a line with 16 space separated values describing 4x4 row-major matrix):".format(
            index
        )
    )
    elements = inputted.split(maxsplit=15)
    data = np.array(elements, dtype=np.float64).reshape((4, 4))
    robot_pose = zivid.hand_eye.Pose(data)
    print("The following pose was entered:\n{}".format(robot_pose))
    return robot_pose


def _main():
    app = zivid.Application()
    camera = app.connect_camera()

    current_pose_id = 0
    calibration_inputs = list()
    calibrate = False

    while not calibrate:
        command = input(
            "Enter command, p (to add robot pose) or c (to perform calibration):"
        ).strip()
        if command == "p":
            try:
                robot_pose = _enter_robot_pose(current_pose_id)

                frame = _acquire_checkerboard_frame(camera)

                print("Detecting checkerboard square centers... ")
                result = zivid.hand_eye.detect_feature_points(frame.get_point_cloud())

                if result:
                    print("OK")
                    res = zivid.hand_eye.CalibrationInput(robot_pose, result)
                    calibration_inputs.append(res)
                    current_pose_id += 1
                else:
                    print("FAILED")
            except ValueError as ex:
                print(ex)
        elif command == "c":
            calibrate = True
        else:
            print("Unknown command '{}'".format(command))

    print("Performing hand-eye calibration...")
    calibration_result = zivid.hand_eye.calibrate_eye_to_hand(calibration_inputs)
    code.interact(local=locals())
    if calibration_result:
        print("OK")
        print("Result:\n{}".format(calibration_result))
    else:
        print("FAILED")


if __name__ == "__main__":
    _main()
