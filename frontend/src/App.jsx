import { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState("");
  const [imageUrl, setImageUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateImage = async () => {
    setLoading(true);
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/generate/", { prompt });
      setImageUrl(response.data.image_url);
    } catch (error) {
      console.error("Error:", error);
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>AI Image Generator</h1>
      <input 
        type="text" 
        placeholder="Enter prompt..." 
        value={prompt} 
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={generateImage} disabled={loading}>
        {loading ? "Generating..." : "Generate"}
      </button>
      {imageUrl && <img src={imageUrl} alt="Generated" />}
    </div>
  );
}

export default App;
