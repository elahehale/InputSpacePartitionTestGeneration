def get_input():
    characteristics = input("Enter list of comma seperated characteristic: ")
    characteristics = characteristics.split(",")
    abstract_blocks = []
    max_blocks_num = 0
    for ch in characteristics:
        ch_blocks = input("Enter blocks of characteristic " + ch + " comma seperated: ")
        ch_blocks = ch_blocks.split(",")
        max_blocks_num = max(max_blocks_num, len(ch_blocks))
        abstract_blocks.append(ch_blocks)
    return characteristics, abstract_blocks, max_blocks_num


def acoc_test_generation(characteristics, abstract_blocks):
    tests = ['']
    ch_len = len(characteristics)
    i = 0
    for ch in characteristics:
        temp_tests = []
        for test in tests:
            for block in abstract_blocks[i]:
                new_test = test + (',' if i != 0 & i < ch_len else '') + block
                temp_tests.append(new_test)
        tests = temp_tests
        i += 1
    print(tests)
    return tests


def ecc_test_generation(characteristics, abstract_blocks, test_num):
    tests = ['' for t in range(test_num)]
    i = 0
    while i < test_num:
        j = 0
        for ch in characteristics:
            length = len(abstract_blocks[j])
            tests[i] = tests[i] + (',' if j != 0 & j < test_num else '') + abstract_blocks[j][min(i, i % length)]
            j += 1
        i += 1
    print(tests)
    return tests


def acoc():
    # chars, blocks, _ = get_input()
    acoc_test_generation(['A', 'B'], [['a1', 'a2', 'a3'], ['b1', 'b2']])


def ecc():
    # chars, blocks, tests_len = get_input()
    ecc_test_generation(['A', 'B', 'C'], [['a1', 'a2', 'a3', 'a4'], ['b1', 'b2', 'b3'], ['c1']], 4)


mode = input("choose your test generation mode\n1 = ACoC\n2 = ECC\n3 = BCC\n4 = MBCC\nEnter number: ")
methods = {
    '1': acoc,
    '2': ecc,
}
methods.get(mode)()

