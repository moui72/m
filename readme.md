# Tyler Peckenpaugh's python repo

This repo contains some arbitrary examples of python code that I have written

## Installation

 1. Clone the repo. 
 2. With Python >= 3.8 run `pip install -r requirements.txt`.
 3. Download the [data file]([dataset](https://github.com/magiclabs/email_screening_question/blob/master/Backend/data.csv.zip) and save and unzip it as `data.csv` in the repo root directory

## Run test suite

To run all tests: Run `pytest .` from the repo directory.

To run one test file: Run `pytest <test_file_name>`, e.g., `pytest test_temperature_explorer.py`

To run one test: Run `pytest <test_file_name>::<test_name>`, e.g., `pytest test_temperature_explorer.py::test_coldest` 

You can get higher levels of verbosity from pytest by using, e.g., `-v`, `-vv`, or `-vvv` as arguments when invoking the executable

## Sample test output

Here's the output from a test run on the author's machine

```sh
pytest -vv 
================================================ test session starts =================================================
platform linux -- Python 3.8.5, pytest-6.2.1, py-1.10.0, pluggy-0.13.1 -- /home/peckent/.pyenv/versions/3.8.5/bin/python3
cachedir: .pytest_cache
rootdir: /home/peckent/magic
collected 11 items                                                                                                   

test_flatten.py::test_flatten[input0-expected_output0] PASSED                                                  [  9%]
test_flatten.py::test_flatten[input1-expected_output1] PASSED                                                  [ 18%]
test_flatten.py::test_flatten[input2-expected_output2] PASSED                                                  [ 27%]
test_flatten.py::test_flatten[input3-expected_output3] PASSED                                                  [ 36%]
test_flatten.py::test_flatten[input4-expected_output4] PASSED                                                  [ 45%]
test_flatten.py::test_flatten[input5-expected_output5] PASSED                                                  [ 54%]
test_flatten.py::test_flatten[input6-expected
```