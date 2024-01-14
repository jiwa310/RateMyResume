import React, { useState, useEffect } from 'react'
import Welcome from '../components/Welcome'
import Header from '../components/Header'
import Explore from '../components/Explore'
import Upload from '../components/Upload'
// import { connectToDatabase } from '../utils/mongodb'

export default function Home() {
  const exploreRef = React.createRef();
  const uploadRef = React.createRef();

  useEffect(() => {
    const hash = window.location.hash;
    let offset = -75; 
    if (hash === '#explore') {
      const top = exploreRef.current.getBoundingClientRect().top + window.pageYOffset + offset;
      window.scrollTo({ top: top, behavior: 'smooth' });
    } else if (hash === '#upload') {
      const top = uploadRef.current.getBoundingClientRect().top + window.pageYOffset + offset;
      window.scrollTo({ top: top, behavior: 'smooth' });
    }
    history.replaceState(null, null, ' ');
  }, []);

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
