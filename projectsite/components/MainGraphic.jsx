import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { motion } from "framer-motion";

const MainGraphic = () => {
    return (
        <div className="w-full h-full">
            <div className="w-full h-36 mt-24 mb-96 flex flex-col items-center justify-center">
                <div className="text-3xl mb-8 flex flex-col items-center justify-center">Using Convolutional Neural Networks to <br></br> Help you With your Math:</div>

                <motion.a
                transition={{ type: "spring", stiffness: 500 }}
                whileHover={{ scale: 1.1 }}
                href={"https://legacy.reactjs.org/docs/getting-started.html"}
                >
                    <div className="text-ncc-brown text-9xl relative no-underline">BUTTON</div>
                </motion.a>
            </div>
            
        </div>
    )
}

export default MainGraphic;
