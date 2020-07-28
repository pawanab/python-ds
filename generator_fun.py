#list comprehension 
total = sum([n for n in range(1,100) if n%2==0 ])
print(total)

## generator; difference with list comprehension is []not used here
total = sum(n for n in range(1,100) if n%2==0 )
print(total)

cost = 10_000
print(f'COST 10_000 == {cost}')

hex_flag = 0xDAFE_FFF8
print(f'hefa flag 0xDAFE_FFF8 == {hex_flag}')

binary = 0b_0011_1001
print(f'Binary 0b_0011_1001 == {binary}')