import React, { useState } from "react";
import UploadImage from "./components/UploadImage";
import PredictionResult from "./components/PredictionResult";
import HeatmapViewer from "./components/HeatmapViewer";

export default function App() {
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-white flex flex-col items-center py-10">
      <div className="w-full max-w-3xl bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-3xl font-bold text-center text-blue-700 mb-6">
          🩺 Pneumonia Diagnosis Assistant
        </h1>

        <UploadImage onResult={setResult} />

        {result && (
          <>
            <PredictionResult result={result} />
            <HeatmapViewer heatmapUrl={result.heatmap_url} />
          </>
        )}
      </div>
    </div>
  );
}
