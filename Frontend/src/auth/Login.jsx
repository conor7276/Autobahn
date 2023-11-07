import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Nav from "../Navbar";
import axios from "axios";

const videoPath = "/rs6.mp4";

function Login() {
    const navigate = useNavigate();


    function getToken() {
      const userToken = localStorage.getItem('token');
      return userToken && userToken
    }
  
    const [token, setToken] = useState(getToken());
    const [showAlert, setShowAlert] = useState(false);
    const [data,setData]=useState();
    function saveToken(userToken) {
      localStorage.setItem('token', userToken);
      navigate(-1);
      setToken(userToken);
    };
  
    function removeToken() {
      localStorage.removeItem("token");
      setToken(null);
    }

    const [loginForm, setloginForm] = useState({
      email: "",
      password: ""
    })

    function logMeIn(event) {
        axios({
            method: "POST",
            url: "http://127.0.0.1:5000/token",
            data: {
                email: loginForm.email,
                password: loginForm.password,
            },
        })
        
            .then((response) => {
              setShowAlert(true);
            setTimeout(() => {
             setShowAlert(false);
             }, 2000);
  
                // console.log(response.data.access_token);
                // console.log(response.data.user_id)
                //console.log(data.data.access_token);
                saveToken(response.data.access_token);
                setData(response.data.user_id)
                
            })
            .catch((error) => {
                if (error.response) {
                    console.log(error.response);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                }
            });


      setloginForm(({
        email: "",
        password: ""}))

      event.preventDefault()
    }

    function handleChange(event) { 
      const {value, name} = event.target
      setloginForm(prevNote => ({
          ...prevNote, [name]: value})
      )}
      

    return (
      <div>
  <video
    autoPlay
    muted
    loop
    className="absolute top-0 left-0 w-full h-full object-cover"
  >
    <source src={videoPath} type="video/mp4" />
    Your browser does not support the video tag.
  </video>
  <div className="absolute top-0 left-0 w-full h-full flex flex-col justify-center items-center">
    <div className="relative">
      <img
        src="Logo.png" // Provide the correct path to your logo image
        alt="App Logo"
        className="w-120 h-48 mb-24"
      />
    </div>
    <div className="bg-white bg-opacity-50 p-4 rounded-md">
      <h1 className="text-center pb-4">Login</h1>
      <form className="login">
        <div className="mb-4">
          <input
            onChange={handleChange}
            type="email"
            text={loginForm.email}
            name="email"
            placeholder="Email"
            value={loginForm.email}
          />
        </div>
        <div className="mb-4">
          <input
            onChange={handleChange}
            type="password"
            text={loginForm.password}
            name="password"
            placeholder="Password"
            value={loginForm.password}
          />
        </div>
        <button
          onClick={logMeIn}
          className=" bg-black hover-bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        >
          Submit
        </button>
      </form>
      {showAlert && (
        <div className="alert">
          <p>Hello {data[1]}</p>
          {console.log(data[1])}
        </div>
      )}
    </div>
  </div>
</div>

    );
}

export default Login;