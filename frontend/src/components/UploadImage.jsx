import React, { useState } from "react";
import { predictImage } from "../services/api";

const UploadImage = ({ onResult }) => {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    try {
      const result = await predictImage(file);
      onResult(result);
    } catch (err) {
      console.error(err);
      alert("Error during prediction. Check backend logs.");
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center gap-4 mb-8">
      <input
        type="file"
        accept="image/*"
        onChange={(e) => setFile(e.target.files[0])}
        className="block w-full text-sm text-gray-600 
                   file:mr-4 file:py-2 file:px-4 
                   file:rounded-xl file:border-0 
                   file:text-sm file:font-semibold 
                   file:bg-blue-100 file:text-blue-700 
                   hover:file:bg-blue-200"
      />
      <button
        onClick={handleUpload}
        disabled={loading}
        className="px-6 py-2 rounded-xl font-semibold 
                   bg-blue-600 text-white hover:bg-blue-700 
                   transition disabled:bg-gray-300"
      >
        {loading ? "Analyzing..." : "Upload & Diagnose"}
      </button>
    </div>
  );
};

export default UploadImage;
