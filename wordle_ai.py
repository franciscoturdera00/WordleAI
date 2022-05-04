#!/usr/bin/env python3

from config.arguments_parser import initiate_parser

if __name__ == "__main__":
    arguments = initiate_parser()
    arguments.func(arguments)
