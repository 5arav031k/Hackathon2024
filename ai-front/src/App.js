import React from 'react';
import './App.css';
import DynamicSelect from './DynamicSelect'

function App() {
    return (
        <div className="App">
            <div className="container">
                <div className="search-bar">
                    <input type="text" placeholder="Value" />

                    {/* First dynamic select */}
                    <DynamicSelect apiUrl="https://api.example.com/options1" placeholder="Select Options 1" />

                    {/* Second dynamic select */}
                    <DynamicSelect apiUrl="https://api.example.com/options2" placeholder="Select Options 2" />

                    <button>Button</button>
                </div>
                <div className="result-box"></div>
            </div>
        </div>
    );
}

export default App;
