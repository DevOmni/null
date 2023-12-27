import random
from string import ascii_letters, digits, ascii_uppercase, ascii_lowercase, punctuation

FORBIDDEN = r' @!"\'`/\\%&^()~-:;>=<?{}[]|.,+'
CHARS = [chr(i) for i in range(ord(' '), ord('~')+1)]
SYMS = ''.join([c for c in punctuation if c not in FORBIDDEN])


def gen_code_from_pattern(pattern: str or list, forbidden=''):
    # example pattern: nn@sslluuaaa
    # n-number, o-non_numerical, s-symbols (punctuation), l-lowercase, u-uppercase, a-alpha, c-all chars, @-exclusive at
    if not isinstance(pattern, (list, str)):
        raise TypeError('Pattern must be either str or list')
    syms = ''.join([c for c in SYMS if c not in forbidden])
    genome = {'n': digits,          'o': syms+ascii_letters, 's': syms,
              'l': ascii_lowercase, 'u': ascii_uppercase,
              'a': ascii_letters,   'c': digits+syms+ascii_letters}
    generated = ''
    for i, char in enumerate(pattern, 0):
        if char not in list(genome.keys()):
            cchar = char
        elif char in list(FORBIDDEN):
            raise Exception(f'char in pattern should not be one of the Forbidden char {list(FORBIDDEN)}')
        else:
            cchar = random.choice(genome.get(char))
        generated += cchar

    return generated


def gen_cell_code(codel=None, textl=None):
    # Sample Code: 0001@rubbish
    code, text = 'null', 'shited'  # will use length of this strings [4, 6]
    code = ''.join([str(random.randint(0, 9)) for i in range(codel or len(code))])
    text = ''.join([str(random.choice(SYMS.replace('_', '')+ascii_lowercase+ascii_uppercase)) for _ in range(textl or len(text))])
    #                                                      # cr lk th hun                 tr cr lk th hun
    return code + '@' + text  # Number of Possibilities: [30charsLC  72,90,10,000]  [55charsLCUC  27,68,06,40,625]


# def gen_cell_code(pattern=None):
#     code, text = 'null', 'shited'  # will use length of this strings [4, 6]
#     return gen_code_from_pattern(pattern=pattern or f'{"n"*len(code)}@{"o"*len(text)}', forbidden='_')


if __name__ == '__main__':
    # print(gen_code(clen=4, llen=8, syms=1, l_case=1, u_case=0, is_at=0, mix=1))
    print(gen_cell_code())
    # print(SYMS.replace('_', ''))
    # print(SYMS)
    pass
