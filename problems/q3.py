"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807

"""


def get_reverse_num(lst):
    if not lst:
        return 0
    rev_lst = lst[::-1]
    rev_num = rev_lst[0]
    for index, value in enumerate(rev_lst):
        try:
            rev_num = rev_num * 10 + rev_lst[index+1]
        except IndexError:
            pass
    return rev_num


def get_reverse_list(num):
    rev_list = []
    while num != 0:
        last_digit = num % 10
        rev_list.append(last_digit)
        num = num // 10
    return rev_list


def solution(l1, l2):
    r_l1 = get_reverse_num(l1)
    r_l2 = get_reverse_num(l2)
    num = r_l1 + r_l2
    result = get_reverse_list(num)
    return result


ls1 = [2, 4, 3]
ls2 = [5, 6, 4]
print(solution(ls1, ls2))
