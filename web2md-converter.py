import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import base64
import argparse

def get_base64_image(img_url):
    try:
        # Fetch the image
        response = requests.get(img_url)
        response.raise_for_status()  # Raise an error for bad responses
        # Encode the image in Base64
        return base64.b64encode(response.content).decode('utf-8')
    except Exception as e:
        print(f"Error fetching image {img_url}: {e}")
        return None

def main(url, target_class):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the div with the specified class
    div_content = soup.find('div', class_=target_class)

    # Convert the HTML content to Markdown
    if div_content:
        # Replace images with Base64 encoded inline images
        for img in div_content.find_all('img'):
            img_url = img['src']
            base64_image = get_base64_image(img_url)
            if base64_image:
                # Create the Markdown image syntax with Base64
                img_markdown = f'![{img.get("alt", "")}](data:image/jpeg;base64,{base64_image})'
                img.replace_with(BeautifulSoup(img_markdown, 'html.parser'))

        # Convert the modified HTML content to Markdown
        markdown_content = md(str(div_content))

        # Save the Markdown content to a file
        with open('output.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print("Markdown content saved to output.md")
    else:
        print(f"No content found for class: {target_class}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape content from a webpage and convert it to Markdown.')
    parser.add_argument('url', type=str, help='The URL of the webpage to scrape.')
    parser.add_argument('target_class', type=str, help='The class of the target div to scrape.')

    args = parser.parse_args()
    main(args.url, args.target_class)