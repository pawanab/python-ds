L = [('Sam', 35),
    ('Tom', 25),
    ('Bob', 30)]

D = {
    'SAM': 35,
    'TOM': 125,
    'BOB': 99
}

def find_max_in_set_first_index(ele):
    return ele[1]

def find_max_by_dict_value(ele):
    return D[ele]


print(max(L, key=find_max_in_set_first_index))

print(max(D, key=find_max_by_dict_value))
