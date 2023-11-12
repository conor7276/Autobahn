import { useState } from 'react';
import { Link } from 'react-router-dom';
import {AiOutlineHeart} from 'react-icons/ai';
import axios from "axios";
export  default function Invcomponent({car}){
    const id=car[0];
    const price=car[1];
    const photo=car[2];
    const name=car[8];
    //const brand=car[9];


    function getToken() {
      const userToken = localStorage.getItem('token');
      return userToken && userToken
    }
  
    const [token, setToken] = useState(getToken());

    function getData() {
        const userData = localStorage.getItem('data');
        return userData && userData
      } 

      const [data,setData]=useState(getData());

      function Like() {
        axios({
          credentials: 'include',
          method: 'POST',
          mode: 'no-cors',
          url: 'http://localhost:5000/Like',
          
          data: {
            personID: data[0],
            carID: id,
          },
        });
        console.log(id,data[0])
      }
    
      function add(event) {
        event.stopPropagation();
        Like();
        event.preventDefault();
      }
    
      return (
        <>
        <div className='group w-full h-84 p-2 mt-5 rounded-lg duration-300 transform hover:-translate-y-1 relative '>
          <Link to={`${id}`} className="h-full block">
            <div className='w-full h-full'>
              <div className='w-full h-full'>
                <img className='object-cover rounded-lg w-full h-full' src={photo[0]} alt='Photos Coming Soon' />
              </div>
              <h3 className='absolute bottom-10 left-10 text-white '>{name}</h3>
              <h3 className='absolute bottom-10 right-10 text-white'>{price} $</h3>
            </div>
          </Link>
    
          {token ? (
          <button onClick={add} className='absolute top-0 right-0 text-white p-2'>
            <AiOutlineHeart />
          </button>
          ) : null}
          
        </div>
        </>
      );
      
      
}