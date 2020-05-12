"""HDR capture sample."""
from zivid import Application, Settings


def _main():
    app = Application()
    camera = app.connect_camera()

    settings = Settings(frames=[Settings.Frame(iris=iris) for iris in (14, 21, 35)])
    with camera.capture(settings) as hdr_frame:
        hdr_frame.save("result.zdf")


if __name__ == "__main__":
    _main()
