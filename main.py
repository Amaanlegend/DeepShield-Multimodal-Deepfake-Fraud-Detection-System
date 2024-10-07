from pre_processing import process_media
from deepfake_detection import detect_deepfake
from biometrics import cross_verify_biometrics
from blockchain_logger import log_to_blockchain

def calculate_confidence(deepfake_results, biometric_results):
    """
    Calculate the confidence score based on deepfake and biometric analysis.
    Returns a confidence score between 0 and 1 (higher is better).
    """
    # Assign weights to each sub-component (tune based on requirements)
    weight_texture = 0.3
    weight_audio_sync = 0.2
    weight_facial_landmarks = 0.3
    weight_face_verification = 0.1
    weight_voice_verification = 0.1

    # Extract deepfake results
    texture_score = sum(deepfake_results["texture_anomalies"]) / len(deepfake_results["texture_anomalies"])
    audio_sync_score = deepfake_results["audio_sync"]
    facial_landmark_score = sum(deepfake_results["facial_landmarks"]) / len(deepfake_results["facial_landmarks"])

    # Extract biometric results
    face_verification_score = biometric_results["face_verification"]
    voice_verification_score = biometric_results["voice_verification"]

    # Calculate overall confidence score
    confidence_score = (
        (weight_texture * texture_score) +
        (weight_audio_sync * audio_sync_score) +
        (weight_facial_landmarks * facial_landmark_score) +
        (weight_face_verification * face_verification_score) +
        (weight_voice_verification * voice_verification_score)
    )
    
    return confidence_score

def main():
    # Input media files from user
    media_file = "input_media.mp4"
    biometric_data = {"face": "face_image.jpg", "voice": "voice_sample.wav"}

    # Step 1: Pre-process media (stabilization, metadata check)
    processed_media = process_media(media_file)

    # Step 2: Deepfake detection (multimodal: video, audio)
    deepfake_results = detect_deepfake(processed_media)

    # Step 3: Biometric cross-verification
    biometric_results = cross_verify_biometrics(processed_media, biometric_data)

    # Step 4: Calculate Confidence Score
    confidence_score = calculate_confidence(deepfake_results, biometric_results)
    print(f"Confidence Score: {confidence_score:.2f}")

    # Step 5: Log results and analysis to blockchain
    log_to_blockchain(media_file, deepfake_results, biometric_results, confidence_score)

    # Step 6: Generate report
    generate_report(deepfake_results, biometric_results, confidence_score)

if __name__ == "__main__":
    main()

