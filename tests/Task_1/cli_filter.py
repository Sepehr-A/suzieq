import argparse
import os
import pandas as pd


def filter_by_osstring(dataframe: pd.DataFrame, filter_value: str, partial_match: bool) -> pd.DataFrame:
    if partial_match:
        return dataframe[dataframe['osString'].str.contains(filter_value, na=False)]
    else:
        return dataframe[dataframe['osString'] == filter_value]


def open_file(file_path: str) -> pd.DataFrame:
    if file_path.endswith('.parquet'):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")
        return pd.read_parquet(file_path)
    else:
        raise ValueError("Unsupported file format")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filter the table by osString')
    parser.add_argument('--filepath', type=str, help='Path to the Parquet file containing the table data',
                        required=True)
    parser.add_argument('--filter-value', type=str, help='The osString value to filter by')
    parser.add_argument('--partial-match', action="store_true",
                        help="Enable partial matching for filter value, default is exact match")

    args = parser.parse_args()

    try:
        table = open_file(args.filepath)
        if args.filter_value:
            table = filter_by_osstring(table, args.filter_value, args.partial_match)

        print(table.to_markdown(tablefmt="pretty"))
    except Exception as e:
        print(f"Error: {e}")
