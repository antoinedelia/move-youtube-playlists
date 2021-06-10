from src.utils import logger
from src import youtube_api

youtube = youtube_api.Youtube_Api().init_youtube_client("client_secret.json")


def test_init_youtube_client():
    pass


def test_get_playlist_id_by_name():
    result = youtube.get_playlist_id_by_name("")
    logger.info(result)


def test_does_playlist_exist_by_name():
    pass


def test_delete_playlist():
    pass


def test_add_video_to_playlist():
    pass
