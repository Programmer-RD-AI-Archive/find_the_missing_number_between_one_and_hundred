a = []
for x in range(56):
    a.append(x)


def find_the_missing_number_between_one_and_hundred(number_list, last):
    numbers_from_one_to_hundred = []
    for x in range(last):
        numbers_from_one_to_hundred.append(x)
    p = []
    for x in numbers_from_one_to_hundred:
        if x in number_list:
            pass
        else:
            p.append(x)
    if p == []:
        print("There are numbers till " + str(last - 1))
    if p != []:
        for m in p:
            print(f"The Numbers that are not from 1 to 100 : " + str(m))


find_the_missing_number_between_one_and_hundred(number_list=a, last=101)

