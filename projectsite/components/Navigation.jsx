import "bootstrap/dist/css/bootstrap.min.css";
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import {FaEnvelope} from "react-icons/fa"
import {FaGithubSquare} from "react-icons/fa"
import {FaLinkedin} from "react-icons/fa"
import { motion } from "framer-motion";

const Navigation = () => {
    return (
        <div className="w-full h-auto flex flex-col ">
      <div className="w-full h-2 bg-ncc-beige"/>
    <div className="flex justify-center bg-ncc-beige">
        <Navbar>
          <Navbar.Brand href="#home" className="justify-center ml-7">
                  <div className="text-7xl w-11/12">TITLE</div>
          </Navbar.Brand>
        </Navbar>

        <Navbar >
          <Nav>
            <motion.a
                  target="_blank"
                  href="https://github.com/mchen04/CitrusHackProject"
                  className="text-ncc-brown hover:text-ncc-white ml-1 mr-6"
              >
                  <FaGithubSquare size={30}/>
              </motion.a>

              <motion.a
                target="_blank"
                href="mailto: nolancswe@gmail.com"
                className="text-ncc-brown hover:text-ncc-white mr-16"
              >
                <FaEnvelope size={30} />
            </motion.a>
          </Nav>
        </Navbar>
    </div>
    
    </div>
    )
}

export default Navigation;
