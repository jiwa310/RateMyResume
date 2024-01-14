import PdfViewHeader from '../components/pdfViewHeader';
import { Document, Page } from 'react-pdf';
import { useRouter } from 'next/router';

export default function PdfView() {
    const router = useRouter();
    const { file } = router.query;

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
            <button className="border-2 border-cyan-400 text-cyan-400 py-2 px-4 font-bold hover:bg-cyan-400 hover:text-black transition duration-200">
                Post
            </button>
        </div>
        </div>
    );
}

