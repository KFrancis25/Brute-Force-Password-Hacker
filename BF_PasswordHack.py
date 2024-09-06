import hashlib
import itertools
import string

def hash_password(password: str) -> str:
    """Returns the SHA-256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_password(hashed_password: str, max_length: int = 4):
    """Attempts to brute force the hashed password by generating all possible combinations."""
    chars = string.ascii_lowercase + string.digits  # Possible characters (lowercase + digits)
    attempts = 0
    
    # Try all combinations of characters up to the maximum length
    for length in range(1, max_length + 1):
        for combination in itertools.product(chars, repeat=length):
            attempt = ''.join(combination)
            attempts += 1
            if hash_password(attempt) == hashed_password:
                print(f"Password found: {attempt}")
                print(f"Total attempts: {attempts}")
                return attempt
    print("Password not found within the given length.")
    return None

# Example usage
hashed = hash_password("abc")
brute_force_password(hashed, max_length=4)
