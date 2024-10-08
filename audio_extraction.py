# audio_extraction.py

import moviepy.editor as mp

def extract_audio_from_video(video_path, output_audio_path):
    """
    Extracts audio from a video file.
    
    Parameters:
    video_path (str): Path to the input video file.
    output_audio_path (str): Path to save the extracted audio file.
    
    Returns:
    None
    """
    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)

    print(f"Audio extracted to {output_audio_path}")
