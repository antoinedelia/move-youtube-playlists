
# Move Youtube playlists to a new account

Easy way to move Youtube playlists to a new account.

> ⚠️ This is still a work in progress and should be used with caution.

## Getting Started

You will need OAuth credentials from [Youtube API](https://console.cloud.google.com/apis/api/youtube.googleapis.com). You can (and should) download the credcentials directly from the console and place the `client_secret.json` file at the root of the workspace. You can find more info on the [Official Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python).

You will also need a CSV file for each playlist you wish to export. To do so, go to [Google Takeout](https://takeout.google.com/settings/takeout) and only export Youtube playlists. After that, place all CSV files into a `playlists` folder at the root of the workspace.

At the end, the script will output a `report.json` file containing all the videos and their status (succes or failure) and an error message in case it failed (if the video is now private, deleted, or if the quotas limit has been reached). 

## Known Issues

### Only 200 videos a day
The current quotas limit for Youtube API calls is at 10'000 per day. The problem is that a single request to add a video to a playlist costs 50, which only let us add 200 videos every day. For people with huge playlists, this can become very troublesome very quickly. The only way to deal with this right now is to run the script every day until all the videos are uploaded. We can ask Google for an increase of the quotas, but I'm not sure if they accept these easily.

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