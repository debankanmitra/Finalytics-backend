import os
import tempfile
from pytube import YouTube
from deepgram import DeepgramClient, PrerecordedOptions, FileSource

DEEPGRAM_API_KEY=os.environ.get('DEEPGRAM_API_KEY')

def download_audio(video_url):
    yt = YouTube(video_url)
    audio_streams = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        audio_streams.download(filename=temp_file.name)
        audio_filename = temp_file.name  # Store the temporary filename

    return audio_filename


def get_transcription(audiofile):
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    with open(audiofile, "rb") as file:
        buffer_data = file.read()

    payload: FileSource = {
        "buffer": buffer_data,
    } 

    options = PrerecordedOptions(
        model='nova-2-video',
        detect_language=True,
        filler_words=False,
        language='en',
        numerals=True,
        profanity_filter=True,
        smart_format=True,
        paragraphs=False
    )
    response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
    transcription=response["results"]["channels"][0]["alternatives"][0]["transcript"]
    return transcription


def download_and_transcribe(youtube_url):
    audio_file = download_audio(youtube_url)
    try:
        response = get_transcription(audio_file)
    finally:
        # Attempt to delete the temporary file using shutil (alternative to os.remove)
        if os.path.exists(audio_file):
            os.remove(audio_file)
    return response

print(download_and_transcribe('https://www.youtube.com/watch?v=0CmtDk-joT4'))