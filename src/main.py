from youtube_transcript_api import YouTubeTranscriptApi
from bots.FinancialAdvisorBot import FinancialAdvisorBot

def convert_json_to_rst(transcript):
    result = ""
    for caption in transcript:
        result += f"{caption['text']}\n\n" # Each caption is separated by two newlines.
    return result

def get_transcript_for_video():
    video_id = "hr2UmaUN5Cg"
    result = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en']) 
    result = convert_json_to_rst(result)
    return result

def main():
    transcript = get_transcript_for_video()
    bot = FinancialAdvisorBot(transcript)
    result = bot.generate_optimist_recommendation()
    result += "\n"
    result += bot.generate_pesimist_recommendation()
    print(result)
    
if __name__ == "__main__":
    main()
