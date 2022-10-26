def get_primes(lst):
    list_of_integers = lst
    for element in list_of_integers:
        flag = False

        if element > 1:
            # check for factors
            for i in range(2, element):
                if (element % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

            # check if flag is True
            if not flag:
                yield element

gen = get_primes([2, 4, 3, 5, 6, 9, 1, 0])
print(list(gen))
