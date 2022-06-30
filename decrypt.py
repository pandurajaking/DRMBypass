import os
import subprocess


def decrypt(in_path: str, out_path: str, key_dict: dict):
    binary_location = os.getenv('MP4DECRYPT_PATH')

    p = subprocess.run([
        binary_location, "--key", f"{key_dict.get('KID')}:{key_dict.get('Key')}", f"{in_path}", f"{out_path}"
    ], capture_output=True)

    print(
        f"Subproccess is worked out with the following arguments:\n {p.args}")

    if(p.returncode != 0):
        return False
    else:
        return True
