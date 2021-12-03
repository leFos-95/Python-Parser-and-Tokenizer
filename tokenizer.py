
import common_data
import re

# Establishment of custom TNSDL tokenizer.
def s_ident(scanner, token):
    if token in common_data.keyword_list:
        return (token, 'keyword')
    else: return (token, 'identifier')
def s_arithm_operator(scanner, token): return (token, 'a_operator')
def s_logic_operator(scanner, token): return (token,'l_operator')
def s_float(scanner, token): return (token,'float')
def s_int(scanner, token): return (token, 'int')
def s_punctuation(scanner, token): return (token, 'punctuation')
def s_termination(scanner, token): return (token, 'termination')
def s_assignment(scanner, token): return (token, 'assignment')
def s_open_bracket(scanner, token): return (token, 'open bracket')
def s_close_bracket(scanner, token): return (token, 'close bracket')
def s_hex(scanner, token): return (token, 'hex')
def s_case(scanner, token): return ('):', 'case')
def s_preprocessor(scanner, token): return (token, 'preprocessor')
def s_comment(scanner, token): return (token, 'comment')
scanner = re.Scanner([
(r"[\w_]\w*|\?", s_ident),
(r"\d+\.\d*", s_float),
(r"\d+x\d*", s_hex),
(r"/\*|\*/|//", s_comment),
(r"\d+", s_int),
(r"==|>=|<=|>(?![>=])|<(?![<=])|/=|&(?!=)|%(?!=)|&&|!|<<(?!=)|>>(?!=)", s_logic_operator),
(r"\+(?!=)|-(?!=)|\*(?!=)|/(?!=)", s_arithm_operator),
(r"[,@'.:!\"\\]", s_punctuation),
(r"[;]", s_termination),
(r"=|\+=|\-=|\*=|/=|%=|&=|\|=|\^=|<<=|>>=", s_assignment),
(r"\(|\[|{", s_open_bracket),
(r"\)(?!:)|\]|}", s_close_bracket),
(r"\):", s_case),
(r"#if|#else|#endif|#include|#|#undef|elif|#line|#error|#warning|#region|#endregion|#", s_preprocessor),
(r"\s+", None),
])
