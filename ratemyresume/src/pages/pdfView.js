import PdfViewHeader from '../components/pdfViewHeader';
import { Document, Page } from 'react-pdf';
import { useRouter } from 'next/router';
// import DisqusThread from 'react-disqus-comments';

export default function PdfView() {
    const router = useRouter();
    const { file } = router.query;
    
    // Construct a unique URL for Disqus
    const url = `http://localhost:3000/pdfView?file=${file}`;

    return (
        <div className={`container font-montserrat transition-opacity duration-1000 `}>
        <PdfViewHeader />
        <Document file={file}>
            <Page pageNumber={1} renderTextLayer={false} renderAnnotationLayer={false}/>
        </Document>
        {/* <div style={{ width: '100%' }}>
          <DisqusThread
              shortname="ratemyresume-com"
              identifier={url}
              title="PDF View"
              url={url}
          />
        </div> */}
        </div>
    );
}
