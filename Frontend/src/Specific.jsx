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



// const testButton = async() =>{
//   console.log("Button has been pressed");
// }
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
      <div className="flex w-screen">
      <div className="flex mt-20 ml-60 w-5/12 h-5/12 relative">
  <img className="w-auto h-full" src={image} alt="NA" />
  <div className="inset-0 flex ml-8 ">
    <p className="whitespace-nowrap text-5xl font-bold flex">
      <span>{item[9]} {item[8]}</span>
      <span className="text-green-500 ml-72">{item[1]}$</span>
    </p>
  </div>
</div>
</div>

      <div className="grid grid-rows-1 grid-cols-10 ml-60 mt-5 w-5/12">
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