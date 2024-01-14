export default function Welcome( {scrollToSection} ) {
    return (
      <section className="min-h-screen text-center pt-10 md:pt-5 pl-10 md:pl-20 pr-10 md:pr-20">
        <h1 className="text-cyan-300 text-5xl md:text-7xl font-bold mb-4">Real Resumes.</h1>
        <h2 className="text-gray-400 text-4xl md:text-6xl font-bold mb-4">Anonymized by Us.</h2>
        <h2 className="text-gray-300 text-4xl md:text-6xl font-bold mb-4">Rated by You.</h2>
        <p className="text-gray-400 text-xl md:text-2xl font-bold mb-4">Find inspiration from real resumes from people from all over the globe. Or contribute your own to get feedback from our community. All completely anonymous. </p>
        <button 
          onClick={() => scrollToSection('upload')}
          className="border-2 border-cyan-400 text-cyan-400 py-2 px-4 font-bold hover:bg-cyan-400 hover:text-black transition duration-200"
        >
          Get Started
        </button>
      </section>
    )
  }
  