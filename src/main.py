from bots.FinancialAdvisorBot import FinancialAdvisorBot
from data_extractors.FromYoutube import get_transcript_for_video 
import sys

def main():
    video_url = sys.argv[1]
    transcript = get_transcript_for_video(video_url)
    bot = FinancialAdvisorBot(transcript)
    result = bot.generate_optimist_recommendation()
    print(result += "\n")
    result = bot.generate_pesimist_recommendation()
    print(result)

if __name__ == "__main__":
    main()
