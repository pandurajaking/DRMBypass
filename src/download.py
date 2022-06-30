import os
import subprocess


def download(url: str, name: str):
    binary_location = os.getenv('N_M3U8DL_PATH')
    workdir_path = os.getenv('WORKDIR_PATH')
    p = subprocess.run([
        binary_location, f"{url}", "--saveName", f"{name}", "--workDir", f"{workdir_path}", "--enableDelAfterDone"
    ], capture_output=True)

    print(f"Subproccess is worked out with the following arguments:\n {p.args}")
    if ('Task Done' in str(p.stdout)):
        return str(os.path.join(workdir_path, name))
    else:
        return None
