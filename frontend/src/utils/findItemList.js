
const findItemList = async (itemList) => {
	const response = await fetch(`http://localhost:8000/${itemList}`);

	if (!response.ok) {
		throw new Error(`HTTP error! status: ${response.status}`);
	}

	return response.json();
};

export default findItemList;