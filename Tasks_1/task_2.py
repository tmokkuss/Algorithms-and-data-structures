m = int(input())
fridge = set(input().strip() for _ in range(m))

n = int(input())
possible_recipes = []
for _ in range(n):
    recipe_name = input().strip()
    num_ingredients = int(input())
    ingredients = set(input().strip() for _ in range(num_ingredients))

    if ingredients.issubset(fridge):
        possible_recipes.append(recipe_name)

for recipe_name in possible_recipes:
    print(recipe_name)
