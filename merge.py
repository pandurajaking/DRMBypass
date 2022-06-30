import os
import subprocess


def merge(in_path1: str, in_path2: str, out_path: str):
    binary_location = os.getenv('FFMPEG_PATH')

    p = subprocess.run([
        binary_location, "-i", in_path1, "-i", in_path2, "-c:v", "copy", "-c:a", "copy", out_path
    ], capture_output=True)

    print(
        f"Subproccess is worked out with the following arguments:\n {p.args}")

    if(p.returncode != 0):
        return False
    else:
        return True
