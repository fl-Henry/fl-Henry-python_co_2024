

def split(dig_str) -> list[str]:

    result_list = []
    next_str = ''
    for char in dig_str:
        if char == " ":
            result_list.append(next_str)
            next_str = ''
        else:
            next_str += char

    if dig_str[-1] != " " and next_str != '':
        result_list.append(next_str)

    return result_list


def sum(dig_list: list[int]) -> int:

    counter = 0
    for x in dig_list:
        counter += x

    return counter


# sss = '12 4568 125'
# print(sss)
# sss = sss.split()
# print(sss)
# sss = [int(x) for x in sss]
# print(sss)
# sss = sum(sss)
# print(sss)


sss = '12 4568 125 4567'
print(sss)
sss = split(sss)
print(sss)
sss = [int(x) for x in sss]
print(sss)
sss = sum(sss)
print(sss)