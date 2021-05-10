def main():
    person_01 = "Anton"
    age_person_01 = 21

    person_02 = "Beth"
    age_person_02 = age_person_01 + 6

    person_03 = "Chen"
    age_person_03 = age_person_02 + 20

    person_04 = "Drew"
    age_person_04 = age_person_03 + age_person_01

    person_05 = "Ethan"
    age_person_05 = age_person_03

    print(f"{person_01} is {age_person_01}")
    print(f"{person_02} is {age_person_02}")
    print(f"{person_03} is {age_person_03}")
    print(f"{person_04} is {age_person_04}")
    print(f"{person_05} is {age_person_05}")


if __name__ == '__main__':
    main()