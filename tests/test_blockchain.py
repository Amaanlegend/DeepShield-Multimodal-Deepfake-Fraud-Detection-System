# test_blockchain.py

import pytest
from src.blockchain.blockchain_logger import log_to_blockchain

def test_blockchain_logging():
    result_data = {'prediction': 'deepfake', 'confidence': 0.9}
    transaction_hash = log_to_blockchain(result_data)
    
    assert len(transaction_hash) == 64  # SHA256 hash length is 64 characters
