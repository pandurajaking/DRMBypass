import argparse
from dotenv import load_dotenv

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
    args = parser.parse_args()
    if args.url is not None:
        if args.name is not None:
            pipeline(args.url, args.name)
        else:
            pipeline(args.url, "default_name")
    if args.list is not None:
        if args.offset is not None:
            threads(args.list, args.offset)
        else:
            threads(args.list, 0)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
