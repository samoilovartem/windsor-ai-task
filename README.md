# Windsor AI Test Task

## Description

A Python project that fetches data from a CSV file hosted on Google Drive and returns it to the user in JSON format. The user can specify the CSV fields they want to fetch.

## Dependencies

This project relies on the following Python libraries:

- `requests` to handle HTTP requests.
- `loguru` for logging and handling errors.
- `pandas` for processing CSV data.
- `gdown` for downloading files from Google Drive.
- `pydantic` for data validation and settings management.

## Installation

To install and use this project, please follow these steps:

1. Clone the repository:
```shell
git clone https://github.com/samoilovartem/windsor-ai-task.git
```
2. Install the dependencies:

The project uses [Poetry](https://python-poetry.org/) for dependency management. If you haven't installed Poetry, you can do so using this command:
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
Then, to install project dependencies, run:
```shell
poetry install
```
3. Activate the virtual environment created by Poetry:
```shell
poetry shell
```

## Usage
The script can be run from the command line using the following format:
```shell
python run.py --fields field_1,field_2,field_3
```
Replace field_1,field_2,field_3 with the actual names of the fields you wish to extract from the CSV file. The field names should be separated by commas without spaces.

The --fields argument is used to specify which columns from the CSV file you wish to include in the output. If you want to include all columns, simply omit the --fields argument.

Here is an example command:
```shell
python run.py --fields date,campaign,clicks
```
In this example, the script will only include the 'date', 'campaign', and 'clicks' columns in the output JSON.

The script logs its progress, so you can see what it's doing. If everything goes well, it will print the resulting JSON to the console. If there's an error at any point, it will print an error message and stop.

## Testing
To ensure the functionality of the program, I have included a suite of tests. These tests cover functions including downloading a file, reading CSV data, converting data to JSON, and handling exceptions.

To run the tests:
```shell
pytest
```
This will automatically find the test files (files that start with test_) and run the tests they contain.

If all the tests pass, you will see an output similar to this:
```shell
======================================================= test session starts =======================================================
platform darwin -- Python 3.11.0, pytest-7.3.2, pluggy-1.2.0
rootdir: /Users/samoylovartem/Projects/python/windsor-ai-task
collected 5 items                                                                                                                 

test_data_fetcher.py .....                                                                                                  [100%]

======================================================== 5 passed in 0.52s ========================================================
```



