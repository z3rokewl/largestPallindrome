def gen_numbers():
    for i in range(100, 999):
        for j in range(100, 999):
            yield str(i*j)
    yield None

def pallindrome_checker():
    pallindrome_list = []
    generator = gen_numbers()
    next_number = generator.next()
    while next_number != None:
        if next_number == next_number[::-1]:
            pallindrome_list.append(int(next_number))
        next_number = generator.next()
    return pallindrome_list


def main():
    print max(pallindrome_checker())
    return 0

if __name__ == '__main__':
    main()