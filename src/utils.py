import os
import subprocess


def download(url: str, name: str, max_speed: int):
    binary_location = os.getenv('N_M3U8DL_PATH')
    workdir_path = os.getenv('WORKDIR_PATH')
    p = subprocess.run([
        binary_location, f"{url}",
        "--saveName", f"{name}",
        "--workDir", f"{workdir_path}",
        "--maxSpeed", f"{int(max_speed)}",
        "--enableDelAfterDone"
    ], capture_output=True)

    print(
        f"Subproccess is worked out with the following arguments:\n {p.args}")
    if ('Task Done' in str(p.stdout)):
        return str(os.path.join(workdir_path, name))
    else:
        return None


def decrypt(in_path: str, out_path: str, key_dict: dict):
    binary_location = os.getenv('MP4DECRYPT_PATH')

    p = subprocess.run([
        binary_location,
        "--key", f"{key_dict.get('KID')}:{key_dict.get('Key')}",
        f"{in_path}",
        f"{out_path}"
    ], capture_output=True)

    print(
        f"Subproccess is worked out with the following arguments:\n {p.args}")

    if(p.returncode != 0):
        return False
    else:
        return True


def merge(in_path1: str, in_path2: str, out_path: str):
    binary_location = os.getenv('FFMPEG_PATH')

    p = subprocess.run([
        binary_location,
        "-i", in_path1,
        "-i", in_path2,
        "-c:v", "copy",
        "-c:a", "copy",
        out_path
    ], capture_output=True)

    print(
        f"Subproccess is worked out with the following arguments:\n {p.args}")

    if(p.returncode != 0):
        return False
    else:
        return True
