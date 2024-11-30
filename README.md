### AOC-2024

## Installing

- Required: `Python 3.12.0`

Packages are managed using [Poetry](https://python-poetry.org/) After installation of poetry, the following command can be used to install the required packages:

```bash
poetry install
```

## Scaffolding

In order to get started on a new day, a scaffolding script is provided. This script will create a dedicated folder for your day, including a python file for the day and a test file for the day. It will also create a `input.txt` file for the day, which can be used to paste the input data for the day.

Scaffolding can be done using the following command:

```bash
python scaffold.py --day {day}
```

## Running

Any of the part files can be run directly using the built-in vscode runner, or by simply calling the python file e.g;

```bash
python 01/part1.py
python 01/part2.py
```

The (generated) unit tests can be used to test the test input of the day, just paste the test data in `{day}/test_input.txt` and adjust the expected values in `{day}/day_test.py`.
