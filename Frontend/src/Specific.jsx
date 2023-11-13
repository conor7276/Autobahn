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

const postTest = async() =>{
  const requestOptions = {
    method : 'POST',
    body: JSON.stringify({title:'POST test'})
  };
  //const response = await fetch(`http://localhost:5000/inquire/${requestOptions.body}`);
  const response = await fetch(`http://localhost:5000/inquire`, requestOptions);
  const data = await response.json();
  console.log(data)
  return data;
  
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
      <span>{item[9]} {item[8]}
      <div className="mt-5"><span className="text-green-500">{item[1]}$</span></div>
      <div className="inset-0 flex ml-1 ">
    {/* Table */}
    <table className="w-full h-full mt-10 ">
  <tbody>
  <tr className="flex">
      {/* Cell 1 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/miles.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Miles: </p>
      </td>
      
      {/* Cell 2 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/transmition.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Transmition: </p>
      </td>
    </tr>

    <tr className="flex">
      {/* Cell 3 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/color.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Color: </p>
      </td>
      
      {/* Cell 4 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/drivetrain.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Drivetrain: </p>
      </td>
    </tr>

    <tr className="flex">
      {/* Cell 5 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/engine.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Engine: </p>
      </td>
      
      {/* Cell 6 */}
      <td className="flex-none w-72 border border-gray-800 p-4 flex items-center">
        <img className="w-10 h-10 object-cover rounded object-left mr-2" src="/hp.png" alt="Image 1" />
        <p className="text-black text-lg text-center">Horsepower: </p>
      </td>
    </tr>
  </tbody>
</table>

  </div>
      </span>
      
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
      <button onClick={postTest} className="ml-60 mt-5">Press me for post request</button>
    </div>
  ))}
</div>

</>

    );
  }