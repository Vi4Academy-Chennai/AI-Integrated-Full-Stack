// src/components/PredictionForm.jsx
import "./PredictionForm.css";

function PredictionForm() {
  return (
    <main className="form-container">
      <section className="card">
        <h2>Model Feature Input</h2>
        <form onSubmit={(e) => e.preventDefault()}>
          <div className="input-group">
            <label htmlFor="feature1">Primary Feature (e.g., Sq Ft / Hours):</label>
            <input type="number" id="feature1" placeholder="Enter value..." />
          </div>

          <div className="input-group">
            <label htmlFor="feature2">Secondary Feature (e.g., Rooms / Age):</label>
            <input type="number" id="feature2" placeholder="Enter value..." />
          </div>

          <button type="submit" className="submit-btn">Run Prediction</button>
        </form>
      </section>
    </main>
  );
}

export default PredictionForm;