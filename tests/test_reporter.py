"""Tests for the console DataFrame summary."""
import io
import unittest
from contextlib import redirect_stdout

import pandas as pd

from src.reporter import DataFrameReporter


class DataFrameReporterTests(unittest.TestCase):
    def report(self, frame, **kwargs):
        output = io.StringIO()
        with redirect_stdout(output):
            DataFrameReporter(**kwargs).show_report(frame, "Отчёт:")
        return output.getvalue()

    def test_empty_table_does_not_crash(self):
        result = self.report(pd.DataFrame({"amount": pd.Series(dtype="float64")}))
        self.assertIn("Количество строк: 0", result)
        self.assertIn("Доля дубликатов: 0.00%", result)
        self.assertIn("Описательная статистика: нет данных", result)
        self.assertIn("Доля пропусков: 0.00000", result)

    def test_table_without_columns_does_not_crash(self):
        result = self.report(pd.DataFrame())
        self.assertIn("Количество столбцов: 0", result)
        self.assertIn("Описательная статистика: нет данных", result)

    def test_duplicates_and_missing_values(self):
        frame = pd.DataFrame({"value": [1.0, 1.0, None]})
        result = self.report(frame, float_format=".2%", percent_format=".1%")
        self.assertIn("Количество дубликатов: 1", result)
        self.assertIn("Доля дубликатов: 33.3%", result)
        self.assertIn("Количество пропусков: 1", result)
        self.assertIn("Доля пропусков: 33.33%", result)


if __name__ == "__main__":
    unittest.main()
