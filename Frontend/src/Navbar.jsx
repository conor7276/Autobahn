import { PiShoppingCart } from 'react-icons/pi';
import { IoPersonOutline } from 'react-icons/io5';
import { BiSolidCarMechanic } from 'react-icons/bi';
import { Link } from 'react-router-dom';

function Nav(){
    return(
        <nav className="bg-black">
            <div className=" flex flex-wrap items-center justify-between ">
            <div className=" items-end ">
            <img src="/Logo.png" className="h-16 mx-10" alt="Flowbite Logo" />
            </div>
            <div className='flex items-end'>
                
            <Link to={`/Inventory?brand=All`} className="text-white mr-10 font-sans "> <BiSolidCarMechanic /> </Link>
            <Link to={`/Inventory?brand=All`} className="text-white mr-10 font-sans "> <PiShoppingCart /> </Link>
            <Link to={`/Inventory?brand=All`} className="text-white mr-10 font-sans"> <IoPersonOutline /> </Link>

            </div>
            
            </div>
        </nav>
    )
}
export default Nav;