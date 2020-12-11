def max_find(sequence):
    curr_max = global_max = sequence[0]
    for n in sequence[1::]:
        curr_max = max(n, curr_max+n)
        global_max = max(global_max, curr_max)

    print(global_max)


if __name__ == '__main__':
    n = list(map(int,input().strip().split()))
    max_sum(n)

    