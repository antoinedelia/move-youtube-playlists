import json
from dataclasses import dataclass
from typing import List
from pathlib import Path
from youtube_api import Youtube_Api
import pandas as pd

PLAYLISTS_CSV_DIRECTORY_PATH = "./playlists/"
CLIENT_SECRETS_FILE = "client_secret.json"


@dataclass
class File:
    name: str = None
    name_with_extension: str = None
    path: str = None


def get_csv_files_from_dir(directory_path: str) -> List[File]:
    from os import listdir
    from os.path import isfile, join
    files = [File(Path(f).stem, f, directory_path + f) for f in listdir(directory_path) if isfile(join(directory_path, f))]
    return files


def main():
    youtube = Youtube_Api()
    youtube.init_youtube_client(CLIENT_SECRETS_FILE)

    files = get_csv_files_from_dir(PLAYLISTS_CSV_DIRECTORY_PATH)

    for file in files:
        playlist_name = file.name
        print(f"Trying to move playlist {playlist_name}")

        # Check if playlist with this name exists. If so, delete it beforehand
        if youtube.does_playlist_exist_by_name(playlist_name):
            playlist_id = youtube.get_playlist_id_by_name(playlist_name)
            youtube.delete_playlist(playlist_id)

        playlist_id = youtube.create_playlist(playlist_name)

        dataframe = pd.read_csv(file.path)
        videos = json.loads(dataframe.to_json(orient='records'))
        for video in videos:
            video_id = video["Video Id"]
            youtube.add_video_to_playlist(playlist_id, video_id)


if __name__ == "__main__":
    main()
