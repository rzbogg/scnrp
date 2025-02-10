from command import create_command
import sys


def show_help():
    print('usage: scnrp command parameters...')

if len(sys.argv) < 2:
    show_help()
else:
    command = create_command(sys.argv[1:])
    print(command.run())
