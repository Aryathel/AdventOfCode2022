def get_input():
    with open('./input.txt', 'r')as f:
        return f.read()


def step_1(data: str) -> int:
    max_cal = -1
    for group in data.split('\n\n'):
        val = sum(int(cal) for cal in group.split('\n'))
        if val > max_cal:
            max_cal = val
    return max_cal


def step_2(data: str) -> int:
    max_cals = [-1, -1, -1]
    for group in data.split('\n\n'):
        val = sum(int(cal) for cal in group.split('\n'))
        if any(val > cal for cal in max_cals):
            max_cals[max_cals.index(min(max_cals))] = val
    return sum(max_cals)


if __name__ == "__main__":
    data = get_input()
    print(f'Step 1: {step_1(data)}')
    print(f'Step 2: {step_2(data)}')
