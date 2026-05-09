"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""

    return dish_name, set(dish_ingredients)


def check_drinks(drink_name, drink_ingredients):
    """Append Cocktail or Mocktail to drink name."""

    if not ALCOHOLS.intersection(drink_ingredients):
        return f"{drink_name} Mocktail"

    return f"{drink_name} Cocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize dish based on ingredients."""

    ingredient_count = len(dish_ingredients)

    for category, category_name in (
        (VEGAN, "VEGAN"),
        (VEGETARIAN, "VEGETARIAN"),
        (PALEO, "PALEO"),
        (KETO, "KETO"),
        (OMNIVORE, "OMNIVORE"),
    ):

        if len(dish_ingredients.intersection(category)) == ingredient_count:
            return f"{dish_name}: {category_name}"

    return None


def tag_special_ingredients(dish):
    """Return dish name and special ingredients."""

    return (
        dish[0],
        SPECIAL_INGREDIENTS.intersection(dish[1]),
    )


def compile_ingredients(dishes):
    """Create a master list of ingredients."""

    ingredients = set()

    for dish in dishes:
        ingredients |= dish

    return ingredients


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from dishes list."""

    appetizers = set(appetizers)

    return [
        dish
        for dish in set(dishes)
        if dish not in appetizers
    ]


def singleton_ingredients(dishes, intersection):
    """Return ingredients appearing in only one dish."""

    result = set()

    for dish in dishes:
        result |= (dish - intersection)

    return result