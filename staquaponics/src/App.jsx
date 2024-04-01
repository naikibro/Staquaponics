import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    async function fetchVideos() {
      try {
        const response = await fetch('/videos/');
        const data = await response.json();
        setVideos(data);
      } catch (error) {
        console.error('Error fetching videos:', error);
      }
    }

    fetchVideos();
  }, []);

  return (
    <>
      <h1>Staquaponics</h1>
      {videos.map((video, index) => (
        <div key={index}>
          <h2>{video.name}</h2>
          <video controls>
            <source src={`/videos/${video.fileName}`} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      ))}
    </>
  );
}

export default App;
