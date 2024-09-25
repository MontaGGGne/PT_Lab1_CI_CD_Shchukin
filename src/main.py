# -*- coding: utf-8 -*-
import argparse
import sys
import os
import pathlib
from CalcRating import CalcRating
from CalcQuartiles import CalcQuartiles
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader
from YAMLDataReader import YAMLDataReader


def get_path_from_arguments(args) -> str:
    # ggg
    parser = argparse.ArgumentParser()
    group_methods = parser.add_argument_group('method')
    group_methods.add_argument("-p", dest="path", type=str,
                               required=True,
                               help="Path to datafile")
    group_types = parser.add_argument_group('type')
    group_types.add_argument("-t", dest="type", type=str,
                             required=True,
                             help="File type")
    args_prms = parser.parse_args(args)
    return args_prms


def main():
    args = get_path_from_arguments(sys.argv[1:])
    if args.type == 'txt':
        reader = TextDataReader()
    elif args.type == 'xml':
        reader = XMLDataReader()
    elif args.type == 'yaml':
        reader = YAMLDataReader()
    else:
        print("[ERROR] Error -type argument")
        exit(0)
    print(args.path)
    students = reader.read(args.path)
    print("Students: ", students)
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    quart = CalcQuartiles(students).calc()
    print("Second quartile: ", quart)


if __name__ == "__main__":
    main()
