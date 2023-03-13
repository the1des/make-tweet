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

profile1 = "young person who is interested in gaining a better understanding of cryptocurrency and machine learning"
profile2 = "middle-aged person who wants to understand the basics of artificial intelligence and how it can be applied in their industry"
profile3 = "college student who wants to learn more about the future of renewable energy and how it will impact the job market"
profile4 = "retiree who is interested in learning about how technology is changing the world around them"
profile5 = "entrepreneur who wants to explore the potential of blockchain technology for their business"
profile6 = "Cryptocurrency trader who wants to stay up-to-date with the latest news, trends, and strategies in the cryptocurrency market."

profiles = [profile1, profile2, profile3, profile4, profile5, profile6]
print("Please choose a profile:")
for i, profile in enumerate(profiles):
    print(f"{i+1}. {profile}")

# get the profile from user input
profile_index = int(input("Enter the index of the profile: "))
if profile_index < 1 or profile_index > len(profiles):
    print("Invalid profile index.")
    exit()
profile = profiles[profile_index - 1]

prompt = f"Create a tweet that provides a simple explanation of {keyword} for a {profile}."

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.9,
  max_tokens=550,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

styles = ["abstract", "realistic", "cartoonish", "surreal", "minimalist", "gothic", "pop art", "impressionistic", "geometric", "vintage", "Picasso", "Van Gogh", "Monet", "Rothko", "Pollock" , "Orientalism"]
print("Please choose a DALL-E style from the following options:")
for i, style in enumerate(styles):
    print(f"{i+1}. {style}")

# get the style from user input
style_index = int(input("Enter the index of the style: "))
if style_index < 1 or style_index > len(styles):
    print("Invalid style index.")
    exit()
style = styles[style_index - 1]

prompt_dalle = f"prepare a phrase for DALL-E API to create a {style} style image for this tweet: \n {response.choices[0].text}"

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
    size="256x256",
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
