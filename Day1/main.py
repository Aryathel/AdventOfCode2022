def get_input():
    """Get the data input from the text file."""
    with open('./input.txt', 'r')as f:
        return f.read()


def step_1(data: str) -> int:
    """Split the data into groups, then process each group's total and choose the highest one."""
    max_cal = -1
    for group in data.split('\n\n'):
        val = sum(int(cal) for cal in group.split('\n'))
        if val > max_cal:
            max_cal = val
    return max_cal


def step_2(data: str) -> int:
    """Split the data into groups, the process each group's total and replace
    the lowest value in the top three if the current value is greater than it.
    """
    max_cals = [-1, -1, -1]
    for group in data.split('\n\n'):
        val = sum(int(cal) for cal in group.split('\n'))
        if any(val > cal for cal in max_cals):
            max_cals[max_cals.index(min(max_cals))] = val
    return sum(max_cals)


if __name__ == "__main__":
    print('Advent of Code 2022 Day 1', '-------------------------', sep='\n')
    data = get_input()
    print(f'Step 1: {step_1(data)}')
    print(f'Step 2: {step_2(data)}')
