import React, { useState, useEffect } from 'react'
import Welcome from '../components/Welcome'
import Header from '../components/Header'

export default function Home() {
  const [loading, setLoading] = useState(false);
  return (
      <div className={`container font-league-spartan transition-opacity duration-1000 ${loading ? 'opacity-0' : 'opacity-100'}`}>
        <Header/>
        <Welcome />
      </div>
  )
}
