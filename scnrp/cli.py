"""
    Parsing and managing interaction with user
    provided data
"""
"""
    scnrp command
"""
"""
    scnrp account address --last-tx --balance --last-txs
"""
"""
    scnrp tx hash|id --last-tx --balance --last-txs
"""

import argparse

arg_parser = argparse.ArgumentParser(prog='scnrp',description='an xrp ledger explorer')
command_parser = arg_parser.add_subparsers(title='command',dest='command',required=True,description='main command to run')

def command(name,description,*arg,**kwargs):
    def inner(cmd_cls):
        p = command_parser.add_parser(name,description=description)
        arguments = vars(cmd_cls)['ARGUMENTS']
        if arguments:
            for arg in arguments:
                names_or_flags = []
                options = {}
                for item in arg:
                    if isinstance(item,str):
                        names_or_flags.append(item)
                    elif isinstance(item,dict):
                        options = item
                p.add_argument(*names_or_flags,**options)
        return cmd_cls
    return inner
