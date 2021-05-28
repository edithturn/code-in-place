SAMPLE_ROSTER = ['edith', 'pavel', 'shrek', 'donkey']

def find_karel(roster):
    if 'edith' in roster:
        print('edith is here!')
    else:
        print("edith isn't here.")
    
def main():
    find_karel(SAMPLE_ROSTER)

if __name__ == "__main__":
    main()