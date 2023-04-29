import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import { Cormorant_Garamond } from 'next/font/google';
import { PT_Serif } from 'next/font/google';

const garamond = Cormorant_Garamond({
  subsets: ['latin'], 
  weight: ['600'],
})

const serif = PT_Serif({
  subsets: ['latin'],
  weight: ["400"],
})

export default function App({ Component, pageProps }: AppProps) {
  return (
    <div className='bg-ncc-beige'>
      <div className={serif.className}>
          <Component {...pageProps} />
      </div>
    </div>
  );
}
