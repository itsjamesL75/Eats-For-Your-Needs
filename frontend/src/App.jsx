
function App() {
	fetch("http://127.0.0.1:8000/recipes")
		.then(response => response.json())
		.then(data => {
				console.log(data);
		});

	return (
		<div>
			<h1 class="text-3xl font-bold underline">
				Hello world!
			</h1>
		</div>
	)
}

export default App
