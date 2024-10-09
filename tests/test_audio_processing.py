# test_audio_processing.py

import pytest
from src.audio_processing.audio_analysis import analyze_audio

def test_audio_analysis():
    audio_file = 'tests/sample_audio.wav'
    result = analyze_audio(audio_file)
    
    assert 'pitch_mean' in result
    assert 'tempo' in result
    assert 'abnormal_pitch' in result
    assert isinstance(result['pitch_mean'], float)
