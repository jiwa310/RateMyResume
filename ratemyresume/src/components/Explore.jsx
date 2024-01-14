import { pdfjs } from 'react-pdf';
import { Document, Page } from 'react-pdf';
import { useState } from 'react';
import Select from 'react-select';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

const pdfFiles = [
  "test1.pdf",
  "test2.pdf",
  "test3.pdf",
  "test4.pdf",
  "test5.pdf",
  "test6.pdf",
  // add more pdf urls
];

const options = [
  { value: 'highestRated', label: 'Highest Rated' },
  { value: 'popular', label: 'Popular' },
  { value: 'newest', label: 'Newest' },
  { value: 'hot', label: 'Hot' },
];

export default function Explore() {
  const [hoverIndex, setHoverIndex] = useState(null);
  const [selectedOption, setSelectedOption] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');

  const handleSelectChange = (option) => {
    setSelectedOption(option);
    // Add your sorting logic here based on the selected option
  };

  return (
    <div className="min-h-screen p-10">
      <h1 className="text-cyan-300 text-5xl md:text-3xl font-bold mb-4">Find Your Inspiration.</h1>
      <div className="flex justify-between mb-4">
        <Select 
          options={options} 
          value={selectedOption} 
          onChange={handleSelectChange} 
        />
        <input 
          type="text" 
          placeholder="Search..." 
          value={searchTerm} 
          onChange={(e) => setSearchTerm(e.target.value)} 
          className="border rounded p-2"
        />
      </div>
      <div className="grid grid-cols-4 gap-4">
        {pdfFiles.map((pdfFile, index) => (
          <div 
            key={index} 
            className={`w-full h-full ${hoverIndex === index ? 'bg-blue-200' : ''}`}
            onMouseEnter={() => setHoverIndex(index)}
            onMouseLeave={() => setHoverIndex(null)}
            onClick={() => window.open(pdfFile)}
          >
            <Document file={pdfFile}>
              <Page pageNumber={1} width={250} renderTextLayer={false} renderAnnotationLayer={false} />
            </Document>
          </div>
        ))}
      </div>
    </div>
  );
}
