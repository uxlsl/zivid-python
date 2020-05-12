"""Capture sample."""
import datetime
from zivid import Application, Settings


def _main():
    app = Application()
    camera = app.connect_camera()

    settings = Settings(
        frames=[
            Settings.Frame(
                iris=22,
                exposure_time=datetime.timedelta(microseconds=8333),
                filters=Settings.Frame.Filters(
                    outlier=Outlier(enabled=True, threshold=5)
                ),
            )
        ]
    )

    with camera.capture(settings) as frame:
        frame.save("result.zdf")


if __name__ == "__main__":
    _main()
