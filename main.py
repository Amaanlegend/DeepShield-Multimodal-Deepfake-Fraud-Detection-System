from pre_processing import process_media
from deepfake_detection import detect_deepfake
from biometrics import cross_verify_biometrics
from blockchain_logger import log_to_blockchain

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

    # Step 5: Log results and analysis to blockchain
    log_to_blockchain(media_file, deepfake_results, biometric_results, confidence_score)

    # Step 6: Generate report
    generate_report(deepfake_results, biometric_results, confidence_score)

if __name__ == "__main__":
    main()
