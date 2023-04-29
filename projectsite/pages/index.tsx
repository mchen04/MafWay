import "bootstrap/dist/css/bootstrap.min.css";
import Image from "next/image";
import Navigation from "@/components/Navigation";
import MainGraphic from "@/components/MainGraphic";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div>
      
    <Image
      src="/flowers1.jpeg"
      alt="Field of Flowers"
      layout="fill"
      objectFit="cover"
    >
    </Image>
    <Navigation/>
    <MainGraphic/>
    <Footer/>
    </div>
  )
}
