import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    async function fetchVideos() {
      try {
        const response = await fetch('/videos/videos.json'); // Fetching the static JSON file
        if (!response.ok) {
          throw new Error(`Failed to fetch videos: ${response.status} ${response.statusText}`);
        }
        const videoObjects = await response.json();
        console.log(videoObjects);
        setVideos(videoObjects);
      } catch (error) {
        console.error('Error fetching videos:', error.message);
      }
    }
  
    fetchVideos();
  }, []);

  return (
    <>
      <h1>Staquaponics</h1>
      {videos.map((video, index) => (
        
        (video.type === "mp4" && (
          <div key={index}>
            <h2>{video.name}</h2>
            <video controls>
              <source src={`/videos/${video.name}`} type="video/mp4" />
              Your browser does not support the video tag.
            </video>
          </div>
        ))
      ))}
    </>
  );
}

export default App;
