import requests
import pickle

url = f'https://drive.google.com/file/d/1kJkkt3OcyEiDUPq8rQo9Ky1zavldbock/view?usp=drive_link'

# Send a GET request to download the file
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a .pkl file
    with open('rx.pkl', 'wb') as f:
        f.write(response.content)
    print("File downloaded successfully.")
else:
    print("Failed to download file.")

# Load the model from the downloaded pickle file
with open('rx.pkl', 'rb') as f:
    model = pickle.load(f)

# Now you can use your model
print("Model loaded successfully.")
