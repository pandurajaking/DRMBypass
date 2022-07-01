import argparse
from dotenv import load_dotenv

from parse_page import Driver
from pipeline import pipeline
from threads import threads

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description='Download and decrypt DRM protected mpeg-dash content')
    parser.add_argument('--url', type=str, help='URL goes here')
    parser.add_argument('--name', type=str, help='set the output file path')
    parser.add_argument('--list', type=str, help='set the URLs list path')
    parser.add_argument(
        '--offset', type=int, help='set offset for resulting filenames')
    parser.add_argument(
        '--speed', type=int, help='Set download speed limit(KB/s); 0 means no limit')
    args = parser.parse_args()

    driver_obj = Driver()
    offset = 0
    max_speed = 0  # no limit
    filename = "default_name"

    if args.offset is not None:
        offset = args.offset
    if args.speed is not None:
        max_speed = args.speed
    if args.name is not None:
        filename = args.name

    if args.url is not None:
        pipeline(driver_obj, args.url, filename, max_speed)
    elif args.list is not None:
        threads(driver_obj, args.list, offset, max_speed)
    else:
        parser.print_help()

    driver_obj.driver.close()
    return 0


if __name__ == '__main__':
    main()
