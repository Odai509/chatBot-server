import requests
from bs4 import BeautifulSoup
import re

# URL of the page to scrape
url = "https://deepseek-ai-deepseek-coder-7b-instruct.hf.space/?view=api"

def get_api_url(url):
    # Fetch the webpage content
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the script containing 'window.gradio_config'
        script = soup.find('script', string=re.compile('window.gradio_config'))
        if script:
            match = re.search(r'"root":\s*"([^"]+)"', script.string)
            if match:
                # Extract the URL
                api_url = match.group(1)
                return api_url
            else:
                return "API URL not found in the script."
        else:
            return "Script with 'window.gradio_config' not found."
    else:
        return f"Error: Status code {response.status_code}"

# Call the function and print the extracted API URL
print(get_api_url(url))
