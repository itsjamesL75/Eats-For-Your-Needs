const RecipeCard = ({ recipe }) => {
    return (
        <div className="recipe-card">
            <h2 class='font-bold underline'>{recipe.name}</h2>

            <ul class="list-disc pl-5">
                {recipe.ingredients.map((ingredient, index) => (
                    <li key={index}>{ingredient}</li>
                ))}
            </ul>
        </div>
    );
}

export default RecipeCard;