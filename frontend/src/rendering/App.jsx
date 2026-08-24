
import { useState, useEffect } from "react";
import findItemList from "../utils/findItemList";
import RecipeCard from "../components/ui/RecipeCard";
import Checkbox from "../components/ui/Checkbox";

function App() {
	const [recipes, setRecipes] = useState([]);
	const [displayedRecipes, setDisplayedRecipes] = useState([]);
	const [ingredients, setIngredients] = useState([]);
	const [selectedIngredients, setSelectedIngredients] = useState([]);
	const [selectedMode, setSelectedMode] = useState("all");
	const [maxMissing, setMaxMissing] = useState(1);

	useEffect(() => {
		const loadRecipes = async () => {
			try {
				const data = await findItemList("recipes");
				setRecipes(data);
				setDisplayedRecipes(data);
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

	useEffect(() => {
		const fetchMatchingRecipes = async () => {
			if (!recipes.length) {
				return;
			}

			if (selectedIngredients.length === 0) {
				setDisplayedRecipes(recipes);
				return;
			}

			try {
				const response = await fetch("http://localhost:8000/recipes/filter", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
					},
					body: JSON.stringify({
						ingredients: selectedIngredients.map((ingredient) => ingredient.name),
						mode: selectedMode,
						max_missing: selectedMode === "best" ? maxMissing : 0,
					}),
				});

				if (!response.ok) {
					throw new Error(`HTTP error! status: ${response.status}`);
				}

				const data = await response.json();
				setDisplayedRecipes(data);
			} catch (error) {
				console.error("Error fetching filtered recipes:", error);
			}
		};

		fetchMatchingRecipes();
	}, [recipes, selectedIngredients, selectedMode, maxMissing]);

	const categorisedIngredients = ingredients.reduce((acc, ingredient) => {
		if (!acc[ingredient.category]) {
			acc[ingredient.category] = [];
		}
		acc[ingredient.category].push(ingredient);
		return acc;
	}, {});

	Object.keys(categorisedIngredients).forEach((category) => {
		categorisedIngredients[category].sort((a, b) => a.name.localeCompare(b.name));
	});

	// Checks if the checked/unchecked ingredient is in the current list or not and will add/remove it from the list accordingly via filtering the id. 
	const handleIngredientToggle = (ingredient, isChecked) => {
		setSelectedIngredients((prevSelectedIngredients) => {
			const nextSelectedIngredients = isChecked
				? [...prevSelectedIngredients, ingredient]
				: prevSelectedIngredients.filter((selectedIngredient) => selectedIngredient.id !== ingredient.id);

			console.log("Selected ingredients:", nextSelectedIngredients);
			return nextSelectedIngredients;
		});
	};

	const ingredientsIntoCheckboxes = (ingredient) => (
		<div key={ingredient.id} className="w-full">
			<Checkbox 
				id={ingredient.id}
				label={ingredient.name}
				isDefaultChecked={false}
				isDisabled={false}
				onChange = {
					(event) => handleIngredientToggle(ingredient, event.target.checked)
				}
			/>
		</div>
	);

	const categoriesIntoLists = (category) => (
		<div key={category} className="mb-6">
			<h3 className="text-xl font-bold">{category}</h3>
			<div className="mt-2 flex flex-col gap-2">
				{categorisedIngredients[category].map(ingredientsIntoCheckboxes)}
			</div>
		</div>
	);

	const handleSubmit = (event) => {
		event.preventDefault();
	};

	const handleModeChange = (event) => {
		const nextMode = event.target.value;

		if (nextMode === "best") {
			setMaxMissing(1);
		}

		setSelectedMode(nextMode);
	};

	const handleMaxMissingChange = (event) => {
		const nextMaxMissing = Number(event.target.value);

		if (nextMaxMissing === 0) {
			setSelectedMode("all");
			setMaxMissing(1);
			return;
		}

		setMaxMissing(nextMaxMissing);
	};

	return (
		<form onSubmit={handleSubmit}>
			<div className="mb-6 flex items-center gap-4">
				<label htmlFor="response-mode" className="mr-3 font-semibold">Response mode:</label>
				<select
					id="response-mode"
					value={selectedMode}
					onChange={handleModeChange}
					className="rounded border border-gray-300 px-2 py-1"
				>
					<option value="all">all</option>
					<option value="any">any</option>
					<option value="best">best</option>
				</select>

				{selectedMode === "best" && (
					<>
						<label htmlFor="max-missing" className="font-semibold">Max missing:</label>
						<select
							id="max-missing"
							value={maxMissing}
							onChange={handleMaxMissingChange}
							className="rounded border border-gray-300 px-2 py-1"
						>
							<option value={0}>0</option>
							<option value={1}>1</option>
							<option value={2}>2</option>
							<option value={3}>3</option>
						</select>
					</>
				)}
			</div>

			<div>
				{Object.keys(categorisedIngredients).map(categoriesIntoLists)}
			</div>

			<div className="recipe-list mt-8">
				{displayedRecipes.map((recipe) => (
					<RecipeCard key={recipe.id} recipe={recipe} />
				))}
			</div>
		</form>
	);
}

export default App;