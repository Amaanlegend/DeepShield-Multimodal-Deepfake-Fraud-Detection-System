from keras.models import load_model
from utils.io_utils import extract_audio_features, extract_face_features

# Load pre-trained models
face_model = load_model("models/face_model.h5")
voice_model = load_model("models/voice_model.h5")

def cross_verify_biometrics(media, biometric_data):
    """
    Cross-verify the media's face and voice against stored biometrics.
    """
    face_verification = verify_face(media['video'], biometric_data['face'])
    voice_verification = verify_voice(media['video'], biometric_data['voice'])

    return {
        "face_verification": face_verification,
        "voice_verification": voice_verification
    }

def verify_face(video, stored_face_image):
    """
    Verify the face in the video with the stored biometric face data.
    """
    # Extract face features from the video
    video_face_features = extract_face_features(video)

    # Compare with the stored face features
    stored_face_features = extract_face_features(stored_face_image)

    # Use model to predict match
    match_score = face_model.predict([video_face_features, stored_face_features])
    return match_score

def verify_voice(video, stored_voice_sample):
    """
    Verify the voice in the video with the stored biometric voice data.
    """
    # Extract audio features from the video
    video_voice_features = extract_audio_features(video)

    # Compare with stored voice features
    stored_voice_features = extract_audio_features(stored_voice_sample)

    # Use voice model to predict match
    match_score = voice_model.predict([video_voice_features, stored_voice_features])
    return match_score
