# -*- coding: utf-8 -*-
from DataReader import DataReader
from Types import DataType, YamlType
import yaml


class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        all_info: YamlType = []
        with open(path, encoding='utf-8') as stream:
            all_info = yaml.safe_load(stream)
        for student in all_info:
            name = student['имя']
            del student['имя']
            tuple_list = [(k, v) for k, v in student.items()]
            self.students[name] = tuple_list
        return self.students
