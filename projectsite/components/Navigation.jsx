import "bootstrap/dist/css/bootstrap.min.css";
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import {FaEnvelope} from "react-icons/fa"
import {FaGithubSquare} from "react-icons/fa"
import {FaLinkedin} from "react-icons/fa"
import { motion } from "framer-motion";
import { Cormorant_Garamond } from "next/font/google";

const garamond = Cormorant_Garamond({
  subsets: ['latin'], 
  weight: ['400'],
})

const Navigation = () => {
    return (
      <div className="w-full h-auto flex flex-col ">
      <div className="w-full h-2 bg-ncc-beige"/>
    <div className="flex justify-between bg-ncc-beige">
        <Navbar>
          <NavDropdown title="[ Menu ]" id="basic-nav-dropdown" style={{fontSize: 32}} className="justify-start ml-16">
                <NavDropdown.Item href="/">Home</NavDropdown.Item>
                <NavDropdown.Item href="/portfolio" className="test-2xl ">
                  Portfolio
                </NavDropdown.Item>
                <NavDropdown.Item href="/experience">Experience</NavDropdown.Item>
                <NavDropdown.Item href="/about">
                  About
                </NavDropdown.Item>
          </NavDropdown>
        </Navbar>

        <Navbar>
          <Navbar.Brand href="#home" className="justify-center ml-7">
                  <img
                    src="/React-icon.png"
                    width="60"
                    height="60"
                    className="d-inline-block align-top"
                  />
          </Navbar.Brand>
        </Navbar>

        <Navbar>
          <Nav>
            <motion.a
                  target="_blank"
                  href="https://github.com/Nolancchu"
                  className="text-ncc-brown hover:text-ncc-green ml-1 mr-6"
              >
                  <FaGithubSquare size={30}/>
              </motion.a>

              <motion.a
                target="_blank"
                href="https://www.linkedin.com/in/nolan-chu/"
                className="text-ncc-brown hover:text-ncc-green mr-6"
              >
                <FaLinkedin size={30} />
              </motion.a>

              <motion.a
                target="_blank"
                href="mailto: nolancswe@gmail.com"
                className="text-ncc-brown hover:text-ncc-green mr-16"
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
