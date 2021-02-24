def gen_prime(x):
    results = []
    multiples = []
    for i in range(2, x+1):
        if i not in multiples:
            results.append(i)
            print(' RESULT :: ', results)
            for j in range(i*i, x+1, i):
                print('J >> ',j)
                multiples.append(j)
                print(multiples)




if __name__ == '__main__':
    print(gen_prime(20))

