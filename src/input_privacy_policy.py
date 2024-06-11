
def read_paragraphs_from_file(input_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            paragraphs = file.read().split('\n\n')
        return [para.strip() for para in paragraphs if para.strip()]
    except IOError as e:
        print(f"Error reading text content from file: {e}")
        return None


def combine_paragraphs(paragraphs, max_length=2000):
    combined_paragraphs = []
    current_paragraph = ''

    for paragraph in paragraphs:
        if len(current_paragraph) + len(paragraph) + 1 <= max_length:
            if current_paragraph:
                current_paragraph += ' ' + paragraph
            else:
                current_paragraph = paragraph
        else:
            combined_paragraphs.append(current_paragraph)
            current_paragraph = paragraph

    if current_paragraph:
        combined_paragraphs.append(current_paragraph)

    return combined_paragraphs


def input_paragraphs(input_file_path):

    # Read paragraph text
    paragraphs = read_paragraphs_from_file(input_file_path)

    if paragraphs:
        # Combine paragraph text
        combined_paragraphs = combine_paragraphs(paragraphs)
        # Returns the combined paragraph text list
        return combined_paragraphs


if __name__ == "__main__":
    combined_paragraphs = input_paragraphs('../data/Weibo-segmented.txt')
    # print(len(combined_paragraphs))
    # for i, txt in enumerate(combined_paragraphs):
    #     print(i, txt)