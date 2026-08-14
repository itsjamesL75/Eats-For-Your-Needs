const Checkbox = ({ id, label, isDefaultChecked = false, isDisabled = false, ...rest }) => {
	return (
		<label htmlFor={id} className="flex w-full items-start gap-2">
			<input
				id={id}
				type="checkbox"
				defaultChecked={isDefaultChecked}
				disabled={isDisabled}
				className="appearance-none mt-1 h-4 w-4 shrink-0 rounded-sm border border-blue-200 bg-white accent-blue-500 disabled:cursor-not-allowed disabled:opacity-60"
				{...rest}
			/>
			<span className="text-sm leading-5">{label}</span>
		</label>
	)
};

export default Checkbox;