import Nav from "./Navbar";

export default function Services(){

    return(
        <>
        <div className="w-screen ">
        <Nav />
        <div className="min-h-screen bg-cover bg-center" style={{ backgroundImage: `url(Service.jpg)` }}></div>

        <div className="grid grid-cols-2 grid-rows-2 gap-4 p-4">
        <div className="grid grid-cols-2 grid-rows-2 gap-4 p-4 absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <div className="w-80 h-80 bg-gray-800 bg-opacity-40 hover:bg-gray-900 transition-all transform hover:scale-105 rounded-md">
            <img className="mx-auto h-auto " src="https://logos-world.net/wp-content/uploads/2021/04/Porsche-Logo.png" alt="Porsche Logo"></img>
              <p className="text-white text-center p-4">Content Here</p>
            </div>
            <div className="w-80 h-80 bg-gray-800 bg-opacity-40 hover:bg-gray-900 transition-all transform hover:scale-105 rounded-md">
            <img className="mx-auto h-auto" src="http://pluspng.com/img-png/audi-logo-png-audi-logo-rings-symbol-4880.png" alt="Audi Logo"></img>
              <p className="text-white text-center p-4">Content Here</p>
            </div>
            <div className="w-80 h-80 bg-gray-800 bg-opacity-40 hover:bg-gray-900 transition-all transform hover:scale-105 rounded-md">
            <img className="mx-auto h-auto" src="https://logos-world.net/wp-content/uploads/2020/05/Mercedes-Benz-Logo.png" alt="Mercedes Logo"></img>
              <p className="text-white text-center p-4">Content Here</p>
            </div>
            <div className="w-80 h-80 bg-gray-800 bg-opacity-40 hover:bg-gray-900 transition-all transform hover:scale-105 rounded-md">
            <img className="mx-auto h-52" src="https://www.carlogos.org/car-logos/bmw-logo-1997-1200x1200.png" alt="BMW Logo"></img>
              <p className="text-white text-center p-4">Content Here</p>
            </div>
          </div>
          </div>
        </div>
        </>
    )

}