import PdfViewHeader from '../components/pdfViewHeader';
import { Document, Page } from 'react-pdf';
import { useRouter } from 'next/router';
import Link from 'next/link'

export default function PdfPost() {
  const router = useRouter();
  const { file } = router.query;

  const handlePostClick = async () => {
    const response = await fetch(file);
    const blob = await response.blob();

    const formData = new FormData();
    formData.append('file', blob);

    const result = await fetch('/api/upload', {
      method: 'POST',
      body: formData,
    });

    if (result.ok) {
      console.log('File uploaded successfully');
    } else {
      console.log('File upload failed');
    }
  };

  return (
    <div className={`container font-montserrat transition-opacity duration-1000 `}>
      <PdfViewHeader />
      <Document file={file}>
        <Page pageNumber={1} renderTextLayer={false} renderAnnotationLayer={false}/>
      </Document>
      <div className="flex justify-between items-end absolute bottom-0 left-0 right-0 pb-4 px-6">
        <button className="border-2 border-cyan-400 text-cyan-400 py-2 px-4 font-bold hover:bg-cyan-400 hover:text-black transition duration-200">
          Edit
        </button>
        <Link href="/#explore" className="border-2 border-cyan-400 text-cyan-400 py-2 px-4 font-bold hover:bg-cyan-400 hover:text-black transition duration-200">
          Post
        </Link>
      </div>
    </div>
  );
}
