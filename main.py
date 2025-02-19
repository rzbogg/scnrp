from scnrp.command import run_command
from scnrp.cli import arg_parser
import sys


def show_help():
    print('usage: scnrp command parameters...')

def main():
    args = arg_parser.parse_args()
    command_result = run_command(args)
    print(command_result)

main()
