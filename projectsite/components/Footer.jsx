import React from "react";
import { GrMail } from "react-icons/gr";
import {FaGithubSquare} from "react-icons/fa";
import { motion } from "framer-motion";

const Footer = () => {
  return (
        <div className="w-full h-auto flex flex-col items-center bg-ncc-beige">
            <div className="w-full h-[.2rem] mb-8 bg-ncc-black"/>
            <div className="flex flex-row items-center justify-center -translate-y-3">
                <motion.a
                    target="_blank"
                    href="https://www.citrushack.com/"
                    className="text-ncc-brown hover:text-ncc-brown "
                    whileHover={{ scale: 1.2 }}
                >
                    <div className="text-ncc-brown  flex flex-row">
                        <img className="w-[35px] -translate-y-2 translate-x-2 " src="citrus.png"/>
                        itrus Hack 2023
                    </div>
                   
                </motion.a>

            </div>
        </div>
  );
};

export default Footer;
