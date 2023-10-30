import { Link } from 'react-router-dom';
export  default function Invcomponent({car}){
    const id=car[0];
    const price=car[1];
    const photo=car[2];
    const name=car[8];
    //const brand=car[9];

    return(
        
        <Link to={`${id}`} className='group w-full h-84 p-2 mt-5 rounded-lg  duration-300 transform hover:-translate-y-1'>
        <div className="w-full h-full">
        <img className='object-cover rounded-lg w-full h-full' src={photo} alt="Photos Coming Soon" />
        </div>
        <h3 className="absolute bottom-10 left-10 text-white">{name}</h3>
        <h3 className="absolute bottom-10 right-10 text-white">{price}</h3>
        </Link>
    )
}