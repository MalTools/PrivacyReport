import requests
from bs4 import BeautifulSoup


def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        return html_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the HTML content: {e}")
        return None


def save_html_to_file(html_content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
        print(f"HTML content saved to {file_path}")
    except IOError as e:
        print(f"Error saving the HTML content to file: {e}")


def main():
    # Webpage URL
    url = 'https://in.m.jd.com/help/app/private_policy.html'  # https://example.com
    # 保存HTML内容的文件路径
    file_path = '../data/Jingdong-pp.html'  # webpage.html

    html_content = fetch_html(url)

    if html_content:
        # Save html file
        save_html_to_file(html_content, file_path)


if __name__ == "__main__":
    main()
