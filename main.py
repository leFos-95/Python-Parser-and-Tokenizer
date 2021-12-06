import common_data
from tokenizer import scanner
from collections import defaultdict
from nltk.corpus import wordnet

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

def retrieve_str_tokens(tokenized_text):
    open_string = 0
    #    print tokenized_text
    for tok_index, tok in enumerate(tokenized_text):
        if tok[0] == '"':
            if open_string == 0:
                open_string = 1
                tok[1] = "string_content"
            else:
                if tokenized_text[0] != '//':
                    open_string = 0
                tok[1] = "string_content"
        else:
            if open_string == 1:
                tok[1] = "string_content"


    return tokenized_text

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


def frequency_keywords(tokenized_text):
    counter = defaultdict(int)
    counts = 0
    tokenized_text = [list(item) for item in tokenized_text]
    for token in tokenized_text[0]:
        if token[0] in common_data.keyword_list:
            counter[token[0]] += 1
            counts += 1

    return counter, "Total number of frequency keywords is: ", counts


def english_word(tokenized_text):  # Petros Papaioannou
    tokenized_text = [list(item) for item in tokenized_text[0]]
    is_isnt = [0, 0]
    for item in tokenized_text:
        if (item[0] != " "):
            if (wordnet.synsets(item[0])):
                print
                "Tokenized item: '", item[0], "' is an english word."
                is_isnt[0] += 1
            else:
                print
                "Tokenized item: '", item[0], "' is not an english word."
                is_isnt[1] += 1

    print("English words found: ", is_isnt[0], ".")
    print("Non - English words found: ", is_isnt[1], ".")






print(tokenize_text('java.txt'))
text_in_tokens = tokenize_text('java.txt')
token_map = retrieve_file_Java_comment_tags(text_in_tokens)
tokenized_text_with_comments_marked = remove_comments(text_in_tokens, token_map)
tokenized_text_with_strings_class_names = retrieve_class_names(tokenized_text_with_comments_marked)
tokenized_text_with_frequency_keywords = frequency_keywords(text_in_tokens)
tokenized_text_with_comments_and_string_contents_marked = retrieve_str_tokens(tokenized_text_with_comments_marked)



# print(retrieve_file_Java_identifiers(text_in_tokens))
# print(token_map)
# print(tokenized_text_with_comments_marked)
# print(tokenized_text_with_strings_class_names)
# print(nesting_level(tokenized_text_with_comments_marked))
# print(tokenized_text_with_frequency_keywords)
print(tokenized_text_with_comments_and_string_contents_marked)
english_word(text_in_tokens)

