"""File camera capture sample."""
from zivid import Application, Settings


def _main():
    app = Application()
    camera = app.create_file_camera("MiscObjects.zdf")

    settings = Settings(frames=[Settings.Frame(iris=22,)])

    with camera.capture(settings) as frame:
        frame.save("results.zdf")


if __name__ == "__main__":
    _main()
