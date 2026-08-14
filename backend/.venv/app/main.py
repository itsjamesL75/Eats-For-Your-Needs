from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
        "ingredients": ["Bread", "Bacon", "Butter", "Chicken breast"], 
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
    }
]

ingredients = [
    {
        "id": 1,
        "name": "Bread",
        "category": "Carbs"
    },
    {
        "id": 2,
        "name": "Rice",
        "category": "Carbs"
    },
    {
        "id": 3,
        "name": "Potato",
        "category": "Carbs"
    },
    {
        "id": 4,
        "name": "Sweet potato",
        "category": "Carbs"
    },
    {
        "id": 5,
        "name": "Penne pasta",
        "category": "Carbs"
    },
    {
        "id": 6,
        "name": "Spaghetti pasta",
        "category": "Carbs"
    },
    {
        "id": 7,
        "name": "Chicken breast",
        "category": "Meats"
    },
    {
        "id": 8,
        "name": "Chicken thigh",
        "category": "Meats"
    },
    {
        "id": 9,
        "name": "Ground beef",
        "category": "Meats"
    },
    {
        "id": 10,
        "name": "Beef",
        "category": "Meats"
    },
    {
        "id": 11,
        "name": "Pork",
        "category": "Meats"
    },
    {
        "id": 12,
        "name": "Bacon",
        "category": "Meats"
    },
    {
        "id": 13,
        "name": "Ham",
        "category": "Meats"
    },
    {
        "id": 14,
        "name": "Sausage",
        "category": "Meats"
    },
    {
        "id": 15,
        "name": "Lamb",
        "category": "Meats"
    },
    {
        "id": 16,
        "name": "Salmon",
        "category": "Fish"
    },
    {
        "id": 17,
        "name": "Tuna",
        "category": "Fish"
    },
    {
        "id": 18,
        "name": "Avocado",
        "category": "Fruits"
    },
    {
        "id": 19,
        "name": "Strawberry",
        "category": "Fruits"
    },
    {
        "id": 20,
        "name": "Raspberry",
        "category": "Fruits"
    },
    {
        "id": 21,
        "name": "Blueberry",
        "category": "Fruits"
    },
    {
        "id": 22,
        "name": "Lemon",
        "category": "Fruits"
    },
    {
        "id": 23,
        "name": "Lime",
        "category": "Fruits"
    },
    {
        "id": 24,
        "name": "Apple",
        "category": "Fruits"
    },
    {
        "id": 25,
        "name": "Banana",
        "category": "Fruits"
    },
    {
        "id": 26,
        "name": "Orange",
        "category": "Fruits"
    },
    {
        "id": 27,
        "name": "Garlic",
        "category": "Vegetables"
    },
    {
        "id": 28,
        "name": "Onion",
        "category": "Vegetables"
    },
    {
        "id": 29,
        "name": "Bell pepper",
        "category": "Vegetables"
    },
    {
        "id": 30,
        "name": "Carrot",
        "category": "Vegetables"
    },
    {
        "id": 31,
        "name": "Tomato",
        "category": "Vegetables"
    },
    {
        "id": 32,
        "name": "Cucumber",
        "category": "Vegetables"
    },
    {
        "id": 33,
        "name": "Peas",
        "category": "Vegetables"
    },
    {
        "id": 34,
        "name": "Broccoli",
        "category": "Vegetables"
    },
    {
        "id": 35,
        "name": "Lettuce",
        "category": "Vegetables"
    },
    {
        "id": 36,
        "name": "Spring onion",
        "category": "Vegetables"
    },
    {
        "id": 37,
        "name": "Eggs",
        "category": "Dairy and Eggs"
    },
    {
        "id": 38,
        "name": "Butter",
        "category": "Dairy and Eggs"
    },
    {
        "id": 39,
        "name": "Milk",
        "category": "Dairy and Eggs"
    },
    {
        "id": 40,
        "name": "Cheese",
        "category": "Dairy and Eggs"
    },
    {
        "id": 41,
        "name": "Yoghurt",
        "category": "Dairy and Eggs"
    },
    {
        "id": 42,
        "name": "Sour cream",
        "category": "Dairy and Eggs"
    },
    {
        "id": 43,
        "name": "Cream",
        "category": "Dairy and Eggs"
    },
    {
        "id": 44,
        "name": "Ketchup",
        "category": "Sauces"
    },
    {
        "id": 45,
        "name": "Mustard",
        "category": "Sauces"
    },
    {
        "id": 46,
        "name": "Mayonnaise",
        "category": "Sauces"
    },
    {
        "id": 47,
        "name": "Barbeque sauce",
        "category": "Sauces"
    },
    {
        "id": 48,
        "name": "Garlic powder",
        "category": "Spices and Seasonings"
    },
    {
        "id": 49,
        "name": "Basil",
        "category": "Spices and Seasonings"
    },
    {
        "id": 50,
        "name": "Oregano",
        "category": "Spices and Seasonings"
    },
    {
        "id": 51,
        "name": "Ginger",
        "category": "Spices and Seasonings"
    },
    {
        "id": 52,
        "name": "Chilli powder",
        "category": "Spices and Seasonings"
    },
    {
        "id": 53,
        "name": "Chilli flakes",
        "category": "Spices and Seasonings"
    },
    {
        "id": 54,
        "name": "Paprika",
        "category": "Spices and Seasonings"
    },
    {
        "id": 55,
        "name": "Olive oil",
        "category": "Miscellaneous"
    },
    {
        "id": 56,
        "name": "Vegetable oil",
        "category": "Miscellaneous"
    },
    {
        "id": 57,
        "name": "Stock",
        "category": "Miscellaneous"
    },
    {
        "id": 58,
        "name": "Tortilla",
        "category": "Carbs"
    },
    {
        "id": 59,
        "name": "Noodles",
        "category": "Carbs"
    },
    {
        "id": 60,
        "name": "Soy sauce",
        "category": "Sauces"
    },
    {
        "id": 61,
        "name": "Honey",
        "category": "Miscellaneous"
    },
    {
        "id": 62,
        "name": "Water",
        "category": "Miscellaneous"
    },
    {
        "id": 63,
        "name": "Pork shoulder",
        "category": "Meats"
    },
    {
        "id": 64,
        "name": "Salt",
        "category": "Spices and Seasonings"
    },
    {
        "id": 65,
        "name": "Pepper",
        "category": "Spices and Seasonings"
    },
    {
        "id": 66,
        "name": "Apple cider vinegar",
        "category": "Miscellaneous"
    },
    {
        "id": 67,
        "name": "Sugar",
        "category": "Miscellaneous"
    },
    {
        "id": 68,
        "name": "Brown sugar",
        "category": "Miscellaneous"
    },
]

@app.get("/")
def root():
    return {"message": "Recipe API is running!"}


@app.get("/recipes")
def get_recipes():
    return recipes

@app.get("/ingredients")
def get_ingredients():
    return ingredients