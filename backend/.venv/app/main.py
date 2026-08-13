from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
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

@app.get("/")
def root():
    return {"message": "Recipe API is running!"}


@app.get("/recipes")
def get_recipes():
    return recipes