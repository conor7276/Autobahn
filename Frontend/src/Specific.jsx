import {useLoaderData } from "react-router-dom";

export async function loader({ params }) {
    const jobResponse = await fetch(
      `http://localhost:5000/hello/${params.CarId}`
    );
    const car = await jobResponse.json();
    return { car };
}

export default function Specific() {
    const { car } = useLoaderData();
  
    return (
      <div>
        {car.map((item) => (
          <div >
            <img className="w-1/2 h-1/2" src={item[2][0]} />
            <p>Hello</p>
            <p>{item[1]}</p>
          </div>
        ))}
      </div>
    );
  }