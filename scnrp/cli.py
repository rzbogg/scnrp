"""
    Parsing and managing interaction with user
    provided data
"""

import argparse


arg_parser = argparse.ArgumentParser(prog='scnrp',description='an xrp ledger explorer')
command_parser = arg_parser.add_subparsers(title='command',dest='command',required=True,description='main command to run')
cmd_parsers = {}


def argument(*names_or_flags,action=None):
    def inner(cmd_cls):
        name = cmd_cls.__name__.lower()
        parser = cmd_parsers[name]
        parser.add_argument(*names_or_flags,action=action)
        return cmd_cls
    return inner


def command(description,*arg,**kwargs):
    def inner(cmd_cls):
        name = cmd_cls.__name__.lower()
        parser = command_parser.add_parser(name,description=description)
        cmd_parsers[name] = parser
        return cmd_cls
    return inner
