import argparse
import pandas as pd
import os
from PingResult import validate_ping_data


def read_file(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise Exception(f"File '{file_path}' not found.")

    if file_path.endswith('.csv'):
        ping_table = pd.read_csv(file_path)
    elif file_path.endswith('.parquet'):
        ping_table = pd.read_parquet(file_path)
    else:
        raise Exception("Invalid file format. Please provide a .csv or .parquet file")

    validated_data = validate_ping_data(ping_table.to_dict(orient='records'))
    return pd.DataFrame(validated_data)


def display_ping_results(file_path: str, filter: str = None):
    try:
        ping_table = read_file(file_path)
        if ping_table.empty:
            return

        if filter:
            filter = filter.strip()
            if ':' in filter:
                filter_column, filter_value = filter.split(':', 1)
                filter_column = filter_column.strip()
                filter_value = filter_value.strip()
                if filter_column in ping_table.columns:
                    ping_table = ping_table[ping_table[filter_column] == filter_value]
                    if ping_table.empty:
                        raise Exception(f"No ping results found for '{filter}' filter.")
                else:
                    raise Exception(f"Column '{filter_column}' not found in the data.")
            else:
                raise Exception("Filter format is incorrect. Please use 'column:value' format.")

        print(
            f"Displaying ping results from '{file_path}' file with filter '{filter}'" if filter else f"Displaying ping results from '{file_path}' file.")

        print(ping_table.to_markdown(tablefmt="pretty"))
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Display Ping Results")
    parser.add_argument('--file-path', type=str, required=True,
                        help="Path to the .csv or .parquet file containing ping results.")
    parser.add_argument('--filter', type=str,
                        help="Filter results using column:value format (e.g., source_name:ansible-01)")

    args = parser.parse_args()

    display_ping_results(args.file_path, args.filter)
