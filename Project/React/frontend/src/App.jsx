import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Home, Grid, Calendar, MapPin, Calculator, RotateCcw } from 'lucide-react';
import './App.css'; 

export default function App() {
  const initialFormState = {
    sqrft: '',
    rooms: '',
    year_built: '',
    location_score: ''
  };

  const [formData, setFormData] = useState(initialFormState);
  const [prediction, setPrediction] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value === '' ? '' : parseFloat(e.target.value)
    });
  };

  const handleReset = () => {
    setFormData(initialFormState);
    setPrediction(null);
  };

  const handlePredict = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      const response = await fetch('http://localhost:8000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      
      if (!response.ok) throw new Error("Network response was not ok");
      
      const data = await response.json();
      setPrediction(data.predicted_price);
    } catch (error) {
      console.error("Prediction failed:", error);
      alert("Failed to fetch prediction. Ensure FastAPI is running on port 8000.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
        className="glass-card"
      >
        <div className="header-section">
          <motion.div 
            initial={{ scale: 0.8 }}
            animate={{ scale: 1 }}
            transition={{ type: "spring", stiffness: 200 }}
            className="icon-wrapper"
          >
            <Home size={32} />
          </motion.div>
          <h1 className="title">AI Price Engine</h1>
          <p className="subtitle">Predict real estate value instantly</p>
        </div>

        <form onSubmit={handlePredict}>
          <div className="input-grid">
            <div className="input-group">
              <label className="input-label">
                <Grid size={16} color="var(--accent-blue)" /> Square Footage
              </label>
              <input 
                type="number" name="sqrft"
                value={formData.sqrft} onChange={handleChange}
                placeholder="e.g. 1500"
                className="form-input"
                required
              />
            </div>

            <div className="input-group">
              <label className="input-label">
                <Home size={16} color="var(--accent-purple)" /> Number of Rooms
              </label>
              <input 
                type="number" name="rooms"
                value={formData.rooms} onChange={handleChange}
                placeholder="e.g. 3"
                className="form-input"
                required
              />
            </div>

            <div className="input-group">
              <label className="input-label">
                <Calendar size={16} color="var(--accent-pink)" /> Year Built
              </label>
              <input 
                type="number" name="year_built"
                value={formData.year_built} onChange={handleChange}
                placeholder="e.g. 2010"
                className="form-input"
                required
              />
            </div>

            <div className="input-group">
              <label className="input-label">
                <MapPin size={16} color="var(--accent-green)" /> Location Score (1-10)
              </label>
              <input 
                type="number" step="0.1" name="location_score" min="1" max="10"
                value={formData.location_score} onChange={handleChange}
                placeholder="e.g. 7.5"
                className="form-input"
                required
              />
            </div>
          </div>

          <div className="button-group">
            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              type="button"
              onClick={handleReset}
              className="btn btn-reset"
            >
              <RotateCcw size={18} />
              Reset
            </motion.button>

            <motion.button
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              disabled={isLoading}
              type="submit"
              className="btn btn-submit"
            >
              <Calculator size={18} />
              {isLoading ? 'Processing Tensor...' : 'Predict Value'}
            </motion.button>
          </div>
        </form>

        {prediction !== null && (
          <motion.div 
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            className="result-card"
          >
            <h3 className="result-title">Estimated Market Value</h3>
            <p className="result-value">
              <span className="currency-symbol">$</span>
              {prediction.toLocaleString('en-US')}
            </p>
          </motion.div>
        )}
      </motion.div>
    </div>
  );
}