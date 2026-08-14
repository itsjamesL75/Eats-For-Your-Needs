
import { useState, useEffect } from "react";
import findItemList from "../utils/findItemList";
import RecipeCard from "../components/ui/RecipeCard";
import Checkbox from "../components/ui/Checkbox";


function App() {
	const [recipes, setRecipes] = useState([]);
	const [ingredients, setIngredients] = useState([]);

	useEffect(() => {
		const loadRecipes = async () => {
			try {
				const data = await findItemList("recipes");
				setRecipes(data);
			} catch (error) {
				console.error("Error fetching recipes:", error);
			}
		};

		const loadIngredients = async () => {
			try {
				const data = await findItemList("ingredients");
				setIngredients(data);
			} catch (error) {
				console.error("Error fetching ingredients:", error);
			}
		};

		loadRecipes();
		loadIngredients();
	}, []);

	const categorisedIngredients = ingredients.reduce((acc, ingredient) => {
		if (!acc[ingredient.category]) {
			acc[ingredient.category] = [];
		}
		acc[ingredient.category].push(ingredient);
		return acc;
	}, {});

	Object.keys(categorisedIngredients).forEach(category => {
		categorisedIngredients[category].sort((a, b) => a.name.localeCompare(b.name));
	});

	const ingredientsIntoCheckboxes = (ingredient) => {
		return (
			<div key={ingredient.id} className="w-full">
				<Checkbox 
					id={ingredient.id}
					label={ingredient.name}
					isDefaultChecked={false}
					isDisabled={false}
				/>
			</div>
		)
	}

	const categoriesIntoLists = (category) => {
		return (
			<div key={category} className="mb-6">
				<h3 className="text-xl font-bold">{category}</h3>
				<div className="mt-2 flex flex-col gap-2">
					{categorisedIngredients[category].map(ingredientsIntoCheckboxes)}
				</div>
			</div>
		)
	}

	return (
		// <div>
		// 	<h1 class="text-3xl font-bold underline">
		// 		Recipes
		// 	</h1>

		// 	<div className="recipe-list">
		// 		{recipes.map((recipe) => (
		// 			<RecipeCard key={recipe.id} recipe={recipe} />
		// 		))}
		// 	</div>
		// </div>
		<div>
			{Object.keys(categorisedIngredients).map(categoriesIntoLists)}
		</div>


	)
}

export default App