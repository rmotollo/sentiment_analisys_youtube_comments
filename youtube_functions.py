from googleapiclient.discovery import build

def initialize_youtube_api(apikey: str) -> build:
    return build('youtube', 'v3', developerKey=apikey)


def get_comments(youtube, video_id, max_results=100):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=max_results
    )
    response = request.execute()
    comments = []
    for item in response['items']:
        comment = comments.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        if comment is not None:
            comments.append(comment)

    return comments