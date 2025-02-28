from scnrp.command import run_command
from scnrp.cli import arg_parser
from scnrp.exception import UserError

def main():
    args = arg_parser.parse_args()
    try:
        command_result = run_command(args)
        print(command_result)
    except UserError as e:
        print(e)
    except KeyboardInterrupt:
        print('interuppted')

if __name__ == "__main__":
    main()
