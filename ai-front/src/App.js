import React, { useState } from 'react';
import './App.css';
import ModuleSelect from './ModuleSelect';
import DatasetSelect from './DatasetSelect';
import axios from "axios";

function App() {
    const [inputValue, setInputValue] = useState("");

    const handleSendData = async () => {
        try {
            const jsonData = {
                value: inputValue,
            };

            await axios.post("http://127.0.0.1:5000/receive-data", jsonData, {
                headers: { "Content-Type": "application/json" },
            });

            console.log("Данные успешно отправлены на сервер!");
        } catch (error) {
            console.error("Ошибка при отправке данных:", error);
        }
    };
    const handleKeyDown = (e) => {
        if (e.key === "Enter") {
            handleSendData(); // Выполнить отправку данных при нажатии Enter
        }
    };
    return (
        <div className="App">
            <div className="container">
                <div className="search-bar">
                    <input type="text"
                           placeholder="Write your query here..."
                           value={inputValue}
                           onChange={(e) => setInputValue(e.target.value)}
                           onKeyDown={handleKeyDown}
                    />

                    <button onClick={handleSendData}>Submit</button>

                    <DatasetSelect apiUrl="https://api.example.com/options1" placeholder="Choose dataset"/>
                    <ModuleSelect apiUrl="https://api.example.com/options2" placeholder="Select  model"/>

                    <input type="file"/>
                </div>
                <div className="result-box"></div>
            </div>
        </div>
    );
}

export default App;
