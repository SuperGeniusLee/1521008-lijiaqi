#!/env/python3
# -*-encoding: utf-8-*-


def is_chinese(ch):
    if u'\u4e00' <= ch <= u'\u9fa5':
        return True
    else:
        return False


def main(string: str):
    ct_chinese = 0
    ct_number = 0
    ct_letter = 0
    ct_space = 0
    ct_other = 0
    for char in string:
        if char.isdigit():
            ct_number += 1
        elif is_chinese(char):
            ct_chinese += 1
        elif char.isspace():
            ct_space += 1
        elif char.isalpha():
            ct_letter += 1
        else:
            ct_other += 1

    print("chinese: {}, number: {}, letter: {}, space: {}, other: {}".format(ct_chinese, ct_number, ct_letter, ct_space,
                                                                             ct_other))


if __name__ == '__main__':
    main("fuess你门1233  世界号???")

