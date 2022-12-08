from utils import AdventOfCode2022Day


class Day8(AdventOfCode2022Day, day=8):
    @property
    def grid(self) -> list[list[int]]:
        """Convert the input text into a nested list of integers."""
        return [[int(tree) for tree in row] for row in self.input.split('\n')]

    def step_1(self) -> int:
        """Iterate over each tree in a grid and check if it is visible from any outside edge of the grid."""
        forest = self.grid

        visible_count = 0

        for i in range(len(forest)):
            for j in range(len(forest[i])):
                # Check if the tree is on the top or left edges.
                if i == 0 or j == 0:
                    visible_count += 1
                # Check if the tree is on the bottom or right edges.
                elif i == len(forest) - 1 or j == len(forest[i]) - 1:
                    visible_count += 1
                else:
                    tree_height = forest[i][j]
                    visible = False

                    # Check if the tree is visible from the top.
                    top = True
                    for t in range(0, i):
                        if forest[t][j] >= tree_height:
                            top = False
                    if top:
                        visible = True

                    # Check if tree is visible from the left.
                    if not visible:
                        left = True
                        for l in range(0, j):
                            if forest[i][l] >= tree_height:
                                left = False
                        if left:
                            visible = True

                    # Check if tree is visible from the right.
                    if not visible:
                        right = True
                        for r in range(j+1, len(forest[i])):
                            if forest[i][r] >= tree_height:
                                right = False
                        if right:
                            visible = True

                    # Check if tree is visible from the bottom.
                    if not visible:
                        bottom = True
                        for b in range(i+1, len(forest)):
                            if forest[b][j] >= tree_height:
                                bottom = False
                        if bottom:
                            visible = True

                    if visible:
                        visible_count += 1

        return visible_count

    def step_2(self) -> int:
        """Iterate over each tree in the grid and find the "visibility score" of that tree, then return the max."""
        forest = self.grid

        max_score = 0

        for i in range(len(forest)):
            for j in range(len(forest[i])):
                tree_height = forest[i][j]

                # Get upwards count
                top_score = 0
                if not i == 0:
                    for t in range(i-1, -1, -1):
                        top_score += 1
                        if forest[t][j] >= tree_height:
                            break

                # Get left score
                left_score = 0
                if not j == 0:
                    for l in range(j-1, -1, -1):
                        left_score += 1
                        if forest[i][l] >= tree_height:
                            break

                # Get right score
                right_score = 0
                if not j == len(forest[i]) - 1:
                    for r in range(j+1, len(forest[i])):
                        right_score += 1
                        if forest[i][r] >= tree_height:
                            break

                # Get bottom score
                bottom_score = 0
                if not i == len(forest) -1:
                    for b in range(i+1, len(forest)):
                        bottom_score += 1
                        if forest[b][j] >= tree_height:
                            break

                score = top_score * left_score * right_score * bottom_score
                max_score = max(max_score, score)

        return max_score

    def run(self) -> None:
        self.header()

        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day8().run()
