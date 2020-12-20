from pathlib import Path


def _get_expected_artifacts():
    artifacts_file = Path(__file__).resolve().parent / "expected-artifacts.txt"
    artifacts = artifacts_file.read_text().splitlines()
    artifacts.sort()
    version_file = Path(__file__).resolve().parent / "expected-version.txt"
    version = version_file.read_text().strip()
    return [artifact.format(version=version) for artifact in artifacts]


def _get_present_artifacts():
    artifacts_dir = Path(__file__).resolve().parents[2] / "dist"
    artifacts = [file_path.name for file_path in artifacts_dir.glob("*")]
    artifacts.sort()
    return artifacts


def _main():
    present_artifacts = _get_present_artifacts()
    print("Present artifacts:\n  " + "\n  ".join(present_artifacts))
    expected_artifacts = _get_expected_artifacts()
    print("Expected artifacts:\n  " + "\n  ".join(expected_artifacts))

    assert present_artifacts == expected_artifacts


if __name__ == "__main__":
    _main()
