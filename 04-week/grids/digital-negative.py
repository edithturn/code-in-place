from TextGrid import TextGrid

DEFAULT_FILENAME = 'zero_one.txt'

def main():
    grid = TextGrid(DEFAULT_FILENAME)
    print("Initial grid:")
    print(grid)

    # TODO: your code here!
    for x in range(grid.width):
        for y in range(grid.height):
            cell = grid.get_cell(x, y)
            if cell.value == '0':
                cell.value = '1'
            else: 
                cell.value = '0'

    print("New grid:")
    print(grid)

if __name__ == '__main__':
    main()