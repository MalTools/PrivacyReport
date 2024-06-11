import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_html(url):

    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        print(f"fetching html: {url}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the HTML content from {url}: {e}")
        return None


def extract_text_and_urls(html_content, base_url=None):

    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = []
    urls = []

    # Extracting the text of <p> tags
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text(strip=True))

    # Extract the text of a <div> tag with a specific class name
    div_class_names = ['h3', 'p']  # Add other class names as needed
    for class_name in div_class_names:
        for div in soup.find_all('div', class_=class_name):
            paragraphs.append(div.get_text(strip=True))

    # Extracting text from tables
    for table in soup.find_all('table'):
        table_text = []
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            row_text = [cell.get_text(strip=True) for cell in cells]
            table_text.append('\t'.join(row_text))
        paragraphs.append('\n'.join(table_text))

    # Extract all URLs in <a> tags
    for a in soup.find_all('a', href=True):
        href = a['href']
        full_url = urljoin(base_url, href)  # 拼接完整的URL
        urls.append(full_url)

    return paragraphs, urls


def save_text_to_file(paragraphs, output_file_path):

    try:
        with open(output_file_path, 'a', encoding='utf-8') as file:
            for paragraph in paragraphs:
                file.write(paragraph + '\n\n')
        print(f"Text content saved to {output_file_path}")
    except IOError as e:
        print(f"Error saving text content to file: {e}")


def main():

    start_url = 'https://in.m.jd.com/help/app/private_policy.html'  # https://example.com

    output_file_path = '../data/Jingdong_segmented.txt'  # output.txt

    # Crawling the content of the starting URL
    html_content = fetch_html(start_url)
    if not html_content:
        return
    paragraphs, urls = extract_text_and_urls(html_content, start_url)
    save_text_to_file(paragraphs, output_file_path)

    visited_urls = {start_url}
    for url in urls:

        if not url.startswith('http'):
            continue

        if url in visited_urls:
            return

        visited_urls.add(url)

        html_content = fetch_html(url)
        if not html_content:
            continue
        paragraphs, urls = extract_text_and_urls(html_content)
        save_text_to_file(paragraphs, output_file_path)


if __name__ == "__main__":
    main()
