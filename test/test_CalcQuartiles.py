# -*- coding: utf-8 -*-
from src.Types import DataType, CalcType
from src.CalcQuartiles import CalcQuartiles
import pytest


class TestCalcQuartiles:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, CalcType]:
        data = {
            "Иванов Иван Иванович": [
                ("математика", 67), ("литература", 100),
                ("программирование", 91)
            ],
            "Петров Петр Петрович": [
                ("русский язык", 78), ("физика", 67),
                ("информатика", 61)
            ],
            "Путров Путр Путрович": [
                ("русский язык", 80), ("литература", 90),
                ("русский язык", 100)
            ],
            "Патров Патр Патрович": [
                ("русский язык", 20), ("литература", 100),
                ("русский язык", 60)
            ]
        }
        rating_scores: CalcType = {
            'Иванов Иван Иванович': 86
        }
        return data, rating_scores

    def test_init_calc(self, input_data:
                              tuple[DataType, CalcType]) -> None:
        calc_rating = CalcQuartiles(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, CalcType]) -> None:

        rating = CalcQuartiles(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
