import { useState } from 'react';
import { useNavigate} from 'react-router-dom';
import Nav from "../Navbar";
import axios from "axios";

const videoPath = "/rs6.mp4";

function Login() {
    const navigate = useNavigate();
    const [login,setLogin] =useState(true)
    const handleLoginFlase = (event) => {
      setLogin(false);
    };
    const handleLoginTrue = (event) => {
      setLogin(true);
    };

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
    const [signupForm,setSignupForm]=useState({
      name: "",
      email: "",
      password:"",
      phone:""
    })

    const [loginForm, setloginForm] = useState({
      email: "",
      password: ""
    })

    function singMeUP(event){
      axios({
        credentials: 'include',
        method: "POST",
        mode: 'no-cors',
        url: "http://localhost:5000/signUp",
        data: JSON.stringify({
            name: signupForm.name,
            email: signupForm.email,
            password: signupForm.password,
            phone: signupForm.phone
        }),
        headers: {
          'Authorization': 'application/json',
          'Content-Type': 'application/json',
        }
      })

    


      
      setSignupForm(({
        name:"",
        email: "",
        password: "",
      phone:""}))

      event.preventDefault()
      setLogin(true);

      return
      
    }

    function logMeIn(event) {
        axios({
            method: "POST",
            url: "http://localhost:5000/token",
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

    function handleChangeLogin(event) { 
      const {value, name} = event.target
      setloginForm(prevNote => ({
          ...prevNote, [name]: value})
      )}
      
      function handleChangeSignup(event) { 
        const {value, name} = event.target
        setSignupForm(prevNote => ({
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

    <div className="bg-white  bg-opacity-50 p-4 rounded-md">
      {login ? (
        <div>
        <h1 className="text-center pb-4">Login</h1>
        <form className="login" >
        <div className="mb-4">
          <input
            onChange={handleChangeLogin}
            type="email"
            text={loginForm.email}
            name="email"
            placeholder="Email"
            value={loginForm.email}
          />
        </div>
        <div className="mb-4">
          <input
            onChange={handleChangeLogin}
            type="password"
            text={loginForm.password}
            name="password"
            placeholder="Password"
            value={loginForm.password}
          />
        </div>
        <button
          onClick={logMeIn}
          className=" bg-black w-full hover-bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        >
          Login
        </button>
      </form>
      <button onClick={handleLoginFlase}>
        Dont have an account?
      </button>
      </div> ) : (
        
        <div>
           <h1 className="text-center pb-4">Sign Up</h1>
        <form className="Sign up" >
        <div className="mb-4">
          <input
            onChange={handleChangeSignup}
            type="name"
            text={signupForm.name}
            name="name"
            placeholder="Name"
            value={signupForm.name}
          />
        </div>
        <div className="mb-4">
          <input
            onChange={handleChangeSignup}
            type="email"
            text={signupForm.email}
            name="email"
            placeholder="Email"
            value={signupForm.email}
          />
        </div>
        <div className="mb-4">
          <input
            onChange={handleChangeSignup}
            type="password"
            text={signupForm.password}
            name="password"
            placeholder="Password"
            value={signupForm.password}
          />
        </div>
        <div className="mb-4">
          <input
            onChange={handleChangeSignup}
            type="phone"
            text={signupForm.phone}
            name="phone"
            placeholder="Phone"
            value={signupForm.phone}
          />
        </div>
        <button
          onClick={singMeUP}
          className=" bg-black w-full hover-bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        >
          Signup
        </button>
      </form>
      <button onClick={handleLoginTrue}>
        Already have an account?
      </button>
        </div>
      )}


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