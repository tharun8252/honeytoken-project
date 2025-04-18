import pandas as pd
import re

# Load each dataset (Modify file paths accordingly)
usernames_df = pd.read_excel("username.xlsx")  # Username dataset
emails_df = pd.read_csv("fake_emails.csv")  # Email dataset
passwords_df = pd.read_csv("password.csv", usecols=[0, 1], names=['password', 'strength'], header=None) # Password dataset (with strength column)
api_keys_df = pd.read_csv("api_keys_dataset.csv")  # API keys dataset

# Rename columns for consistency
usernames_df.columns = ['username']
emails_df.columns = ['email']
passwords_df.columns = ['password', 'strength']
api_keys_df.columns = ['api_key']

# Shuffle datasets for randomness
usernames_df = usernames_df.sample(frac=1).reset_index(drop=True)
emails_df = emails_df.sample(frac=1).reset_index(drop=True)
passwords_df = passwords_df.sample(frac=1).reset_index(drop=True)
api_keys_df = api_keys_df.sample(frac=1).reset_index(drop=True)

# Data Preprocessing Function
def clean_text(text):
    """Removes special characters and converts text to lowercase"""
    return re.sub(r'[^a-zA-Z0-9@._-]', '', str(text)).lower()

# Apply preprocessing to each dataset
usernames_df['username'] = usernames_df['username'].apply(clean_text)
emails_df['email'] = emails_df['email'].apply(clean_text)
passwords_df['password'] = passwords_df['password'].apply(clean_text)
api_keys_df['api_key'] = api_keys_df['api_key'].apply(clean_text)

# Drop duplicates
usernames_df = usernames_df.drop_duplicates()
emails_df = emails_df.drop_duplicates()
passwords_df = passwords_df.drop_duplicates()
api_keys_df = api_keys_df.drop_duplicates()

# Match the dataset sizes to the smallest one (avoiding excess passwords)
min_size = min(len(usernames_df), len(emails_df), len(api_keys_df), len(passwords_df))

# Trim datasets to match the smallest one
usernames_df = usernames_df.iloc[:min_size]
emails_df = emails_df.iloc[:min_size]
passwords_df = passwords_df.iloc[:min_size]
api_keys_df = api_keys_df.iloc[:min_size]

# Merge all datasets into one structured DataFrame
merged_df = pd.concat([usernames_df, emails_df, passwords_df, api_keys_df], axis=1)

# Save the final combined dataset
final_csv = "honeytoken_dataset.csv"
merged_df.to_csv(final_csv, index=False)

print(f"✅ Merging complete! Final dataset saved as {final_csv}")
