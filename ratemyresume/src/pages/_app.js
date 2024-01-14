import '@/styles/globals.css'
import { Montserrat } from 'next/font/google';

const montserrat = Montserrat({
  subsets: ['latin'],
  weight: ['400', '700'], // Include the font weights you need
  variable: '--font-montserrat',
});

export default function App({ Component, pageProps }) {
  return (
    <main className={montserrat.variable}>
      <Component {...pageProps} />
    </main>
  )
}

