from pathlib import Path

import pandas as pd

from src.reporter import DataFrameReporter


def main():
    data_path = Path(__file__).resolve().parent / 'data' / 'payments.csv'
    if not data_path.is_file():
        raise SystemExit(f'Файл данных не найден: {data_path}. Поместите payments.csv в папку data/.')
    data = pd.read_csv(data_path)

    reporter_1 = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
    reporter_2 = DataFrameReporter(float_format='0.03f', percent_format='0.01%', include_all=True)

    reporter_1.show_report(data, 'Отчёт в формате 1:')
    print()
    reporter_2.show_report(data, 'Отчёт в формате 2:')


if __name__ == '__main__':
    main()
