import os
import googleapiclient
import googleapiclient.errors
import google_auth_oauthlib.flow
import googleapiclient.discovery


class Youtube_Api:
    client = None

    def init_youtube_client(self, client_secrets_file: str):
        scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        self.client = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    def get_playlist_id_by_name(self, playlist_name: str):
        pass

    def does_playlist_exist_by_name(self, playlist_name: str):
        pass

    def delete_playlist(self, playlist_id: str):
        request = self.client.playlist().delete(id=playlist_id)
        try:
            request.execute()
            print(f"Playlist {playlist_id} was successfully deleted.")
        except googleapiclient.errors.HttpError as e:
            print(f"Could not delete playlist {playlist_id} with error: {e}")

    def create_playlist(self, playlist_name: str) -> str:
        request = self.client.playlist().insert(
            part="snippet",
            body={
                "snippet": {
                    "title": playlist_name
                }
            }
        )
        try:
            response = request.execute()
            print(f"Playlist {playlist_name} was successfully created.")
            return response["id"]
        except googleapiclient.errors.HttpError as e:
            print(f"Could not create playlist {playlist_name} with error: {e}")
            return None

    def add_video_to_playlist(self, new_playlist_id: str, video_id: str, position: int = 99999):
        request = self.client.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": new_playlist_id,
                    "position": position,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        )

        try:
            response = request.execute()
            video_title = response["snippet"]["title"]
            print(f"Successully added video with id {video_id}. The video was: {video_title}")
        except googleapiclient.errors.HttpError as e:
            print(f"Could not move video with id {video_id} with error: {e}")
