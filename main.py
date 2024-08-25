import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from io import BytesIO
from pathlib import Path
import shutil
import os
from utils import bg_remove
from pyngrok import ngrok


app = FastAPI()

# Define the directory where uploaded files will be stored
UPLOAD_DIR = Path("images")  # Sets the directory for storing uploaded images
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)  # Creates the directory if it doesn't exist, including any necessary parent directories

@app.get("/", response_class=HTMLResponse)
async def get_upload_form(file_url: str = None):
    # Serve the HTML upload form to the user
    # Print No.1 (For Debugging)
    print('Get upload form')

    # Read the contents of the frontend HTML file
    with open('frontend.html', 'r') as file:
        html_content = file.read()

    # If a file URL is provided, replace the placeholder in the HTML with the actual file URL
    if file_url:
        html_content = html_content.replace("{{ file_url }}", file_url)
    else:
        html_content = html_content.replace("{{ file_url }}", "")

    # Return the HTML content as a response
    return HTMLResponse(content=html_content)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Handle the file upload and background removal process

    # Check if the file has an allowed extension
    if not (file.filename.endswith('.png') or file.filename.endswith('.jpeg') or file.filename.endswith('.jpg')):
        raise HTTPException(status_code=400, detail="Only PNG or JPEG files are allowed.")  # Raise an error if the file type is not supported

    # Sanitize the filename to avoid any potential security issues
    sanitized_filename = file.filename.replace("%", "").replace("'", "").replace("/", "").replace("\\", "")

    # Define the file's storage location within the upload directory
    file_location = UPLOAD_DIR / sanitized_filename

    # Save the uploaded file to the specified location
    with file_location.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Print No.2 (For Debugging)
    print('no.1')
    try:
        # Print No.3 (For Debugging)
        print('no.2')

        # Call the background removal function and store the path of the new image
        new_path = bg_remove(file_location)

        # Generate the URL for accessing the processed file
        file_url = f"/files/{Path(new_path).name}"

        # Print No.4 (For Debugging)
        print('no.3', new_path)

        # Return the file URL as a JSON response
        return JSONResponse({"file_url": f"/files/{Path(new_path).name}"})
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=f"Error processing file: {e}")

@app.get("/files/{filename}")
async def download_file(filename: str):
    # Handle the request to download a processed file

    # Define the full path to the requested file
    file_path = UPLOAD_DIR / filename

    # Print No.5 (For Debugging)
    print(file_path)

    # Check if the file exists
    if not file_path.exists():
        # Print No.6 (For Debugging)
        print('404 here')
        raise HTTPException(status_code=404, detail="File not found")

    # Return the file as a response
    return FileResponse(file_path)


if __name__ == "__main__":
    # Set up ngrok
    authtoken = os.environ.get('NGROK_TOKEN')
    if authtoken:
        ngrok.set_auth_token(authtoken)
    else:
        print("No NGROK_TOKEN found. Please set the environment variable.")

    port = 9999
    public_url = ngrok.connect(port).public_url
    print("Your Uvicorn server is accessible at:", public_url)

    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
