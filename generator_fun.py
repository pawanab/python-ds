#list comprehension 
total = sum([n for n in range(1,100) if n%2==0 ])
print(total)

## generator; difference with list comprehension is []not used here
total = sum(n for n in range(1,100) if n%2==0 )
print(total)