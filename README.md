# Move Youtube playlists to a new account

Easy way to move Youtube playlists to a new account.

## Getting Started

You will need OAuth credentials from [Youtube API](https://console.cloud.google.com/apis/api/youtube.googleapis.com). You can (and should) download the credcentials directly from the console and place the `client_secret.json` file at the root of the workspace. You can find more info on the [Official Python Quickstart](https://developers.google.com/youtube/v3/quickstart/python).

You will also need a CSV file for each playlist you wish to export. To do so, go to [Google Takeout](https://takeout.google.com/settings/takeout) and only export Youtube playlists. After that, place all CSV files into a `playlists` folder at the root of the workspace.
