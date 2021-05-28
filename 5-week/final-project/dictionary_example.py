def have_birthday(dict, name):
    print("You're one year older, " + name + "!")
    dict[name] += 1

def main():
    ages = {'Edith': 25, 'Edith': 22, 'Felipe': 50}
    print(ages)
    have_birthday(ages, 'Edith')
    print(ages)
    have_birthday(ages, 'Edith')
    print(ages)

if __name__ == '__main__':
    main()