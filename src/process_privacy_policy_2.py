from bs4 import BeautifulSoup

path = "./privacypolicies/"


def extract_paragraph(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    paragraphs = []

    body = soup.find('body')
    # for element in body.descendants:
    #     if element.name == 'p':
    #         paragraphs.append(element.get_text(strip=True))
    #     elif element.name == 'table':
    #         paragraphs.append(str(element))

    elements = body.find_all(lambda tag: tag.name in ["p", "table"])
    for element in elements:
        if element.name == 'p' and element.find_parent('table') is None:
            paragraphs.append(element.get_text(strip=True))
        elif element.name == 'table':
            paragraphs.append(str(element))


    # Extracting the text of <p> tags
    # for p in soup.find_all('p'):
    #     paragraphs.append(p.get_text(strip=True))

    # Extracting text from tables
    # for table in soup.find_all('table'):
        # table_text = []
        # for row in table.find_all('tr'):
        #     cells = row.find_all(['td', 'th'])
        #     row_text = [cell.get_text(strip=True) for cell in cells]
        #     table_text.append('\t'.join(row_text))
        # paragraphs.append('\n'.join(table_text))

        # table_html = str(table)
        # print(table_html)
        # paragraphs.append(table_html)

    if not paragraphs:
        text_content = soup.get_text(separator='\n', strip=True)
        paragraphs.append(text_content)

    return paragraphs




def save_text_to_file(paragraphs, output_file_path):

    try:
        with open(output_file_path, 'a', encoding='utf-8') as file:
            for paragraph in paragraphs:
                file.write(paragraph + '\n\n\n')
        print(f"Text content saved to {output_file_path}")
    except IOError as e:
        print(f"Error saving text content to file: {e}")


if __name__ == '__main__':
    app_name = 'NetEase Youdao Dictionary'
    file = path + app_name + '.html'
    save_text_to_file(extract_paragraph(file), path + 'pp_slicing/%s.txt' % app_name)
