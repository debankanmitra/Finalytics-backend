# https://docs.cohere.com/reference/summarize-2
# Logic to summarize Youtube videos

from transcription import download_and_transcribe
import cohere 
import os

COHERE_API_KEY=os.environ.get('COHERE_API_KEY')

def get_summary(youtube_url):
    co = cohere.Client(COHERE_API_KEY)

    transcription = download_and_transcribe(youtube_url)
    response = co.summarize(
        model='summarize-xlarge',
        length='long',
        format='paragraph',
        temperature=0.3,
        text=transcription
    )
    summary = response.summary
    return summary

print(get_summary('https://www.youtube.com/watch?v=Unayrm7B-cw'))