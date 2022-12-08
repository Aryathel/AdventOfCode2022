from utils import AdventOfCode2022Day


class File:
    """Contains information about a file."""
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        """A string representation of the file."""
        return f'- {self.name} (file, size={self.size})'

    def tree(self, depth: int = 0, indent: str = '  ') -> str:
        """A formatted string representation of a file, for a tree folder view."""
        return (indent * depth) + str(self)


class Directory:
    """Contains information about a directory and the directories and files it contains."""
    directories: dict[str, 'Directory']
    files: list['File']

    def __init__(self, name: str, parent: 'Directory' = None) -> None:
        self.name = name
        self.parent = parent

        self.directories = {}
        self.files = []

    def __str__(self) -> str:
        """A string representation of the directory."""
        return f'- {self.name} (dir)'

    def add_directory(self, name: str) -> None:
        """Adds a child subdirectory to the directory."""
        self.directories[name] = Directory(name=name, parent=self)

    def add_file(self, name: str, size: int) -> None:
        """Adds a child file to the directory."""
        self.files.append(File(name=name, size=size))

    @property
    def path(self) -> str:
        """Gets the full path of the directory."""
        if self.parent:
            return self.parent.path + self.name + '/'
        else:
            return self.name

    @property
    def size(self) -> int:
        """Gets the size of all files contained within all subdirectories of the directory."""
        return sum(i.size for i in self.files) + sum(i.size for i in self.directories.values())

    def tree(self, depth: int = 0, indent: str = '  ') -> str:
        """Gets a tree representation of the directory's file structure."""
        res = [(indent * depth) + str(self)]
        for d in self.directories.values():
            res.append(d.tree(depth=depth+1, indent=indent))
        for f in self.files:
            res.append(f.tree(depth=depth+1, indent=indent))
        return '\n'.join(res)


class Day7(AdventOfCode2022Day, day=7):
    def process_file_tree(self) -> Directory:
        """Creates a structure of Directories and Files from the problem text input."""
        parent_file = Directory(name='/')
        current_dir = parent_file

        for line in self.input.split('\n'):
            params = line.split(' ')
            # Processing commands
            if params[0] == '$':
                # Folder navigation
                if params[1] == 'cd':
                    # Return to root directory
                    if params[2] == '/':
                        current_dir = parent_file
                    # Return to parent of current directory
                    elif params[2] == '..':
                        current_dir = current_dir.parent
                    # Enter specified directory
                    else:
                        current_dir = current_dir.directories[params[2]]
                # Listing directory contents. Nothing actually needs to happen here.
                elif params[1] == 'ls':
                    pass
            # Processing folder contents.
            else:
                # Subdirectory addition
                if params[0] == 'dir':
                    current_dir.add_directory(name=params[1])
                # File addition
                else:
                    current_dir.add_file(size=int(params[0]), name=params[1])

        # Return the root directory containing the full file tree.
        return parent_file

    @classmethod
    def sum_sizes_under_100k(cls, directory: Directory, size: int = 0) -> int:
        """Gets the sum size of all directories whose size is less than 100,000, recursively."""
        if directory.size <= 100000:
            size += directory.size

        for d in directory.directories.values():
            size = cls.sum_sizes_under_100k(d, size=size)

        return size

    def step_1(self) -> int:
        root = self.process_file_tree()

        return self.sum_sizes_under_100k(root)

    @classmethod
    def get_smallest_dir_over_size(cls, directory: Directory, size: int, current: int = None) -> int:
        """Get the smallest directory size that is over a target size."""
        for d in directory.directories.values():
            if d.size >= size:
                if not current:
                    current = d.size
                else:
                    if d.size < current:
                        current = d.size
            current = cls.get_smallest_dir_over_size(d, size, current)
        return current

    def step_2(self) -> int:
        root = self.process_file_tree()

        # Calculate how much space needs to be cleared.
        free_space = 70000000 - root.size
        space_needed = 30000000 - free_space

        # Return the smallest directory size over that amount.
        return self.get_smallest_dir_over_size(root, space_needed)

    def run(self) -> None:
        self.header()
        print(f'Step 1: {self.step_1()}')
        print(f'Step 2: {self.step_2()}')


if __name__ == "__main__":
    Day7().run()
