def group_of_no_1(island_list, point_no):
    if point_no < 1 or point_no > len(island_list) or island_list[point_no - 1] == 0:
        return 0
    res = 1
    island_list[point_no - 1] = 0
    res += group_of_no_1(island_list, point_no - 1)
    res += group_of_no_1(island_list, point_no + 1)
    return res

print(group_of_no_1([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 1))
print(group_of_no_1([1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], 5))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 4))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 10))
print(group_of_no_1([1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], 1))
print(group_of_no_1([0, 1, 0, 1, 0, 1, 0, 1, 0, 1], 7))
