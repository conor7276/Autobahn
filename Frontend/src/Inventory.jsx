import { useState, useEffect } from 'react';
import Nav from "./Navbar";
import Carprot from "./Invcomponent"

function Inventory() {
    const [data, setData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:5000/hello");
                const data = await response.json();
                setData(data);
                console.log(data);
            } catch (error) {
                console.log(error);
            }
        };

        fetchData();
    }, []);

    
    if (data.length === 0) {
        return (
            <>
                <Nav />
            </>
        );
    }
    
    //const car=data[0]
    const carsLayout = data.map((car, i) => {
        return <Carprot car={car} key={i} />;
      });

    return (
        <>
            <Nav />
            <div className='grid grid-cols-3 w-screen h-screen justify-items-center'>
            {carsLayout}
            </div>
        </>
    );
}

export default Inventory;
