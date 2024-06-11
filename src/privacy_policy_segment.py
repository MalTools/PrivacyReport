from bs4 import BeautifulSoup


def extract_paragraphs_from_html(html_content):
    """
    从HTML内容中提取段落文本
    :param html_content: 输入的HTML内容
    :return: 返回提取的段落文本列表
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = []

    # 提取<p>标签的文本
    p_tags = soup.find_all('p')
    paragraphs.extend([p.get_text(strip=True) for p in p_tags])

    # 提取具有特定类名的<div>标签的文本
    div_class_names = ['h3', 'p']  # 根据需要添加其他类名
    for class_name in div_class_names:
        divs = soup.find_all('div', class_=class_name)
        paragraphs.extend([div.get_text(strip=True) for div in divs])

    return paragraphs


def read_html_file(file_path):
    """
    读取HTML文件内容
    :param file_path: HTML文件路径
    :return: HTML内容
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except IOError as e:
        print(f"Error reading HTML file: {e}")
        return None


def save_text_to_file(paragraphs, output_file_path):
    """
    将提取的段落文本内容保存到文件中，每个段落按行分开
    :param paragraphs: 段落文本内容列表
    :param output_file_path: 输出文件路径
    """
    try:
        with open(output_file_path, 'w', encoding='utf-8') as file:
            for paragraph in paragraphs:
                file.write(paragraph + '\n\n')
        print(f"Text content saved to {output_file_path}")
    except IOError as e:
        print(f"Error saving text content to file: {e}")


def main():
    # 输入HTML文件路径
    input_file_path = '../data/Jingdong-pp.html'
    # 输出文件路径
    output_file_path = '../data/Jingdong-pp-segmented.txt'

    # 读取HTML文件内容
    html_content = read_html_file(input_file_path)

    if html_content:
        # 提取段落文本内容
        paragraphs = extract_paragraphs_from_html(html_content)
        # 保存段落文本内容到文件
        save_text_to_file(paragraphs, output_file_path)


if __name__ == "__main__":
    main()
