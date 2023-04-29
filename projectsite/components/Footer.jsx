import React from "react";
import { GrMail } from "react-icons/gr";
import {FaGithubSquare} from "react-icons/fa";
import { motion } from "framer-motion";

const Footer = () => {
  return (
        <div className="w-full h-auto flex flex-col items-center bg-ncc-beige">
            <div className="w-full h-[.1rem] mb-2 bg-ncc-black"/>
            <div className="h-14 flex flex-row items-center">

                <motion.a
                    target="_blank"
                    href="https://discord.gg/Ugjp6Us"
                    className="text-ncc-brown hover:text-ncc-white "
                >
                    <FaGithubSquare size={20}/>
                </motion.a>
            </div>

            <div className="text-ncc-brown mb-10 -translate-y-2">
                Citrus Hack 2023
            </div>
        </div>
  );
};

export default Footer;
