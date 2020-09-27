import os
import argparse
from git_demo import data


def main():
    args = parse()
    args.func(args)


def parse():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest="command")
    commands.required = True

    init_parser = commands.add_parser("init")
    init_parser.set_defaults(func=init)

    return parser.parse_args()


def init():
    data.init()
    print(f"Initialized empty git-demo repository in {os.getcwd()}/{data.GIT_DIR}")
