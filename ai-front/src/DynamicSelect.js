import React, { useState, useEffect } from 'react';

function DynamicSelect({ apiUrl, placeholder }) {
    const [options, setOptions] = useState([]);

    useEffect(() => {
        const fetchOptions = async () => {
            try {
                const response = await fetch(apiUrl);
                const data = await response.json();
                setOptions(data);
            } catch (error) {
                console.error('Error fetching options:', error);
            }
        };

        fetchOptions();
    }, [apiUrl]);

    return (
        <select>
            <option>{placeholder}</option>
            {options.map((option, index) => (
                <option key={index} value={option}>
                    {option}
                </option>
            ))}
        </select>
    );
}

export default DynamicSelect;
