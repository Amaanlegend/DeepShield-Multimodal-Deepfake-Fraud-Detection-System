import hashlib

def log_to_blockchain(media_file, deepfake_results, biometric_results, confidence_score):
    """
    Logs the results of the analysis to a blockchain ledger.
    """
    log_data = {
        "media_file": media_file,
        "deepfake_results": deepfake_results,
        "biometric_results": biometric_results,
        "confidence_score": confidence_score
    }
    
    # Create a hash of the log data
    data_hash = hashlib.sha256(str(log_data).encode()).hexdigest()

    # Append the data hash to the blockchain (simplified for prototype)
    with open("blockchain_ledger.txt", "a") as ledger:
        ledger.write(f"{data_hash}\n")

    print("Analysis logged to blockchain successfully.")
