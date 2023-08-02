from pytube import YouTube
from moviepy.editor import *
from tqdm import tqdm
from slugify import slugify

import os

def download_youtube_audio(url, output_path):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(only_audio=True).first()
        video_stream.download(output_path, filename=f"{slugify(yt.title)}.mp4")

        video_path = f"{output_path}/{slugify(yt.title)}.mp4"
        audio_filename = f"{slugify(yt.title)}.mp3"
        audio_path = f"{output_path}/{slugify(yt.title)}.mp3"
        audio_clip = AudioFileClip(video_path)
        audio_clip.write_audiofile(audio_path)
        audio_clip.close()

        os.remove(video_path)

        print(f"Audio successfully extracted from {yt.title}")
    except Exception as e:
        print(f"Error extracting audio from {url} : {e}")

if __name__ == "__main__":
    youtube_urls = [
        "https://www.youtube.com/watch?v=VIDEO_ID_1",
        "https://www.youtube.com/watch?v=VIDEO_ID_2",
        # add other yt videos URLs here...
    ]

    output_path = "output"

    for url in tqdm(youtube_urls, desc="Extracting audio"):
        download_youtube_audio(url, output_path)