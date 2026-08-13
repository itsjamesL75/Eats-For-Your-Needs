
const findRecipes = async () => {
	const response = await fetch("http://localhost:8000/recipes");

	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}

	return response.json();
};

export default findRecipes;