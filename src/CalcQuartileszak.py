# -*- coding: utf-8 -*-
import statistics
from Types import DataType, CalcType
from ValCalc import ValCalc


class CalcQuartilesZakh(ValCalc):
    def __init__(self, data: DataType) -> None:
        super().__init__(data)

    def calc(self) -> CalcType:
        for key, value in self.data.items():
            sub_vals = [t[1] for t in value]
            self.rating[key] = statistics.mean(sub_vals)
        quants = statistics.quantiles(self.rating.values())
        r_qts = [round(q, 1) for q in quants]
        print(r_qts)
        for key, value in list(self.rating.items()):
            if value < r_qts[-1]:
                del self.rating[key]
        return self.rating
