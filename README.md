# DrmBypass

## Description
Utility downloads and decrypts DRM protected media content.

## Requirements
1. Download listed binaries:
   - mp4decrypt from Bento4-SDK
   - Chrome x64 with an old widevinecdm lib.
   - Patched [widevine-l3-guesser](https://github.com/vigoroous/widevine-l3-guesser)
   - ffmpeg
   - [N_m3u8DL-CLI](https://github.com/nilaoda/N_m3u8DL-CLI) utility
2. Python 3
3. Poetry

## Usage
1. Clone repo
2. Run ```poetry install```
3. Edit ```.env``` according to your ~~bloatware~~ software location
4. Run utility
```
py main.py --url "https://hosting.com/video/175" --name "file"
```
5. Enjoy proccess

## Note
Ulitity was tested on Windows 10 x64, Chrome 94.0.4606.81 x64 with widevinecdm.dll from 07 oct 2021.

## Legal Disclaimer
This is for educational purposes only. Downloading copyrighted materials from streaming services may violate their Terms of Service. **Use at your own risk.**
