#!/usr/bin/env python3
import json
from argparse import ArgumentParser

import gdown
import pandas as pd
from loguru import logger

from config import DataFetcherConfig, data_fetcher_config

parser = ArgumentParser()
parser.add_argument(
    '--fields',
    type=str,
    help='fields to be fetched from CSV file (field_1,field_2,field_3, etc.)',
)


class DataFetcher:
    """
    DataFetcher class to download data from Google Drive, read CSV file, and convert it to JSON.
    """

    def __init__(
        self,
        file_id: str,
        output_file_name: str = data_fetcher_config.output_file_name,
        config: DataFetcherConfig = data_fetcher_config,
    ):
        """
        Initialize DataFetcher with file id, output file name, and configuration.
        """
        self.file_id = file_id
        self.output_file_name = output_file_name
        self.config = config

    def download_file_from_google_drive(self) -> None:
        """
        Download the file from Google Drive using the file id.
        """
        try:
            gdown.download(
                f'{self.config.gdrive_base_url}{self.file_id}',
                self.output_file_name,
                quiet=self.config.gdown_is_quiet,
            )
        except Exception as e:
            logger.warning(f'Error occurred while downloading the file: {e}')

    def read_csv_file(self, fields: str) -> pd.DataFrame:
        """
        Read the downloaded CSV file using the specified fields.
        """
        try:
            csv_data = pd.read_csv(self.output_file_name, usecols=fields.split(','))
            return csv_data
        except Exception as e:
            logger.warning(f'Error occurred while reading the CSV file: {e}')
            return pd.DataFrame()

    def convert_csv_data_to_dict(self, csv_data: pd.DataFrame) -> dict:
        """
        Convert the read CSV data to dictionary.
        """
        try:
            dict_data = csv_data.to_dict(orient=self.config.json_orient_format)
            return dict_data
        except Exception as e:
            logger.warning(
                f'Error occurred while converting dataframe to dictionary: {e}'
            )
            return {}

    def fetch_data(self, fields: str) -> dict:
        """
        Fetch data by downloading the file, reading CSV, and converting it to JSON.
        """
        self.download_file_from_google_drive()
        csv_data = self.read_csv_file(fields)
        if not csv_data.empty:
            return self.convert_csv_data_to_dict(csv_data)
        else:
            return {}


if __name__ == '__main__':
    args = parser.parse_args()
    data_fetcher = DataFetcher(file_id='1zLdEcpzCp357s3Rse112Lch9EMUWzMLE')
    data = data_fetcher.fetch_data(args.fields)
    if data:
        logger.info(
            json.dumps({'data': data}, indent=data_fetcher_config.json_indent_level)
        )
