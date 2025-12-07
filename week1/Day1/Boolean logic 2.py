def calculate_animal_years(human_years):
    if human_years < 1:
        print("humanyears doit être supérieur ou égal à 1")
        return None

    cat_years = 15
    dog_years = 15

    if human_years > 1:
        cat_years += 9
        dog_years += 9

    if human_years > 2:
        cat_years += (human_years - 2) * 4
        dog_years += (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

print(calculate_animal_years(10))
print(calculate_animal_years(1))
print(calculate_animal_years(2))