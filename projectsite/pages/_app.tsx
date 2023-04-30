import '@/styles/globals.css'
import type { AppProps } from 'next/app'
import { Inter } from 'next/font/google';

const Inty = Inter ({
  subsets: ['latin'],
  weight: ['600']
})

export default function App({ Component, pageProps }: AppProps) {
  return (
    <div className='bg-ncc-beige'>
      <div className={Inty.className}>
          <Component {...pageProps} />
      </div>
    </div>
  );
}
