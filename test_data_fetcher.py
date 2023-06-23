import pandas as pd
import pytest

from run import DataFetcher, parser


@pytest.fixture
def fetcher():
    return DataFetcher(file_id='1zLdEcpzCp357s3Rse112Lch9EMUWzMLE')


def test_read_csv_file(fetcher):
    fetcher.output_file_name = 'sample.csv'
    fields = 'clocks,spend'
    result = fetcher.read_csv_file(fields)
    assert isinstance(result, pd.DataFrame)


def test_read_nonexistent_csv_file(fetcher):
    fetcher.output_file_name = 'nonexistent.csv'
    fields = 'column1,column2'
    result = fetcher.read_csv_file(fields)
    assert result.empty


def test_convert_to_json(fetcher):
    sample_data = pd.DataFrame({'column1': ['value1'], 'column2': ['value2']})
    result = fetcher.convert_csv_data_to_dict(sample_data)
    assert result == [{'column1': 'value1', 'column2': 'value2'}]


def test_convert_empty_dataframe_to_json(fetcher):
    empty_data = pd.DataFrame()
    result = fetcher.convert_csv_data_to_dict(empty_data)
    assert result == []


def test_argument_parsing():
    test_args = ['--fields', 'field1,field2,field3']
    args = parser.parse_args(test_args)
    assert args.fields == 'field1,field2,field3'
