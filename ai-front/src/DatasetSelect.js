import React, { useState, useEffect } from 'react';
import axios from 'axios';

function DynamicSelect({ apiUrl, placeholder }) {
    const [options, setOptions] = useState([]);
    const [selectedValue, setSelectedValue] = useState(''); // Keep empty initially

    useEffect(() => {
        const fetchOptions = async () => {
            try {
                const response = await axios.get(apiUrl, { responseType: 'text' }); // Fetch CSV as text
                const csvData = response.data;

                // Parse CSV manually (assuming single-column CSV, one option per line)
                const parsedOptions = csvData
                    .split('\n') // Split by new line
                    .map((line) => line.trim()) // Trim spaces
                    .filter((line) => line); // Remove empty lines

                setOptions(parsedOptions);
            } catch (error) {
                console.error('Error fetching or parsing:', error);
            }
        };

        fetchOptions();
    }, [apiUrl]);

    const handleChange = (e) => {
        setSelectedValue(e.target.value);
    };

    return (
        <select value={selectedValue} onChange={handleChange}>
            {/* Placeholder, not selectable */}
            <option value="" disabled hidden>
                {placeholder}
            </option>
            {/* Render actual options */}
            {options.map((option, index) => (
                <option key={index} value={option}>
                    {option}
                </option>
            ))}
        </select>
    );
}

export default DynamicSelect;
