from tokenizer import scanner

def tokenize_text(file_path):
    with open(file_path, 'r') as f:
        raw_text = f.read()
    tokenized_text = scanner.scan(raw_text)
    return tokenized_text


print(tokenize_text('java.txt'))