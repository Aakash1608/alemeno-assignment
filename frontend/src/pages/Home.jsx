import React, { useState, useEffect } from 'react'
import axios from 'axios'

const Home = () => {
  const [response, setResponse] = useState([])
  const [resExists, setResExists] = useState(false)
  const [image, setImage] = useState()
  const handleChange = (e) => {
    setImage(e.target.files[0])
  }
  const handleSubmit = async() => {
    if (image == null || image == undefined) {
      alert("please enter a file")
      return ;
    }
    try {
      let formData = new FormData()
      console.log(image)
      formData.append("image", image)
      const res = await axios.post("http://127.0.0.1:8000/api/strip/", formData, {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data"
        }
      })
      let data = await res.data
      console.log(Object.values(data))
      setResponse(Object.values(data))
      setResExists(true)
    } catch (error) {
      console.error(error)
    }
  }
  return (
    <div className='container'>
          <div className='form-wrapper'>
            <h3>Upload the file below</h3>
            <input type="file" required name="image" onChange={handleChange} />
            <button id='submit-form' onClick={handleSubmit}>Submit</button>
          </div>
          {
            resExists && (
            <div className='res-wrapper'>
              {
                response.map((color, id) => (
                  <div key={id} className="res-content">
                    <span style={{backgroundColor: `rgb(${color[0]}, ${color[1]}, ${color[2]})`}}></span>
                    <p>{`rgb(${color[0]}, ${color[1]}, ${color[2]})`}</p>
                  </div>
                ))
              }
            </div>
            )
          }        
    </div>
  )
}

export default Home