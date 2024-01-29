import { pdfjs } from 'react-pdf';
import { Document, Page } from 'react-pdf';
import { useEffect, useState } from 'react';
import axios from 'axios';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

export default function Explore() {
  const [hoverIndex, setHoverIndex] = useState(null);
  const [resumes, setResumes] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/get-all').then((res) => {
      // console.log(res);
      if (res.data) {
        console.log("Resumes Data:", res.data)
        setResumes(res.data)
      } else {
        console.error('Invalid response structure. Data may be missing.');
      }
    });
  }, []);

  const handleRowHover = (index) => {
    setHoverIndex(index);
  };

  return (
    <div className="min-h-screen p-10">
      <h1 className="text-cyan-300 text-center text-3xl md:text-5xl font-bold mb-4">
        Find Your Inspiration.
      </h1>

      <table className="w-full border-collapse border border-gray-200">
        <thead>
          <tr>
            <th className="border p-2">ID</th>
            <th className="border p-2">Description</th>
            <th className="border p-2">Likes</th>
            <th className="border p-2">Major Tag</th>
            {/* Add other columns as needed */}
          </tr>
        </thead>
        <tbody>
          {resumes?.map((item, index) => (
            <tr
              key={index}
              className={hoverIndex === index ? 'bg-cyan-200' : ''}
              onMouseEnter={() => handleRowHover(index)}
              onMouseLeave={() => handleRowHover(null)}
            >
              <td className="border p-2">{item._id}</td>
              <td className="border p-2">{item.description}</td>
              <td className="border p-2">{item.likes}</td>
              <td className="border p-2">{item.major_tag}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}





// import { pdfjs } from 'react-pdf';
// import { Document, Page } from 'react-pdf';
// import { useEffect, useState } from 'react';
// import Select from 'react-select';
// import Link from 'next/link';
// import axios from 'axios'

// pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.min.js`;

// const pdfFiles = [
//   "test1.pdf",
//   "test2.pdf",
//   "test3.pdf",
//   "test4.pdf",
//   "test5.pdf",
//   "test6.pdf",
//   "test7.pdf",
//   // add more pdf urls
// ];

// const options = [
//   { value: 'highestRated', label: 'Highest Rated' },
//   { value: 'popular', label: 'Popular' },
//   { value: 'newest', label: 'Newest' },
//   { value: 'hot', label: 'Hot' },
// ];

// const customStyles = {
//     option: (provided, state) => ({
//       ...provided,
//       color: state.isSelected ? 'white' : 'black',
//       backgroundColor: state.isSelected ? 'black' : 'white',
//     }),
//     control: (provided) => ({
//       ...provided,
//       color: 'black',
//     }),
//   };

// export default function Explore() {
//   const [hoverIndex, setHoverIndex] = useState(null);
//   const [selectedOption, setSelectedOption] = useState(null);
//   const [searchTerm, setSearchTerm] = useState('');

//   useEffect( () => {
//     axios.get('http://127.0.0.1:8000/get-all').then(res => {
//       console.log(res)
//     });
//   }, [])

//   const handleSelectChange = (option) => {
//     setSelectedOption(option);
//     // Add your sorting logic here based on the selected option
//   };

//   return (
//     <div className="min-h-screen p-10">
//       <h1 className="text-cyan-300 text-center text-3xl md:text-5xl font-bold mb-4">Find Your Inspiration.</h1>
//       <div className="flex justify-between mb-4">
//         <Select 
//           options={options} 
//           styles={customStyles}
//           value={selectedOption} 
//           onChange={handleSelectChange} 
//         />
//         <input 
//           type="text" 
//           placeholder="Search..." 
//           value={searchTerm} 
//           onChange={(e) => setSearchTerm(e.target.value)} 
//           className="border rounded p-2"
//         />
//       </div>
//       <div className="grid grid-cols-4 gap-4">
//       {pdfFiles.map((pdfFile, index) => (
//         <Link key={index} href={`/pdfView?file=${encodeURIComponent(pdfFile)}`}>
//             <div 
//             className={`w-full h-full relative ${hoverIndex === index ? 'bg-cyan-200' : ''}`}
//             onMouseEnter={() => setHoverIndex(index)}
//             onMouseLeave={() => setHoverIndex(null)}
//             >
//             <div className="absolute inset-0 z-10 bg-cyan-500 opacity-0 hover:opacity-25 transition-opacity duration-200"></div>
//             <Document file={pdfFile}>
//                 <Page pageNumber={1} width={250} renderTextLayer={false} renderAnnotationLayer={false} />
//             </Document>
//             </div>
//         </Link>
//         ))}
//       </div>
//     </div>
//   );
// }
