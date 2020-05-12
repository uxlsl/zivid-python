"""Capture sample 2D."""
import datetime
from zivid import Application, Settings2D


def _main():
    app = Application()
    camera = app.connect_camera()

    settings_2d = Settings2D(
        frames=Settings2D.Frame(
            iris=35, exposure_time=datetime.timedelta(microseconds=10000), gain=1
        )
    )

    with camera.capture_2d(settings_2d) as frame_2d:
        image = frame_2d.image()
        image.save("result.png")


if __name__ == "__main__":
    _main()
