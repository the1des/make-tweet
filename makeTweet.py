import openai
from datetime import datetime
from dotenv import load_dotenv
import os
import uuid
import requests

load_dotenv()  # load environment variables from the .env file

# set up the OpenAI API client
openai.api_key = os.getenv("OPENAI_API_KEY")

# get the keyword from user input
keyword = input("Enter the keyword: ")
keyword = keyword.strip()

prompt = f"make a tweet to explain {keyword} to a young person who like to know more about cryptocurrency and machine learning."

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=550,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

prompt_dalle = f"prepare a phrase for DALL-E API to create a picaso style for this tweet: \n {response.choices[0].text}"

response_dalle = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt_dalle,
  temperature=0.7,
  max_tokens=350,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print('response_dalle: ',response_dalle.choices[0].text)
# Generate the image using Dall-E API
image_response = openai.Image.create(
    prompt=response_dalle.choices[0].text,
    n=1,
    size="256x256"
)


# Create a folder for the current result, named with the current date and time
result_folder_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
result_folder_path = os.path.join("result", result_folder_name)
os.makedirs(result_folder_path)

# Save the generated text to a file in the result folder
result_file_name = str(uuid.uuid4()) + ".txt"
result_file_path = os.path.join(result_folder_path, result_file_name)
with open(result_file_path, "w") as f:
    f.write(response.choices[0].text)


# Download the image binary data from the URL
image_url = image_response['data'][0]['url']
image_binary_data = requests.get(image_url).content

# Save the generated image to a file in the result folder
result_img_file_name = str(uuid.uuid4()) + ".png"
result_img_file_path = os.path.join(result_folder_path, result_img_file_name)
with open(result_img_file_path, "wb") as f:
    f.write(image_binary_data)


print(f"\n Image saved to {result_file_path}")


print(response.choices[0].text.strip())
print(f"\n Response saved to {result_file_path}")
