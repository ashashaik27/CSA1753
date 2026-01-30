import itertools

def solve_crypt_arithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        mapping = dict(zip(letters, perm))

        # Leading letters cannot be zero
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue

        SEND = (mapping['S'] * 1000 +
                mapping['E'] * 100 +
                mapping['N'] * 10 +
                mapping['D'])

        MORE = (mapping['M'] * 1000 +
                mapping['O'] * 100 +
                mapping['R'] * 10 +
                mapping['E'])

        MONEY = (mapping['M'] * 10000 +
                 mapping['O'] * 1000 +
                 mapping['N'] * 100 +
                 mapping['E'] * 10 +
                 mapping['Y'])

        if SEND + MORE == MONEY:
            print("Solution Found:")
            for k, v in mapping.items():
                print(f"{k} = {v}")
            print(f"\n{SEND} + {MORE} = {MONEY}")
            return

    print("No solution found")

# Main program
if __name__ == "__main__":
    solve_crypt_arithmetic()
