# -*- coding: utf-8 -*-
from Types import DataType, CalcType
from abc import ABC, abstractmethod


class ValCalc(ABC):
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: CalcType = {}

    @abstractmethod
    def calc(self) -> CalcType:
        pass
