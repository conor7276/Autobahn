import "./App.css"
import {useState, useEffect} from 'react';
import { Link } from 'react-router-dom';

import Nav from "./Navbar"

function App() {
  

  return (
    <>
  <div className="relative min-h-screen">
    <Nav/>
    <div className="sticky top-0 h-screen w-screen">
      
      <img
        className="h-full w-full object-cover"
        src="Porsche.jpg"
        alt="Porsche 911"
      />
      <div className="absolute top-10 left-10 h-auto w-auto  bg-white/30">
        <h1 className="text-5xl text-center my-2"> Porsche </h1>
        <p className="text-center text-2xl mx-6">The Porsche exudes elegance and performance in<br/> every curve and detail. Its timeless design and<br/> powerful engineering make it a true symbol of<br/> automotive excellence.</p>
        <div className="flex justify-center">
        <Link to={`Inventory`}className="bg-black text-center py-2 px-5 text-white m-3 mb-5">Inventory</Link>
        </div>
      </div>
      <img className="absolute top-10 right-0 h-32 " src="https://logos-world.net/wp-content/uploads/2021/04/Porsche-Logo.png" alt="Porsche Logo"></img>
    </div>

    <div className="sticky top-0 h-screen w-screen">
      <img
        className="h-full w-full object-cover"
        // src="https://i.pinimg.com/originals/a7/f6/d0/a7f6d0029eb322d22c91c3a883e8bd33.jpg"
        src="Audi.jpg"
        alt="Audi RS6"
      /><div className="absolute top-10 left-10 h-auto w-auto  bg-white/30">
      <h1 className="text-5xl text-center my-2"> AUDI </h1>
      <p className="text-center text-2xl mx-6">The Audi is a masterpiece of precision engineering,<br/> blending cutting-edge technology with luxurious<br/> comfort. It's a symbol of sophistication on the road.</p>
      <div className="flex justify-center">
      
        <Link to={`Inventory`}className="bg-black text-center py-2 px-5 text-white m-3 mb-5">Inventory</Link>
        
        </div>
    </div>
      <img className="absolute top-10 right-6 h-28" src="http://pluspng.com/img-png/audi-logo-png-audi-logo-rings-symbol-4880.png" alt="Audi Logo"></img>
    </div>

    <div className="sticky top-0 h-screen w-screen">
      <img
        className="h-full w-full object-cover"
        src="Mercedes.jpg"
        alt="Mercedes G-Class"
      />
      <div className="absolute top-10 left-10 h-auto w-auto  bg-white/30">
        <h1 className="text-5xl text-center my-2"> Mercedes-Benz </h1>
        <p className="text-center text-2xl mx-6">The Mercedes, synonymous with automotive<br/> prestige, embodies a legacy of unparalleled<br/> craftsmanship and innovation. It sets the standard<br/> for luxury and performance, making every drive an<br/> unforgettable experience.</p>
        <div className="flex justify-center">
        <Link to={`Inventory`}className="bg-black text-center py-2 px-5 text-white m-3 mb-5">Inventory</Link>
        </div>
      </div>

      <img className="absolute top-10 right-0 h-32" src="https://logos-world.net/wp-content/uploads/2020/05/Mercedes-Benz-Logo.png" alt="Mercedes Logo"></img>
    </div>

    <div className="sticky top-0 h-screen w-screen">
      <img
        className="h-full w-full object-cover"
        src="BMW.jpg"
        alt="BMW M5 CS"
      />
      <div className="absolute top-10 left-10 h-auto w-auto  bg-white/30">
        <h1 className="text-4xl text-center my-2 "> BMW </h1>
        <p className="text-center text-1xl mx-6">The BMW, the ultimate driving machine, combines<br/> sleek design with exhilarating performance. It's a<br/> testament to precision engineering and the joy of<br/> the open road.</p>
        <div className="flex justify-center">
        <Link to={`Inventory`}className="bg-black text-center py-2 px-5 text-white m-3 mb-5">Inventory</Link>
        </div>
      </div>

      <img className="absolute top-6 right-7 h-44" src="https://www.carlogos.org/car-logos/bmw-logo-1997-1200x1200.png" alt="BMW Logo"></img>
    </div>
  </div>
</>
  )
}

export default App
