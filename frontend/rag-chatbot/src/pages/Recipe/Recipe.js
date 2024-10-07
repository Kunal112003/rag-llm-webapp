import React from "react";
import './Recipe.css';

export const Recipe = () => {

    const [file, setFile] = React.useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    }

    const handleFileSubmit = (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append('file', file);

        fetch('http://localhost:5000/upload_file', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(result => {
                console.log('Success:', result);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }




    return (
    <div className="d-flex justify-content-center align-items-center vh-100 bg-light">
        <div className="card shadow-lg p-4 rounded-3" style={{ width: '400px' }}>
        <h2 className="text-center mb-4">Upload Recipe</h2>
        <form encType="multipart/form-data" onSubmit={handleFileSubmit}>
            <div className="form-group mb-3">
            <label htmlFor="file" className="form-label">
                Select Recipe File
            </label>
            <input
                type="file"
                className="form-control"
                id="file"
                name="file"
                onChange={handleFileChange}
            />
            </div>
            <button type="submit" className="btn btn-primary w-100">
            Submit
            </button>
        </form>
        </div>
    </div>
    );

}

export default Recipe;