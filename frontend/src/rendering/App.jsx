
import { useState, useEffect } from "react";
import findItemList from "../utils/findItemList";
import RecipeCard from "../components/ui/RecipeCard";


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
			{ingredients.map((ingredient) => (
				<div key={ingredient.id}>
					<h2>{ingredient.name}</h2>
					<p>Category: {ingredient.category}</p>
				</div>
			))}
		</div>
	)
}

export default App