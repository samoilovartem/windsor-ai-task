from pydantic import BaseSettings


class DataFetcherConfig(BaseSettings):
    gdrive_base_url: str = 'https://drive.google.com/uc?id='
    output_file_name: str = 'test_task_data.csv'
    json_indent_level: int = 4
    json_orient_format: str = 'records'


data_fetcher_config = DataFetcherConfig()
