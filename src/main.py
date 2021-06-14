import os
import json
from dataclasses import dataclass
from typing import List
from pathlib import Path
import pandas as pd

cwd = os.getcwd()
PLAYLISTS_CSV_DIRECTORY_PATH = f"{cwd}/playlists/"
CLIENT_SECRETS_FILE = f"{cwd}/client_secret.json"
REPORT_FILE = "report.json"


@dataclass
class File:
    name: str = None
    name_with_extension: str = None
    path: str = None


def get_files_from_dir(directory_path: str) -> List[File]:
    """Get all files from a directory

    :param directory_path: The path of the directory
    :type directory_path: str
    :return: A list of files found in the directory
    :rtype: List[File]
    """
    from os import listdir
    from os.path import isfile, join
    files = [File(Path(f).stem, f, directory_path + f) for f in listdir(directory_path) if isfile(join(directory_path, f))]
    return files


def main():
    # Keeping this import here for now, as putting it at the top of the file makes pytest raise a ModuleNotFoundError
    from youtube_api import Youtube_Api
    youtube = Youtube_Api()
    youtube.init_youtube_client(CLIENT_SECRETS_FILE)

    files = get_files_from_dir(PLAYLISTS_CSV_DIRECTORY_PATH)

    for file in files:
        playlist_name = file.name
        print(f"Trying to move playlist {playlist_name}")

        # Check if playlist with this name exists. If so, delete it beforehand
        if youtube.does_playlist_exist_by_name(playlist_name):
            print(f"The playlist {playlist_name} already exists. Deleting it...")
            playlist_id = youtube.get_playlist_id_by_name(playlist_name)
            youtube.delete_playlist(playlist_id)
            print(f"The playlist {playlist_name} has successfully been deleted!")

        print(f"Trying to create playlist {playlist_name}...")
        playlist_id = youtube.create_playlist(playlist_name)
        print(f"The playlist {playlist_name} has successfully been created!")

        dataframe = pd.read_csv(file.path)
        videos = json.loads(dataframe.to_json(orient='records'))

        responses = []
        for video in videos:
            video_id = video["Video Id"]
            response = youtube.add_video_to_playlist(playlist_id, video_id)
            responses.add(response)

        number_of_failures = len([response for response in responses if response["status"] == "Failure"])
        number_of_success = len(responses) - number_of_failures
        print(f"There have been {number_of_success}/{len(responses)} success responses.")
        if number_of_failures > 0:
            print(f"You can view a detailed report of what errors occured in the report file {REPORT_FILE}.")
            with open(REPORT_FILE, 'w', encoding='utf-8') as f:
                json.dump(responses, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
