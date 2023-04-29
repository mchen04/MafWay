import React from "react";
import { BsDiscord } from "react-icons/bs";
import { GrMail } from "react-icons/gr";
import {FaGithubSquare} from "react-icons/fa"
import {FaLinkedin} from "react-icons/fa"
import { motion } from "framer-motion";

const Footer = () => {
  return (
    <footer className="w-full h-full relative">
        <div className="w-full flex flex-col items-center">
            <div className="h-14 mt-3 flex flex-row justify-center items-center">

                <motion.a
                    target="_blank"
                    href="https://github.com/mchen04/CitrusHackProject"
                    className="text-ncc-brown hover:text-ncc-green mr-8"
                >
                    <FaGithubSquare size={20}/>
                </motion.a>

                <motion.a
                target="_blank"
                className="text-ncc-brown hover:text-ncc-green ml-8"
                href="https://ieeeucr.github.io/subscribe.html"
                >
                <GrMail size={20} />
                </motion.a>
            
            </div>

            <div className="text-ncc-brown mb-10">
                For Citrus Hack 2023
            </div>
        </div>
    </footer>
  );
};

export default Footer;
