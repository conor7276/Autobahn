import { PiShoppingCart } from 'react-icons/pi';
import { Link } from 'react-router-dom';

function Nav(){
    return(
        <nav className="bg-black">
            <div className=" flex flex-wrap items-center justify-between ">
            <img src="/Logo.png" className="h-16 mx-10" alt="Flowbite Logo" />
            <Link to={`/Inventory?brand=All`} className="text-white mr-10 font-sans"> <PiShoppingCart /> </Link>
            </div>
        </nav>
    )
}
export default Nav;