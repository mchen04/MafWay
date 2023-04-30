import "bootstrap/dist/css/bootstrap.min.css";
import Navigation from "@/components/Navigation";
import MainGraphic from "@/components/MainGraphic";
import Footer from "@/components/Footer";
import { motion } from "framer-motion";

export default function Home() {
  return (
    
    <motion.div
      initial={{opacity:0}}
      animate={{opacity:1}}
      transition={{delay:.2,duration:1.0}}
    >
      <div className="w-full min-h-screen bg-ncc-beige"> 
        <Navigation/>
        <MainGraphic/>
        <Footer/>
      </div>
    </motion.div>
   
  )
}
