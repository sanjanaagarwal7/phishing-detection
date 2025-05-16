import React from 'react';
import {useState} from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [url,setUrl]=useState('');
  const [result,setResult]=useState(null);
  const handleSubmit = async (e) => {
  e.preventDefault();
  try {
    const response = await axios.post('http://localhost:5000/api/predict', {
      url: url
    });
    setResult(response.data.result);
    console.log("Response from server:", response.data);
  } catch (e) {
    console.error("Error:", e);
    setResult('error');
  }
};

   function handleChange(e){
      setUrl(e.target.value);
    }

  return(
    <>
    <h1 className="header">Is This Website Safe? Find Out Instantly</h1>
    <div className="main">
    <form onSubmit={handleSubmit}>
      <div>
      <input type="text" placeholder="Enter URL" value={url} onChange={handleChange}/> 
      </div>
      <div>
      <button type="submit">Check</button>
      </div>
   </form>
   </div>
   {result === "1" && <p style={{ color: 'green' }}>✅ Site is Safe</p>}
   {result === "0" && <p style={{ color: 'red' }}>⚠️ Phishing Detected</p>}
    {result === 'error' && <p style={{ color: 'orange' }}>⚠️ Error checking the site</p>}

    </>
  )
}

export default App;
