import random

FORBIDDEN = r' @!"\'`/\\%&^()~-_:;>=<?{}[]|.,+'
CHARS = [chr(i) for i in range(ord(' '), ord('~')+1)]
NUMS = [chr(i) for i in range(ord('0'), ord('9')+1)]
LC_ALPHAS = [chr(i) for i in range(ord('a'), ord('z')+1)]
UC_ALPHAS = [chr(i) for i in range(ord('A'), ord('Z')+1)]
SYMS = [sym for sym in CHARS if sym not in NUMS+LC_ALPHAS+UC_ALPHAS+list(FORBIDDEN)]


def gen_room_code():
    # Sample Code: 0001@rubbish
    code, text = '', 'shited'  # will use length of shited
    code = ''.join([str(random.randint(0, 9)) for i in range(4)])
    text = ''.join([str(random.choice(SYMS+LC_ALPHAS+UC_ALPHAS)) for i in range(len(text))])
    # random.choice(SYMS)
    # print(len(NUMS+SYMS+LC_ALPHAS+UC_ALPHAS))                  # cr lk th hun                 tr cr lk th hun
    return code+'@'+text  # Number of Possibilities: [30charsLC  72,90,10,000]  [55charsLCUC  27,68,06,40,625]


if __name__ == '__main__':
    # print("ALL: \n", )
    # print()
    # print("NUMS: \n", )
    # print("LC ALPHAS: \n", )
    # print("UC ALPHAS: \n", )
    # print("SYMS: \n", )

    for _ in range(10):
        print('\n', gen_room_code())


