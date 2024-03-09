from openai import OpenAI
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

load_dotenv()
video_id = "MPD8c3LbL8o" # Replace with your video ID

# prompt = '''
# Hablas español. 
# Eres un buen asesor financiero. 
# Tienes 20 años de experiencia en el mercado de bonos y acciones argentino.
# Tienes 20 años de experiencia en el mercado de bonos y acciones americano e internacional.
# Eres optimista. 
# Ignoras riesgos al momento de invertir.
# Basandote en el siguiente CONTENIDO, enumera las oportunidades de inversion mencionadas.
# Justifica la oportunidad de inversion, puedes utilizar lenguaje tecnico.
# Si no encuentras oportunidad de inversion, entonces di "El video no contiene informacion financiera 🤷‍♂️"
# '''

prompt = '''
Hablas español.
Eres un buen asesor financiero.
Tienes 20 años de experiencia en el mercado de bonos y acciones argentino.
Tienes 20 años de experiencia en el mercado de bonos y acciones americano e internacional.
Eres pesimista.
No tomas riesgos al momento de invertir.
Basandote en el siguiente CONTENIDO, enumera las opciones de inversion mencionadas en las cuales no invertirias.
Justifica, puedes utilizar lenguaje tecnico.
Si no encuentras oportunidad de inversion, entonces di "El video no contiene informacion financiera 🤷‍♂️"
'''

raw_transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es', 'en']) 
def convert_to_rst(transcript):
    rst_text = ""
    for caption in transcript:
        rst_text += f"{caption['text']}\n\n" # Each caption is separated by two newlines.
    return rst_text

rst_transcript = convert_to_rst(raw_transcript)

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": rst_transcript}
  ]
)
print(completion.choices[0].message.content)

