import re 

strs=("10000111", "aabbbbbCdAA", "abbbccda")

# for s in strs:
#     uniq=set(s)
#     # mss=max([max(re.findall(f'{c}+', s), key=len) for c in uniq], key=len)
#     mss=[max(re.findall(f'{c}+', s), key=len) for c in uniq]
#     print(mss)

    
#     print(f'{s} :: {s.index(mss)}, {len(mss)}')




input_str= 'aabbbbbCdAA'
unqi_char = set(input_str)

res_list = []
for c in unqi_char:
    rr = ''.join(re.findall(f'{c}+', input_str))
    res_list.append(rr)

longest_str = max(res_list,key=len)
index_loc = input_str.index(longest_str)
print(f'({index_loc}, {len(longest_str)})')