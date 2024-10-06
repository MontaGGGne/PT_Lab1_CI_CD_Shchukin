# -*- coding: utf-8 -*-
from Types import DataType, CalcType
from ValCalc import ValCalc


class CalcRating(ValCalc):
    def __init__(self, data: DataType) -> None:
        super().__init__(data)

    def calc(self) -> CalcType:
        for key in self.data:
            self.rating[key] = 0.0
            for subject in self.data[key]:
                self.rating[key] += subject[1]
            self.rating[key] /= len(self.data[key])
        return self.rating
