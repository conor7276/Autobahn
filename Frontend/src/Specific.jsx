import Nav from "./Navbar";
import { useState  }  from 'react';
import { useLoaderData } from "react-router-dom";

export async function loader({ params }) {
    const jobResponse = await fetch(
      `http://localhost:5000/specific/${params.CarId}`
    );
    const car = await jobResponse.json();
    console.log(car)
    return { car };
}


export default function Specific() {
  const { car } = useLoaderData();
  const [image, setImage] = useState(car[0][2][0]);
    
    
    const handleImage = (event) => {
      setImage(event.target.src);

  };
    return (
      <>
      <Nav/>
        {car.map((item) => (
      <div key={item.carid }>
      <img className="mt-20 ml-20 w-5/12 h-5/12" src={image} alt="NA" />
      <div className="grid grid-rows-1 grid-cols-10 ml-20 mt-5">
      {item[2].map((images, index) => (
      <img className=" h-auto w-auto px-2" key={index} src={images} alt={`Image ${index}`}  onClick={handleImage} />
      ))}
      </div>
      </div>
      ))}
      </>
    );
  }