import React, { useState } from 'react';

function ModuleSelect({ placeholder }) {
    const [selectedValue, setSelectedValue] = useState('');

    // Predefined static options
    const modelOptions = ['Model A', 'Model B', 'Model C'];

    const handleChange = (e) => {
        setSelectedValue(e.target.value);
    };

    return (
        <select value={selectedValue} onChange={handleChange}>
            {/* Placeholder option */}
            <option value="" disabled hidden>
                {placeholder}
            </option>

            {/* Predefined static options */}
            {modelOptions.map((option, index) => (
                <option key={index} value={option}>
                    {option}
                </option>
            ))}
        </select>
    );
}

export default ModuleSelect;