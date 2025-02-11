from scnrp.command import create_command
from scnrp.cli import arg_parser
import sys


def show_help():
    print('usage: scnrp command parameters...')

def main():
    args = arg_parser.parse_args()
    command = create_command(args)
    print(command.run())

main()
