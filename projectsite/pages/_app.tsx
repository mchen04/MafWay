import '@/styles/globals.css';
import type { AppProps } from 'next/app';
import { Cormorant_Garamond } from 'next/font/google';

const garamond = Cormorant_Garamond({
  subsets: ['latin'], 
  weight: ['400'],
})

export default function App({ Component, pageProps }: AppProps) {
  return  (
  <main className={garamond.className}>
    <Component {...pageProps} />
  </main>
  );
}
