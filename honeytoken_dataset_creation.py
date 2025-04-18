import pandas as pd
import random
import string

def generate_api_key(length=32):
    """Generate a random API key."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_api_keys_dataset(num_keys=300000, key_length=32):
    """Generate a dataset of API keys."""
    api_keys = [generate_api_key(key_length) for _ in range(num_keys)]

    # Convert to DataFrame
    df = pd.DataFrame(api_keys, columns=["api_key"])

    # Save to CSV file
    df.to_csv("api_keys_dataset.csv", index=False)
    print("Dataset generated and saved as 'api_keys_dataset.csv'")

# Generate and save 300,000 API keys
generate_api_keys_dataset()
