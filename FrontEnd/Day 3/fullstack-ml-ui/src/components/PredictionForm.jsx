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
      // Simulating a POST request to a backend endpoint
      // Later, this will point to: "http://127.0.0.1:8000/predict"
      const response = await axios.post("https://jsonplaceholder.typicode.com/posts", {
        feature1: Number(feature1),
        feature2: Number(feature2),
      });

      // Simulate receiving a prediction score back from the server
      // (Using dummy logic for now: sum of inputs * 1.5)
      const simulatedPrediction = (Number(feature1) + Number(feature2)) * 1.5;

      setPredictionResult({
        prediction: simulatedPrediction,
        status: "Success",
        serverMessage: response.statusText,
      });
    } catch (err) {
      setError("Failed to connect to the backend server. Please try again.");
      console.error("API Error:", err);
    } finally {
      setLoading(false);
    }
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

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Processing Inference..." : "Run Prediction"}
          </button>
        </form>

        {/* Error State Display */}
        {error && <p className="error-message">{error}</p>}

        {/* Success Result Display */}
        {predictionResult && (
          <div className="result-box">
            <h3>Prediction Result:</h3>
            <p>Estimated Output: <strong>{predictionResult.prediction}</strong></p>
            <p className="status-success">Status: Connected & Processed Successfully</p>
          </div>
        )}
      </section>
    </main>
  );
}

export default PredictionForm;