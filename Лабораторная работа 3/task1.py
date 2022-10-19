src = not False and True or False and not True

# result = True and True or False and False # упростили отрицания
# result = True or False # упростили логическое "и"

result = True  # избавляемся от логического "ИЛИ"

print(src == result)
