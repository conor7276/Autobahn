import { useState, useEffect } from 'react';
import { useLocation } from 'react-router-dom';
import Nav from "./Navbar";
import Carprot from "./Invcomponent"

function Inventory() {
    const location = useLocation();
    const searchParams = new URLSearchParams(location.search);
    const brand = searchParams.get('brand');
    const [data, setData] = useState([]);
    const [bodyType,setBodyType]= useState('All');
    const [selectedCar, setSelectedCar] = useState(brand);
    const [showSpinner, setShowSpinner] = useState(true);
    const [price, setPrice] = useState(500000); 
    const [min,setMin]=useState(1950);
    const [max,setMax]=useState(2023);

    const handleCarSelect = (event) => {
        setSelectedCar(event.target.value);
    };
    const handleBodyTypeSelect = (event) => {
        setBodyType(event.target.value);
    };
    const handlePriceChange = (event) => {
        setPrice(event.target.value);
        console.log(price)
      };

    setTimeout(() => {
        setShowSpinner(false);
      }, 1000);
    
    useEffect(() => {
        const fetchData = async () => {
            try {
                
                if(selectedCar==="All"){
                    const response = await fetch(`http://localhost:5000/hello/${price}/${min}/${max}/${bodyType}`);
                    const data = await response.json();
                    setData(data);
                    console.log(data);}
                else{
                    const response = await fetch(`http://localhost:5000/hello2/${selectedCar}/${price}/${min}/${max}/${bodyType}`);
                    const data = await response.json();
                    if (data.length==0){
                        setData([]);
                        console.log("No cars found");
                    }
                    else{
                        setData(data);
                        console.log(data);
                    }
                }
            } catch (error) {
                console.log(error);
            }
        };
        fetchData();
    }, [selectedCar,price,min,max,bodyType]);

    const carsLayout = data.map((car, i) => {
        return <Carprot car={car} key={i} />;
      });

      const [x, setX] = useState(500000); 
    const handleXChange = (event) => {
        setX(event.target.value);
      };

      const handleMinChange = (event) => {
        setMin(event.target.value);
      };
      const handleMaxChange = (event) => {
        setMax(event.target.value);
      };

        return (
            <>
                <Nav />
                <div className="h-screen w-screen bg-gray-200">
                <div className="absolute p-2 rounded-lg place-content-center bg-black mt-7 w-1/4 h-auto mx-1">
                <span className="w-full flex justify-center items-center text-sm text-white py-2 mr-3">Make</span>
                <div className="flex justify-center items-center">
                <select id="carSelect" className="w-2/3 h-10 text-xl bg-gray-200 rounded-md" value={selectedCar} onChange={handleCarSelect}>
                <option value="All">All</option>
                <option value="Porsche">Porsche</option>
                <option value="Audi">Audi</option>
                <option value="Mercedes">Mercedes</option>
                <option value="BMW">BMW</option>
                <option value="Foreigners">Foreigners</option>
                <option value="Special">Special</option>
                </select>
                </div>
                <div className="price-range p-4">
                <span className="text-sm text-white">Max Price $</span>
                <span className="text-sm text-white">{x}</span>
                
                <input className="w-full accent-indigo-600" type="range" name="" value={x} min="50000" max="500000" onChange={handleXChange} onMouseUp={handlePriceChange}/>
                <div className="-mt-2 flex w-full justify-between">
                <span className="text-sm text-white">50000</span>
                <span className="text-sm text-white">500000</span>
                </div>
                </div>
                <div>
                <span className="w-full flex justify-center items-center text-sm text-white mr-3">Year</span>
                <div className="w-full flex p-4 justify-center items-center">
                <span className="text-sm text-white mr-3">Min:</span>
                <input className="rounded-lg text-xl h-10 bg-gray-200" type="number" id="minYear" name="minYear" value={min} min="1950" max="2023" step="1" onChange={handleMinChange} />
                <span className="text-sm text-white ml-10 mr-3">Max:</span>
                <input className="rounded-lg text-xl h-10 bg-gray-200" type="number" id="maxYear" name="maxYear" value={max} min="1950" max="2023" step="1" onChange={handleMaxChange}/>
                </div>
                </div>
                
                <span className="w-full flex justify-center items-center text-sm text-white py-2 mr-3">Bodytype</span>
                <div className="flex justify-center items-center">
                <select id="bodyType" className="w-2/3  h-10 text-xl bg-gray-200 rounded-md mb-4" value={bodyType} onChange={handleBodyTypeSelect} >
                <option value="All">All</option>
                <option value="Sedan">Sedan</option>
                <option value="Coupe">Coupe</option>
                <option value="Convertible">Convertible</option>
                <option value="SUV">SUV</option>
                </select>
                </div>
                </div>
                
                {showSpinner ? (
                    <div role="status" className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
                    <svg aria-hidden="true" className="inline w-8 h-8 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-gray-600 dark:fill-gray-300" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                    </svg>
                    <span className="sr-only">Loading...</span>
                    </div>
                ): data.length == 0 ? (
                    <div className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">Sorry we dont have that car</div>
                  ) : (
                    <div>
                      <div className='grid grid-cols-3 w-3/4 h-auto ml-auto pl-2 pr-5'>
                        {carsLayout}
                    </div>
                    </div>
                  )}
                  </div>
                </>
              );

}

export default Inventory;
