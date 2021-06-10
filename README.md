# Move Youtube playlists to a new account

Easy way to move Youtube playlists to a new account.

## Getting Started

You will need OAuth credentials from [Youtube API](https://console.cloud.google.com/apis/api/youtube.googleapis.com). You can (and should) download the credcentials directly from the console and place the `client_secret.json` file at the root of the workspace. You can find more info on the [Official Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python).

You will also need a CSV file for each playlist you wish to export. To do so, go to [Google Takeout](https://takeout.google.com/settings/takeout) and only export Youtube playlists. After that, place all CSV files into a `playlists` folder at the root of the workspace.


## Testing

```bash
# Install pytest and the pytest-env plugin
$ pip install pytest
$ pip install pytest-env

# Run all the tests
$ pytest

# Run tests from a specific file
$ pytest tests/test_main.py

# Run a specific test
$ pytest tests/test_main.py::test_get_csv_files_from_dir
```
---
```bash
# You can also generate a report to be sure all of the code is covered by the tests using pytest-cov.

$ pip install pytest-cov

$ pytest --cov=. tests/

# Use one of these command to generate a detailed report
$ coverage report -m
$ pytest --cov-report term-missing --cov=. tests/

# You can also generate an HTML report
$ pytest --cov-report html:tests_report --cov=. tests/

# Place the report in a folder with the current datetime
$ pytest --cov-report html:tests_report/report-"$(date +'%F %T')" --cov=. tests/
```