
import { useState, useEffect } from "react";
import findRecipes from "./utils/findRecipes";
import RecipeCard from "./components/ui/RecipeCard";


function App() {
	const [recipes, setRecipes] = useState([]);

	useEffect(() => {
		const loadRecipes = async () => {
			try {
				const data = await findRecipes();
				setRecipes(data);
			} catch (error) {
				console.error("Error fetching recipes:", error);
			}
		};

		loadRecipes();
	}, []);

	return (
		<div>
			<h1 class="text-3xl font-bold underline">
				Recipes
			</h1>

			<div className="recipe-list">
				{recipes.map((recipe) => (
					<RecipeCard key={recipe.id} recipe={recipe} />
				))}
			</div>
		</div>
	)
}

export default App