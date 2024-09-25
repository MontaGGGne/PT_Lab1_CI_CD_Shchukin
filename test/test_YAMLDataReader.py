# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.YAMLDataReader import YAMLDataReader


class TestYAMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        yaml_content = """
        - имя: Иванов Иван Иванович
          математика: 67
          литература: 100
        - имя: Петров Петр Петрович
          математика: 78
          физика: 87
        """

        data = {
            "Иванов Иван Иванович": [
                ("математика", 67), ("литература", 100)
            ],
            "Петров Петр Петрович": [
                ("математика", 78), ("физика", 87)
            ]
        }
        return yaml_content, data

    @pytest.fixture()
    def filepath_and_data(self, file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.yaml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = YAMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
