import { useState } from 'react';
import { useNavigate} from 'react-router-dom';
import axios from "axios";

const videoPath = "/rs6.mp4";

function Login() {
  const [error, setError] = useState(null);
  const [errorL, setErrorL] = useState(null);
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
    function getData() {
      const userData = localStorage.getItem('data');
      return userData && userData
    }
  
    const [token, setToken] = useState(getToken());
    const [showAlert, setShowAlert] = useState(false);
    const [data,setData]=useState(getData());

    function saveToken(userToken) {
      localStorage.setItem('token', userToken);
      navigate(-1);
      setToken(userToken);
    };
    function saveData(userData) {
      localStorage.setItem('data', userData);
      
      setData(userData);
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

    function singMeUP(event) {
      event.preventDefault();
    
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
        .then(response => {
          setLogin(true);
          console.log(response.data.message);
          // Reset error state on successful sign-up
          setError(null);
        })
        .catch(error => {
          // Handle error
          if (error.response) {
            console.error(error.response.data.error);
            // Set error state to display the error message
            setError(error.response.data.error);
          } else {
            console.error("Network error");
            setError("Network error");
          }
        });
    
      setSignupForm({
        name: "",
        email: "",
        password: "",
        phone: ""
      });
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
              
  
                
                saveToken(response.data.access_token);
                saveData(response.data.user_id)
                setErrorL(null);
                
            })
            .catch(error => {
              // Handle error
              if (error.response) {
                console.error(error.response.data.error);
                // Set error state to display the error message
                setErrorL(error.response.data.error);
              } else {
                console.error("Network error");
                setError("Network error");
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

    <div className="bg-white bg-opacity-50 p-8 rounded-md w-96 mx-auto">
  {login ? (
    <div>
      <h1 className="text-center pb-4">Login</h1>
      <form className="login">
        <div className="mb-4">
          <input
            onChange={handleChangeLogin}
            type="email"
            text={loginForm.email}
            name="email"
            placeholder="Email"
            value={loginForm.email}
            className="w-full px-4 py-2 border rounded-md"
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
            className="w-full px-4 py-2 border rounded-md"
          />
        </div>
        {errorL && (
          <div className="error">
            <p className="text-red-600">{errorL}</p>
          </div>
        )}
        <button
          onClick={logMeIn}
          className="bg-black w-full hover-bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        >
          Login
        </button>
      </form>
      <button onClick={handleLoginFlase} className="block mx-auto mt-4">
        Don't have an account?
      </button>
    </div>
  ) : (
    <div>
      <h1 className="text-center pb-4">Sign Up</h1>
      <form className="Sign up">
        <div className="mb-4">
          <input
            onChange={handleChangeSignup}
            type="name"
            text={signupForm.name}
            name="name"
            placeholder="Name"
            value={signupForm.name}
            className="w-full px-4 py-2 border rounded-md"
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
            className="w-full px-4 py-2 border rounded-md"
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
            className="w-full px-4 py-2 border rounded-md"
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
            className="w-full px-4 py-2 border rounded-md"
          />
        </div>
        {error && (
          <div className="error">
            <p className="text-red-600">{error}</p>
          </div>
        )}
        <button
          onClick={singMeUP}
          className="bg-black w-full hover-bg-blue-700 text-white font-bold py-2 px-4 rounded-md"
        >
          Signup
        </button>
      </form>
      <button onClick={handleLoginTrue} className="block mx-auto mt-4">
        Already have an account?
      </button>
    </div>
  )}
</div>

  </div>
</div>

    );
}

export default Login;