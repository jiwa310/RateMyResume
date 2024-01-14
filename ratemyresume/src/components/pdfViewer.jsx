import { useState, useEffect } from 'react';

const PdfViewer = ({ pdfId }) => {
    const [pdfData, setPdfData] = useState(null);

    const fetchPdf = async () => {
        try {
            const response = await fetch(`/api/items/${itemId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch PDF');
            }

            const pdfBlob = await response.blob();
            setPdfData(pdfBlob);
        } catch (error) {
            console.error('Error fetching PDF:', error.message);
        }
    };

    useEffect(() => {
        fetchPdf();
    }, [itemId]);

    return (
        <div>
            {pdfData && <embed src={URL.createObjectURL(pdfData)} type="application/pdf" />}
        </div>
    );
};

export default PdfViewer;