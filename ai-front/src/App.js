import './App.css';

function App() {
  return (
      <div className="App">
          <div className="container">
              <div className="search-bar">
                  <input type="text" placeholder="Value"/>
                  <select>
                      <option>Value</option>
                      <option>Option 1</option>
                      <option>Option 2</option>
                  </select>
                  <select>
                      <option>Value</option>
                      <option>Option 1</option>
                      <option>Option 2</option>
                  </select>
                  <button>Button</button>
              </div>
              <div className="result-box"></div>
          </div>
      </div>
  );
}

export default App;
