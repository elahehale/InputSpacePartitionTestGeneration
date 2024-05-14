import copy


def get_input():
    # get non-empty list of characteristics
    while True:
        characteristics_input = input("Enter list of comma-separated characteristics, at least one required: ")
        characteristics = [item.strip() for item in characteristics_input.split(",") if item.strip()]
        # handle empty list
        if characteristics:
            break
        else:
            print("Please enter at least one valid characteristic.")
    print("Your given characteristics: " + ", ".join(characteristics))

    abstract_blocks = []
    max_blocks_num = 0

    # get list of abstract blocks for each characteristic. abstract blocks can't be empty
    i = 0
    while i < len(characteristics):
        ch = characteristics[i]
        while True:
            ch_blocks_input = input(f"Enter blocks of characteristic '{ch}' comma separated, at least one required: ")
            ch_blocks = [item.strip() for item in ch_blocks_input.split(",") if item.strip()]
            # handle empty list
            if ch_blocks:
                max_blocks_num = max(max_blocks_num, len(ch_blocks))
                abstract_blocks.append(ch_blocks)
                break
            else:
                print("Blocks can't be empty for a characteristic. Please enter at least one block.")
        i += 1

    print("Blocks for each characteristic:", abstract_blocks)
    return characteristics, abstract_blocks, max_blocks_num


def get_bcc_base(characteristics_num):
    base = get_mbcc_bases(1, characteristics_num)[0]
    print(base)
    return base


def get_mbcc_bases(m, characteristic_num):
    bases = [[] for t in range(characteristic_num)]
    for i in range(m):
        base_blocks = input("Enter blocks index of base" + str(i + 1) + " comma seperated: ")
        blocks = base_blocks.split(",")
        for j in range(characteristic_num):
            bases[j].append(blocks[j])
    print(bases)
    return bases


def acoc_test_generation(characteristics, abstract_blocks):
    tests = ['']
    ch_len = len(characteristics)
    for i, ch in enumerate(characteristics):
        temp_tests = []
        for test in tests:
            for block in abstract_blocks[i]:
                new_test = test + (',' if i != 0 and i < ch_len else '') + block
                temp_tests.append(new_test)
        tests = temp_tests
    print(tests)
    return tests


def ecc_test_generation(characteristics, abstract_blocks, test_num):
    tests = ['' for t in range(test_num)]
    i = 0
    while i < test_num:
        for j, ch in enumerate(characteristics):
            length = len(abstract_blocks[j])
            tests[i] = tests[i] + (',' if j != 0 and j < test_num else '') + abstract_blocks[j][min(i, i % length)]
        i += 1
    print(tests)
    return tests


def mbcc_test_generation(characteristics, abstract_blocks, bases):
    tests =[]
    for x in range(len(bases[0])):
        base = []
        base_test = []
        for block in bases:
            base.append(block[x])
        for ch, b in enumerate(base):
            base_test.append(abstract_blocks[ch][b])
        tests.append(','.join(base_test))
        for i, ch in enumerate(characteristics):
            for j, block in enumerate(abstract_blocks[i]):
                new_test = copy.copy(base_test)
                if j not in bases[i]:
                    new_test[i] = block
                    tests.append(','.join(new_test))
    print(tests)
    return tests


def bcc_test_generation(characteristics, abstract_blocks, base):
    base_test = []
    for ch, b in enumerate(base):
        base_test.append(abstract_blocks[ch][b])
    print(base_test)
    tests = [','.join(base_test)]
    for i, ch in enumerate(characteristics):
        for j, block in enumerate(abstract_blocks[i]):
            new_test = copy.copy(base_test)
            if j != base[i]:
                new_test[i] = block
                tests.append(','.join(new_test))
    print(tests)
    return tests



def acoc():
    # chars, blocks, _ = get_input()
    acoc_test_generation(['A', 'B'], [['a1', 'a2', 'a3'], ['b1', 'b2']])


def ecc():
    # chars, blocks, tests_len = get_input()
    ecc_test_generation(['A', 'B', 'C'], [['a1', 'a2', 'a3', 'a4'], ['b1', 'b2', 'b3'], ['c1']], 4)


def bcc():
    # chars, blocks, _ = get_input()
    # base = get_bcc_input(len(chars))
    bcc_test_generation(['A', 'B', 'C'], [['a1', 'a2', 'a3', 'a4'], ['b1', 'b2', 'b3'], ['c1', 'c2']], [1, 1, 1])

def mbcc():
    # chars, blocks, _ = get_input()
    # base = get_bcc_input(len(chars))
    bcc_test_generation(['A', 'B', 'C'], [['a1', 'a2', 'a3', 'a4'], ['b1', 'b2', 'b3'], ['c1', 'c2']], [1, 1, 1])


# mode = input("choose your test generation mode\n1 = ACoC\n2 = ECC\n3 = BCC\n4 = MBCC\nEnter number: ")
# methods = {
#     '1': acoc,
#     '2': ecc,
#     '3': bcc,
#     '4': mbcc,
# }
# methods.get(mode)()

# print(get_mbcc_bases(3, 4))
# mbcc_test_generation(['A', 'B', 'C'], [['a1', 'a2', 'a3', 'a4'], ['b1', 'b2', 'b3','b4'], ['c1', 'c2']], [[1,2],[1,2],[1,1]])
get_input()