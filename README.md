# MakeTweet

This code generates a tweet about a given keyword and creates an image to accompany the tweet using the DALL-E API from OpenAI.

## Requirements

- Python 3.7 or higher
- OpenAI API key
- `dotenv` module
- `requests` module
- `openai` module

## Installation

1. Clone this repository or download the source code as a ZIP file and extract it.
2. Install the required modules by running the following command in your terminal:

    ```
    pip install -r requirements.txt
    ```

3. Rename `.env.example` to `.env` and fill in your OpenAI API key.

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the script:

    ```
    python makeTweet.py
    ```

3. Follow the prompts to enter a keyword and select a user profile and DALL-E style.
4. The script will generate a tweet and a DALL-E style image based on your input and save them to a timestamped directory under the `result` folder.

## Acknowledgements

This script was created with the help of the [OpenAI API](https://beta.openai.com/docs/), the [DALL-E API](https://openai.com/dall-e/), and the following Python modules: `dotenv`, `requests`, and `openai`.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
