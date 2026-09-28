// src/components/PredictionForm.jsx
import { useState } from "react";
import "./PredictionForm.css";

function PredictionForm() {
  // Declare state variables for input features and prediction results
  const [feature1, setFeature1] = useState("");
  const [feature2, setFeature2] = useState("");
  const [submittedData, setSubmittedData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Store submitted values to pass down via props or display
    setSubmittedData({
      f1: feature1,
      f2: feature2,
    });
    console.log("Form Submitted:", { feature1, feature2 });
  };

  return (
    <main className="form-container">
      <section className="card">
        <h2>Model Feature Input</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="feature1">Primary Feature (e.g., Sq Ft / Hours):</label>
            <input 
              type="number" 
              id="feature1" 
              value={feature1}
              onChange={(e) => setFeature1(e.target.value)}
              placeholder="Enter value..." 
              required
            />
          </div>

          <div className="input-group">
            <label htmlFor="feature2">Secondary Feature (e.g., Rooms / Age):</label>
            <input 
              type="number" 
              id="feature2" 
              value={feature2}
              onChange={(e) => setFeature2(e.target.value)}
              placeholder="Enter value..." 
              required
            />
          </div>

          <button type="submit" className="submit-btn">Run Prediction</button>
        </form>

        {/* Conditionally render results if data has been submitted */}
        {submittedData && (
          <div className="result-box">
            <h3>Captured Inputs:</h3>
            <p>Feature 1: {submittedData.f1}</p>
            <p>Feature 2: {submittedData.f2}</p>
            <p className="status-pending">Ready for FastAPI Backend Integration!</p>
          </div>
        )}
      </section>
    </main>
  );
}

export default PredictionForm;