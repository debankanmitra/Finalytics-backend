# https://docs.cohere.com/reference/summarize-2
# Logic to summarize Youtube videos

from transcription import download_and_transcribe
from openai import OpenAI
import cohere 
import os

COHERE_API_KEY=os.environ.get('COHERE_API_KEY')
OPENAI_API_KEY=os.environ.get('OPENAI_API_KEY')

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


def llm_summarize(summaries):
    client = OpenAI(api_key="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")
    context = ""
    for summary in summaries:
        key , _ = next(iter(summary.items())) # accessing key of the first element in the dictionary
        res=key + " is " + summary[key] + '\n'
        context = context + res

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Finance AI helper that helps investors taking trading and investment related decisions regarding cryptocurrencies."},
            {"role": "user", "content": f"Here are the summaries of 3 recent youtube videos on cryptocurrency: {context}\n. Based on the summaries, provide 10 pros and 10 cons of the currency from an investment perspective in bullet points"}
        ],
        max_tokens=2000,
    )
    return completion


# print(get_summary('https://www.youtube.com/watch?v=Unayrm7B-cw'))
# https://platform.openai.com/docs/api-reference/chat/create