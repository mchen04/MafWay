import "bootstrap/dist/css/bootstrap.min.css";
import Image from "next/image";
import Navigation from "@/components/Navigation";
import MainGraphic from "@/components/MainGraphic";
import Footer from "@/components/Footer";

export default function Home() {
  return (
    <div className="w-full min-h-screen bg-ncc-beige">
      <Navigation/>
      <MainGraphic/>
      <Footer/>
    </div>
  )
}
