from tokenizer import scanner

def tokenize_text(file_path):
    with open(file_path, 'r') as f:
        raw_text = f.read()
    tokenized_text = scanner.scan(raw_text)
    return tokenized_text

def retrieve_file_Java_identifiers(tokenized_text):
    file_identifier_list = []
    for keyword in tokenized_text[0]:
        if keyword[1] == "identifier":
            file_identifier_list.append(keyword)
    return file_identifier_list


print(tokenize_text('java.txt'))
text_in_tokens = tokenize_text('java.txt')
print(retrieve_file_Java_identifiers(text_in_tokens))