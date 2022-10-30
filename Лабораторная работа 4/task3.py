def delete(list_, index=None):
    if index is not None:
        first_list = list_[:index]
        second_list = list_[index+1:]
        new_list = first_list + second_list
    else:
        new_list = list_[:len(list_)-1]

    return new_list

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
