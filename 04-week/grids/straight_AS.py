from TextGrid import TextGrid

DEFAULT_FILENAME = 'guava.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    # TODO: your code here!
    flag = 0
    for col in range(grid.height):
        for row in range(grid.width):
            cell = grid.get_cell(row, col)
            if cell.value == 'A':
                cell.value = 'A'
                flag = 1
            if flag == 1:
                cell.value = 'A'

    print(grid)

if __name__ == '__main__':
    main()