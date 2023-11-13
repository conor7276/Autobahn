import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import App from './App.jsx'
import Service from './Services.jsx'
import Liked from './Liked.jsx'
import Inv from './Inventory.jsx'
import Car, {
  loader as carLoader
} from './Specific.jsx'
import ErrorPage from "./Errpg.jsx"
import Login from "./auth/Login.jsx"
import './index.css'

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
  },
  {
    path:"/service",
    element:<Service/>,
    errorElement: <ErrorPage />,
  },
  {
    path:"/liked",
    element:<Liked/>,
    errorElement: <ErrorPage />,
  },
  {
    path:"/login",
    element:<Login/>,
    errorElement: <ErrorPage />,
  },
  {
    path: "/Inventory",
    element: <Inv />,
    errorElement: <ErrorPage />,
  },
  {
    path: "/Inventory/:CarId",
    element: <Car />,
    errorElement: <ErrorPage />,
    loader: carLoader,
  },
]);


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);