import { PiShoppingCart } from 'react-icons/pi';
import { IoPersonOutline, IoPersonRemoveOutline } from 'react-icons/io5';
import { BiSolidCarMechanic } from 'react-icons/bi';
import {AiOutlineHeart} from 'react-icons/ai';
import { Link } from 'react-router-dom';
import { useState } from 'react';


function Nav() {

    function getToken() {
        const userToken = localStorage.getItem('token');
        return userToken && userToken
      }
    
      const [token, setToken] = useState(getToken());
    
      function removeToken() {
        localStorage.removeItem("token");
        setToken(null);
      }


    return (
        <nav className="bg-black">
            <div className="flex flex-wrap items-center justify-between">
                <div className="items-end">
                    <img src="/Logo.png" className="h-16 mx-10" alt="Flowbite Logo" />
                </div>
                <div className='flex items-end'>
                    <Link to={`/service`} className="text-white mr-10 font-sans "> <BiSolidCarMechanic /> </Link>
                    <Link to={`/Inventory?brand=All`} className="text-white mr-10 font-sans "> <PiShoppingCart /> </Link>
                    {console.log(token)}
                    {token ? (
                        <div className="flex items-end">
                        <Link to={`/liked`} className="text-white mr-10 font-sans" ><AiOutlineHeart /></Link>
                        <button className="text-white mr-10 font-sans" onClick={removeToken}><IoPersonRemoveOutline /></button>
                        </div>
                    ) : (
                        <Link to={`/login`} className="text-white mr-10 font-sans"> <IoPersonOutline /> </Link>
                    )}
                </div>
            </div>
        </nav>
    );
}

export default Nav;