# test_video_processing.py

import pytest
from src.video_processing.extract_frames import extract_frames

def test_extract_frames():
    video_file = 'tests/sample_video.mp4'
    output_dir = 'tests/output_frames/'
    result = extract_frames(video_file, output_dir)
    
    assert len(result) > 0  # Should return a list of frame file paths
