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

def retrieve_file_Java_comment_tags(tokenized_text):
    file_comment_list = []
    for comment_index, keyword in enumerate(tokenized_text[0]):
        if(keyword[1] == "comment"):
            file_comment_list.extend([(keyword, comment_index)])
    return file_comment_list

def remove_comments(tokenized_text, comment_map):
    comment_open = 0
    comment_start = 0
    comment_end = 0
    tokenized_text = [list(item) for item in tokenized_text[0]]

    for comment_position in comment_map:

        if comment_position[0][0] == "/*":
            if comment_open == 0:
                comment_open = 1
                comment_start = comment_position[1]
        if comment_position[0][0] == "*/":
            if comment_open == 1:
                comment_end = comment_position[1]
                comment_open = 0
                for token_index, token in enumerate(tokenized_text[comment_start:comment_end + 1]):
                    tokenized_text[token_index + comment_start][1] = 'delete'

    return tokenized_text

def retrieve_class_names(tokenized_text):
    class_names = []
    for tok_ind, tok in enumerate(tokenized_text):
        if tok[0] == 'class' and tok[1] not in ['string', 'comment']:
            class_names.append(tokenized_text[tok_ind + 1][0])
    return class_names

def nesting_level(tokenized_text):
    tokenized_text = [list(item) for item in tokenized_text]

    nest_level_counter = 0
    max_level = 0

    for tok in tokenized_text:

        if tok[0] == '{':

            nest_level_counter += 1
            if (nest_level_counter > max_level):
                max_level = nest_level_counter
        elif tok[0] == '}':
            nest_level_counter -= 1

    return max_level

print(tokenize_text('java.txt'))
text_in_tokens = tokenize_text('java.txt')
print(retrieve_file_Java_identifiers(text_in_tokens))
token_map = retrieve_file_Java_comment_tags(text_in_tokens)
print(token_map)
tokenized_text_with_comments_marked = remove_comments(text_in_tokens, token_map)
print(tokenized_text_with_comments_marked)
tokenized_text_with_strings_class_names = retrieve_class_names(tokenized_text_with_comments_marked)
print(tokenized_text_with_strings_class_names)
print(nesting_level(tokenized_text_with_comments_marked))