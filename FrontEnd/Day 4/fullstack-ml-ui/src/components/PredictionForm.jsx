// src/components/PredictionForm.jsx
import { useState } from "react";
import axios from "axios";
import "./PredictionForm.css";

function PredictionForm() {
  const [feature1, setFeature1] = useState("");
  const [feature2, setFeature2] = useState("");
  const [predictionResult, setPredictionResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPredictionResult(null);

    try {
      // Mock API call (Ready to be replaced with FastAPI endpoint: http://127.0.0.1:8000/predict)
      const response = await axios.post("https://jsonplaceholder.typicode.com/posts", {
        feature1: Number(feature1),
        feature2: Number(feature2),
      });

      const simulatedPrediction = (Number(feature1) + Number(feature2)) * 1.5;

      setPredictionResult({
        prediction: simulatedPrediction.toFixed(2),
        status: "Success",
      });
    } catch (err) {
      setError("Failed to connect to the backend server. Please verify your connection.");
      console.error("API Error:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setFeature1("");
    setFeature2("");
    setPredictionResult(null);
    setError(null);
  };

  return (
    <main className="form-container">
      <section className="card">
        <h2>ML Model Feature Input</h2>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="feature1">Primary Feature (e.g., Sq Ft / Hours):</label>
            <input 
              type="number" 
              id="feature1" 
              value={feature1}
              onChange={(e) => setFeature1(e.target.value)}
              placeholder="Enter value (e.g., 1200)..." 
              min="0"
              step="any"
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
              placeholder="Enter value (e.g., 3)..." 
              min="0"
              step="any"
              required
            />
          </div>

          <div className="button-group">
            <button type="submit" className="submit-btn" disabled={loading}>
              {loading ? "Processing..." : "Run Prediction"}
            </button>
            <button type="button" className="reset-btn" onClick={handleReset}>
              Reset
            </button>
          </div>
        </form>

        {error && <p className="error-message">{error}</p>}

        {predictionResult && (
          <div className="result-box">
            <h3>Prediction Result:</h3>
            <p>Estimated Output: <strong>{predictionResult.prediction}</strong></p>
            <p className="status-success">Status: Ready for FastAPI Backend</p>
          </div>
        )}
      </section>
    </main>
  );
}

export default PredictionForm;