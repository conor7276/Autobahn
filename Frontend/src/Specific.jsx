import Nav from "./Navbar";
import { useState  }  from 'react';
import { useLoaderData } from "react-router-dom";

export async function loader({ params }) {
  
    const jobResponse = await fetch(
      `http://localhost:5000/specific/${params.CarId}`
    );
    const car = await jobResponse.json();
    console.log(car
      )
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
  <div className="bg-gray-200 w-screen h-screen">
    <Nav />
    {car.map((item) => (
      <div key={item.carid}>
        <div className="flex mt-20 ml-20 w-5/12 h-5/12">
          <img className="w-auto h-full" src={image} alt="NA" />
          <div className="flex-1 pl-10 ">
            <p className=" whitespace-nowrap"> {item[8]}</p>
          </div>
        </div>
        <div className="grid grid-rows-1 grid-cols-10 ml-20 mt-5 w-5/12">
          {item[2].map((images, index) => (
            <img
              className="h-auto w-auto mr-2 grayscale-on-hover"
              key={index}
              src={images}
              alt={`Image ${index}`}
              onClick={handleImage}
            />
          ))}
        </div>
      </div>
    ))}
  </div>
</>

    );
  }