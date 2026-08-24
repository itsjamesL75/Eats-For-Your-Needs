from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

recipes = [
    {
        "id": 1,
        "name": "Bacon on toast",
        "ingredients": ["Bread", "Bacon", "Butter"],
    },
    {
        "id": 2,
        "name": "Lemon Garlic Chicken with Broccoli",
        "ingredients": ["Butter", "Chicken breast", "Garlic", "Lemon", "Broccoli"],
    },
    {
        "id": 3,
        "name": "Beef Stir-Fry",
        "ingredients": ["Garlic", "Beef", "Vegetable oil", "Bell pepper", "Carrot", "Spring onion", "Ginger", "Soy sauce", "Honey", "Chilli flakes", "Water", "Rice"],
    },
    {
        "id": 4,
        "name": "Slow-Cooked Pulled Pork",
        "ingredients": ["Broccoli", "Vegetable oil", "Pork shoulder", "Paprika", "Garlic powder", "Salt", "Pepper", "Chilli powder", "Barbeque sauce", "Lettuce", "Apple cider vinegar", "Brown sugar", "Stock"],
    },
    {
        "id": 5,
        "name": "Spaghetti Aglio e Olio",
        "ingredients": ["Garlic", "Chilli flakes", "Salt", "Pepper", "Spaghetti pasta", "Olive oil"],
    },
    {
        "id": 6,
        "name": "Avocado and Egg Toast",
        "ingredients": ["Bread", "Lemon", "Salt", "Pepper", "Avocado", "Eggs"],
    },
    {
        "id": 7,
        "name": "Cheesy Garlic Bread",
        "ingredients": ["Bread", "Butter", "Garlic", "Lemon", "Pepper", "Cheese", "Oregano"],
    },
    {
        "id": 8,
        "name": "Tuna and Cucumber Wrap",
        "ingredients": ["Lemon", "Salt", "Pepper", "Tuna", "Tortilla", "Cucumber", "Mayonnaise", "Ketchup"],
    },
    {
        "id": 9,
        "name": "Garlic Butter Chicken with Rice",
        "ingredients": ["Butter", "Chicken breast", "Garlic", "Rice", "Paprika", "Salt", "Pepper", "Olive oil", "Peas"],
    },
    {
        "id": 10,
        "name": "Chicken and Broccoli Stir-Fry",
        "ingredients": ["Garlic", "Broccoli", "Vegetable oil", "Carrot", "Ginger", "Soy sauce", "Honey", "Rice", "Pepper", "Chicken thigh"],
    },
    {
        "id": 11,
        "name": "Lemon Garlic Salmon with Rice",
        "ingredients": ["Butter", "Garlic", "Lemon", "Salt", "Pepper", "Olive oil", "Salmon"],
    },
    {
        "id": 12,
        "name": "Sausage Stir-Fry",
        "ingredients": ["Garlic", "Lemon", "Bell pepper", "Soy sauce", "Paprika", "Salt", "Pepper", "Olive oil", "Oregano", "Sausage", "Onion"],
    },
]

ingredients = [
    {"id": 1, "name": "Bread", "category": "Carbs"},
    {"id": 2, "name": "Rice", "category": "Carbs"},
    {"id": 3, "name": "Potato", "category": "Carbs"},
    {"id": 4, "name": "Sweet potato", "category": "Carbs"},
    {"id": 5, "name": "Penne pasta", "category": "Carbs"},
    {"id": 6, "name": "Spaghetti pasta", "category": "Carbs"},
    {"id": 7, "name": "Chicken breast", "category": "Meats"},
    {"id": 8, "name": "Chicken thigh", "category": "Meats"},
    {"id": 9, "name": "Ground beef", "category": "Meats"},
    {"id": 10, "name": "Beef", "category": "Meats"},
    {"id": 11, "name": "Pork", "category": "Meats"},
    {"id": 12, "name": "Bacon", "category": "Meats"},
    {"id": 13, "name": "Ham", "category": "Meats"},
    {"id": 14, "name": "Sausage", "category": "Meats"},
    {"id": 15, "name": "Lamb", "category": "Meats"},
    {"id": 16, "name": "Salmon", "category": "Fish"},
    {"id": 17, "name": "Tuna", "category": "Fish"},
    {"id": 18, "name": "Avocado", "category": "Fruits"},
    {"id": 19, "name": "Strawberry", "category": "Fruits"},
    {"id": 20, "name": "Raspberry", "category": "Fruits"},
    {"id": 21, "name": "Blueberry", "category": "Fruits"},
    {"id": 22, "name": "Lemon", "category": "Fruits"},
    {"id": 23, "name": "Lime", "category": "Fruits"},
    {"id": 24, "name": "Apple", "category": "Fruits"},
    {"id": 25, "name": "Banana", "category": "Fruits"},
    {"id": 26, "name": "Orange", "category": "Fruits"},
    {"id": 27, "name": "Garlic", "category": "Vegetables"},
    {"id": 28, "name": "Onion", "category": "Vegetables"},
    {"id": 29, "name": "Bell pepper", "category": "Vegetables"},
    {"id": 30, "name": "Carrot", "category": "Vegetables"},
    {"id": 31, "name": "Tomato", "category": "Vegetables"},
    {"id": 32, "name": "Cucumber", "category": "Vegetables"},
    {"id": 33, "name": "Peas", "category": "Vegetables"},
    {"id": 34, "name": "Broccoli", "category": "Vegetables"},
    {"id": 35, "name": "Lettuce", "category": "Vegetables"},
    {"id": 36, "name": "Spring onion", "category": "Vegetables"},
    {"id": 37, "name": "Eggs", "category": "Dairy and Eggs"},
    {"id": 38, "name": "Butter", "category": "Dairy and Eggs"},
    {"id": 39, "name": "Milk", "category": "Dairy and Eggs"},
    {"id": 40, "name": "Cheese", "category": "Dairy and Eggs"},
    {"id": 41, "name": "Yoghurt", "category": "Dairy and Eggs"},
    {"id": 42, "name": "Sour cream", "category": "Dairy and Eggs"},
    {"id": 43, "name": "Cream", "category": "Dairy and Eggs"},
    {"id": 44, "name": "Ketchup", "category": "Sauces"},
    {"id": 45, "name": "Mustard", "category": "Sauces"},
    {"id": 46, "name": "Mayonnaise", "category": "Sauces"},
    {"id": 47, "name": "Barbeque sauce", "category": "Sauces"},
    {"id": 48, "name": "Garlic powder", "category": "Spices and Seasonings"},
    {"id": 49, "name": "Basil", "category": "Spices and Seasonings"},
    {"id": 50, "name": "Oregano", "category": "Spices and Seasonings"},
    {"id": 51, "name": "Ginger", "category": "Spices and Seasonings"},
    {"id": 52, "name": "Chilli powder", "category": "Spices and Seasonings"},
    {"id": 53, "name": "Chilli flakes", "category": "Spices and Seasonings"},
    {"id": 54, "name": "Paprika", "category": "Spices and Seasonings"},
    {"id": 55, "name": "Olive oil", "category": "Miscellaneous"},
    {"id": 56, "name": "Vegetable oil", "category": "Miscellaneous"},
    {"id": 57, "name": "Stock", "category": "Miscellaneous"},
    {"id": 58, "name": "Tortilla", "category": "Carbs"},
    {"id": 59, "name": "Noodles", "category": "Carbs"},
    {"id": 60, "name": "Soy sauce", "category": "Sauces"},
    {"id": 61, "name": "Honey", "category": "Miscellaneous"},
    {"id": 62, "name": "Water", "category": "Miscellaneous"},
    {"id": 63, "name": "Pork shoulder", "category": "Meats"},
    {"id": 64, "name": "Salt", "category": "Spices and Seasonings"},
    {"id": 65, "name": "Pepper", "category": "Spices and Seasonings"},
    {"id": 66, "name": "Apple cider vinegar", "category": "Miscellaneous"},
    {"id": 67, "name": "Sugar", "category": "Miscellaneous"},
    {"id": 68, "name": "Brown sugar", "category": "Miscellaneous"},
]


def normalize_ingredients(items: list[str]) -> set[str]:
    return {item.strip().lower() for item in items if item and item.strip()}


def build_recipe_match(recipe: dict, selected_ingredients: list[str]) -> dict:
    selected_set = normalize_ingredients(selected_ingredients)
    recipe_set = normalize_ingredients(recipe["ingredients"])

    matched = recipe_set & selected_set
    missing = recipe_set - selected_set

    return {
        "id": recipe["id"],
        "name": recipe["name"],
        "ingredients": recipe["ingredients"],
        "match_count": len(matched),
        "missing_count": len(missing),
    }


def filter_recipes(selected_ingredients: list[str], mode: str, max_missing: int = 0):
    if not selected_ingredients:
        return recipes

    selected_set = normalize_ingredients(selected_ingredients)
    filtered = []

    for recipe in recipes:
        match_summary = build_recipe_match(recipe, selected_ingredients)
        recipe_set = normalize_ingredients(recipe["ingredients"])

        # "all" mode requires all recipe ingredients to be present in the selected ingredients
        # "any" mode requires at least one recipe ingredient to be present in the selected ingredients
        # "best" mode requires the number of missing ingredients to be less than or equal to max_missing
        if mode == "all" and recipe_set.issubset(selected_set):
            filtered.append(match_summary)
        elif mode == "any" and match_summary["match_count"] > 0:
            filtered.append(match_summary)
        elif mode == "best" and match_summary["missing_count"] <= max_missing:
            filtered.append(match_summary)

    # Sorts the filtered recipes based on match count, missing count, and recipe ID
    if mode == "best":
        filtered.sort(
            key=lambda item: (-item["match_count"], item["missing_count"], item["id"])
        )

    return filtered

# Model helps to validate requests before processing them
class RecipeFilterRequest(BaseModel):
    ingredients: list[str]
    mode: str = "all"
    max_missing: int = 0


@app.get("/")
def root():
    return {"message": "Recipe API is running!"}


@app.get("/recipes")
def get_recipes():
    return recipes

@app.get("/ingredients")
def get_ingredients():
    return ingredients


@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe

    raise HTTPException(status_code=404, detail="Recipe not found")


@app.post("/recipes/filter")
def filter_recipes_by_ingredients(request: RecipeFilterRequest):
    if request.mode not in {"all", "any", "best"}:
        raise HTTPException(
            status_code=400,
            detail="mode must be one of: 'all', 'any', 'best'",
        )

    if request.max_missing < 0:
        raise HTTPException(
            status_code=400,
            detail="max_missing must be greater than or equal to 0",
        )

    return filter_recipes(
        request.ingredients,
        request.mode,
        request.max_missing,
    )