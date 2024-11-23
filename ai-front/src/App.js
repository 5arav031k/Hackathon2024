import React, { useState } from 'react';
import './App.css';
import ModuleSelect from './ModuleSelect';
import DatasetSelect from './DatasetSelect';
import axios from "axios";

function App() {
    const [inputValue, setInputValue] = useState("");
    const [serverResponse, setServerResponse] = useState("");

    const handleInputBarSize = (e) => {
        e.target.style.height = "auto"; // Reset the height
        e.target.style.height = `${e.target.scrollHeight}px`;
    };

    const handleSendData = async () => {
        try {
            const jsonData = {
                value: inputValue,
            };

            await axios.post("http://127.0.0.1:5000/api/ai-response", jsonData, {
                headers: { "Content-Type": "application/json" },
                withCredentials: true,
            });

            console.log("Data successfully sent to the server!");
        } catch (error) {
            console.error("Error sending data:", error);
        }
    };

    const handleKeyDown = (event) => {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault(); // Prevent adding a new line in the textarea
            handleSendData(); // Call submit function
        }
    };

    const handleFileChange = async (e) => {
        const selectedFile = e.target.files[0];
        if (!selectedFile) {
            alert("Файл не выбран!");
            return;
        }

        const formData = new FormData();
        formData.append("file", selectedFile);

        try {
            const response = await axios.post("http://127.0.0.1:5000/api/upload-file", formData, {
                headers: { "Content-Type": "multipart/form-data" },
                withCredentials: true,
            });
            setServerResponse(response.data.response || "Файл обработан успешно.");
        } catch (error) {
            console.error("Ошибка при отправке файла:", error);
            setServerResponse("Ошибка при обработке файла.");
        }
    };

    return (
        <div className="App">
            <div className="container">
                <div className="option-bar">
                    <DatasetSelect apiUrl="https://api.example.com/datasets-options" placeholder="Choose dataset"/>
                    <ModuleSelect placeholder="Select  model"/>
                </div>

                <div className="result-box"></div>

                <div className="search-bar">
                    <textarea
                        placeholder="Write your query here..."
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onInput={handleInputBarSize}
                        className="auto-growing-textarea"
                        onKeyDown={handleKeyDown}
                    />

                    <div>
                        <input type="file"
                               accept=".csv"
                               onChange={handleFileChange}
                        />
                        <button onClick={handleSendData}>Submit</button>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default App;
