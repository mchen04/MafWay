import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import {FaGithubSquare} from "react-icons/fa";
import { motion } from "framer-motion";
import { Inter } from "next/font/google";
import internal from "stream";

const Int = Inter({
    subsets: ['latin'],
    weight: ['700'],
})


const Navigation = () => {
    return (
    <div className="w-full h-auto flex flex-col ">
      <div className="w-full h-2 bg-ncc-beige"/>

      <div className="flex justify-center">
      </div>

        <div className="flex flex-row items-center justify-between ml-16 mr-32 bg-ncc-beige">
            <Navbar>
            <Navbar.Brand href="#home" className="flex flex-col justify-center ml-7">
                    <div className="text-6xl">
                        <span className={Int.className}>MAFWAY</span>
                    </div>

                    <div className="text-xl -translate-y-2">
                        <span className={Int.className}>Making Math Easy</span>
                    </div>
            </Navbar.Brand>
            </Navbar>

            <div className="flex flex-row -translate-y-4">
                <Navbar >
                            <Nav>
                                <motion.a
                                    target="_blank"
                                    href="https://github.com/mchen04/CitrusHackProject"
                                    className="text-ncc-brown hover:text-ncc-brown mr-4"
                                    whileHover={{ scale: 1.5 }}
                                >
                                    <FaGithubSquare size={45}/>
                                </motion.a>
                            </Nav>
                        </Navbar>
            </div>
        </div>
    
    </div>
    )
}

export default Navigation;
