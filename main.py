from pytube import YouTube
from moviepy.editor import AudioFileClip
import os

def download_video(youtube_url, download_dir):
    yt = YouTube(youtube_url)
    ys = yt.streams.get_audio_only()
    video_path = ys.download(output_path=download_dir)
    print("Video downloaded successfully!")
    return video_path  # Return the full path of the downloaded video

def convert_to_mp3(input_path, output_path):
    audio_clip = AudioFileClip(input_path)
    audio_clip.write_audiofile(output_path)
    audio_clip.close()
    print("Video converted to MP3 successfully!")

youtube_url = 'YT_link'
download_dir = r'E:\YTToMP3Conversions\saved_videos'  # Use raw string for directory path
mp3_output_dir = r'E:\YTToMP3Conversions\output'  # Use raw string for directory path

# Ensure the directories exist
os.makedirs(download_dir, exist_ok=True)
os.makedirs(mp3_output_dir, exist_ok=True)

# Download the video and get the full path of the downloaded file
downloaded_video_path = download_video(youtube_url, download_dir)

# Construct the full path for the MP3 file
mp3_output_path = os.path.join(mp3_output_dir, "audio.mp3")

# Convert the downloaded video to MP3
convert_to_mp3(downloaded_video_path, mp3_output_path)
