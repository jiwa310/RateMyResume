import React, { useState, useEffect } from 'react'
import Welcome from '../components/Welcome'
import Header from '../components/Header'
import Explore from '../components/Explore'
import Upload from '../components/Upload'
// https://firebase.google.com/docs/web/setup#available-libraries
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getStorage, ref } from "firebase/storage";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBPht2FSlyZAAtkbK9BKi9-tEDrvn-Vis4",
  authDomain: "ratemyresume-sbhacks.firebaseapp.com",
  projectId: "ratemyresume-sbhacks",
  storageBucket: "ratemyresume-sbhacks.appspot.com",
  messagingSenderId: "607688078150",
  appId: "1:607688078150:web:167acd763c12c3091b6b47",
  measurementId: "G-DSK4JES502",
  storageBucket: "gs://ratemyresume-sbhacks.appspot.com"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
// Get a reference to the storage service, which is used to create references in your storage bucket
const storage = getStorage();
// Create a storage reference from our storage service
const storageRef = ref(storage);

export default function Home() {
  const exploreRef = React.createRef();
  const uploadRef = React.createRef();

  const scrollToSection = (section) => {
    let offset = -75;
    switch(section) {
      case 'upload':
        if (uploadRef.current) {
          const top = uploadRef.current.getBoundingClientRect().top + window.pageYOffset + offset;
          window.scrollTo({ top: top, behavior: 'smooth' });
        }
        break;
      case 'explore':
        if (exploreRef.current) {
          const top = exploreRef.current.getBoundingClientRect().top + window.pageYOffset + offset;
          window.scrollTo({ top: top, behavior: 'smooth' });
        }
        break;
    }
  }
  

  const [loading, setLoading] = useState(false);
    return (
      <div className={`container font-montserrat transition-opacity duration-1000 ${loading ? 'opacity-0' : 'opacity-100'}`}>
        <Header scrollToSection={scrollToSection} />
        <Welcome scrollToSection={scrollToSection} />
        <div ref={uploadRef}><Upload /></div>
        <div ref={exploreRef}><Explore /></div>
      </div>
    )
}

