const DropdownMenu = ({ id, label, values, className = "rounded border border-gray-300 px-2 py-1", ...rest }) => {
	return (
		<>
			<label htmlFor={id} className="font-semibold">{label}</label>
			<select id={id} className={className} {...rest}>
				{values.map((value) => (
					<option key={value} value={value}>
						{value}
					</option>
				))}
			</select>
		</>
	);
};

export default DropdownMenu;
