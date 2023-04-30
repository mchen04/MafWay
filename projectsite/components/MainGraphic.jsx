import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { motion } from "framer-motion";
import { useState } from "react";

const MainGraphic = () => {
    const [imageSrc, setImageSrc] = useState();
    const [uploadData, setUploadData] = useState();

    function handleOnChange(changeEvent) {
        const reader = new FileReader();
    
        reader.onload = function(onLoadEvent) {
          setImageSrc(onLoadEvent.target.result);
          setUploadData(undefined);
        }
    
        reader.readAsDataURL(changeEvent.target.files[0]);
    }

    async function handleOnSubmit(event) {
        event.preventDefault();
    
        const form = event.currentTarget;
        const fileInput = Array.from(form.elements).find(({ name }) => name === 'file');
    
        const formData = new FormData();
    
        for ( const file of fileInput.files ) {
          formData.append('file', file);
        }
    
        formData.append('upload_preset', 'my-uploads');
    
        const data = await fetch('https://api.cloudinary.com/v1_1/dp0bizotu/image/upload', {
          method: 'POST',
          body: formData
        }).then(r => r.json());
    
        setImageSrc(data.secure_url);
        setUploadData(data);
    }

    return (
        <div className="w-full h-full flex flex-row items-center">
            <div className="w-6/12 h-36 mt-24 mb-96 ml-12 flex flex-col items-center ">
                <div className="text-3xl flex mt-20">Using Convolutional Neural Networks</div>
                <div className="text-3xl flex mb-10">to Help You With Your Math:</div>
                <motion.a
                transition={{ type: "spring", stiffness: 500 }}
                whileHover={{ scale: 1.15, }}
                href={"https://legacy.reactjs.org/docs/getting-started.html"}
                >
                    <div className="flex items-center justify-center text-ncc-beige">
                        <label htmlFor="dropzone-file" className="flex flex-col items-center rounded-3xl justify-center w-96 h-40 border-[3px] border-ncc-beige cursor-pointer bg-ncc-brown">
                            <div className="flex flex-col items-center justify-center pt-5 pb-6 ml-16">
                                
                                <form method="post" onChange={handleOnChange} onSubmit={handleOnSubmit}>
                                <p>
                                    <input type="file" name="file" />
                                </p>  
                                
                                {imageSrc && !uploadData && (
                                    <p>
                                    <button>Upload Files</button>
                                    </p>
                                )}

                            </form>
                            </div>

                        </label>
                    </div> 
                </motion.a>
            </div>
            <div className="w-2 h-[32rem] ml-32 rounded-2xl bg-ncc-brown "/>
            <motion.div
                animate={{x:[400,300,200,150,100,60,20,10,0]}}
            >
                <div>
                    <img className="w-[1000px]" src="phone.png" alt="phone" />
                </div>
            </motion.div>
        </div>
    )
}

export default MainGraphic;
