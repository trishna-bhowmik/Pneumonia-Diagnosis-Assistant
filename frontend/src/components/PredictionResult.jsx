import React from "react";

const PredictionResult = ({ result }) => {
  if (!result) return null;

  const isPneumonia = result.prediction.toLowerCase() === "pneumonia";

  return (
    <div className="bg-gray-50 rounded-2xl p-6 shadow-inner mt-6 text-center">
      <h3 className="text-xl font-semibold text-gray-800 mb-4">
        Diagnosis Result
      </h3>

      <p
        className={`text-2xl font-bold mb-2 ${
          isPneumonia ? "text-red-600" : "text-green-600"
        }`}
      >
        {isPneumonia ? "⚠️ Pneumonia Detected" : "✅ Normal"}
      </p>

      <div className="mt-4 space-y-2 text-gray-700">
        <p>
          <span className="font-medium">Confidence:</span>{" "}
          {(result.confidence * 100).toFixed(2)}%
        </p>
        <div className="w-full bg-gray-200 rounded-full h-3 mt-3">
          <div
            className={`h-3 rounded-full ${
              isPneumonia ? "bg-red-500" : "bg-green-500"
            }`}
            style={{ width: `${(result.confidence * 100).toFixed(0)}%` }}
          />
        </div>
      </div>
    </div>
  );
};

export default PredictionResult;
