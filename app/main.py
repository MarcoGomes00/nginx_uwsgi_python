
import argparse
import sys


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World-XPTO"]  # python3


def main(args):
    print('Text :\t{}'.format(args.text))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--url", dest="text",
                        default="default text", help="Write what you want")
    parser.add_argument("-v", "--verbose", dest="verbose", action="count",
                        default=0, help="Verbosity (-v, -vv, etc)")
    arguments = parser.parse_args()
    sys.exit(main(arguments))
