import React from "react";

export default function HeatmapViewer({ heatmapUrl }) {
  if (!heatmapUrl) return null;

  return (
    <div className="mt-8 text-center">
      <h3 className="text-lg font-semibold text-gray-800 mb-4">
        Grad-CAM Heatmap
      </h3>
      <img
        src={`https://pneumonia-diagnosis-assistant-2.onrender.com${heatmapUrl}`}
        alt="Heatmap"
        className="rounded-2xl shadow-lg border border-gray-200 mx-auto"
      />
    </div>
  );
}
