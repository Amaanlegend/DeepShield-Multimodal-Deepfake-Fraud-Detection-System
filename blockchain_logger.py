# blockchain_logger.py

import hashlib
import json

def hash_result(result_data):
    """
    Hashes the detection result for immutability.
    
    Parameters:
    result_data (dict): Result data to be hashed (includes deepfake detection result).
    
    Returns:
    str: The resulting hash of the data.
    """
    result_string = json.dumps(result_data, sort_keys=True).encode()
    result_hash = hashlib.sha256(result_string).hexdigest()
    return result_hash

def log_to_blockchain(result_data):
    """
    Logs the detection result onto the blockchain for transparency.
    
    Parameters:
    result_data (dict): Detection result data.
    
    Returns:
    str: Blockchain transaction hash.
    """
    # For demonstration, we will return a simulated blockchain hash
    transaction_hash = hash_result(result_data)
    print(f"Result logged on blockchain with hash: {transaction_hash}")
    return transaction_hash
