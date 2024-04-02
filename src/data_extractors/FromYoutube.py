from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def __get_video_id(url):
    try:
        return YouTube(url).video_id
    except Exception as e:
        return None

def __convert_json_to_rst(transcript):
    result = ""
    for caption in transcript:
        result += f"{caption['text']}\n\n"
    return result

def __get_transcript_from_id(video_id):
    result = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en']) 
    result = __convert_json_to_rst(result)
    return result

def get_transcript_for_video(url):
    result = None
    video_id = __get_video_id(url)
    if video_id is None:
        result = None
    else:
        result = __get_transcript_from_id(video_id)
    return result
