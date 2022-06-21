def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
        print()
    except IndexError:
        i = i - 1
    finally:
        return my_list[i]
