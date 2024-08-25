# Background Remover Simple Web Application

This web application allows users to upload images and automatically remove the background, providing a clean, transparent result. It's built with a FastAPI backend and a simple HTML/CSS/JavaScript frontend.

## Features

- User-friendly web interface
- Supports PNG and JPEG image uploads
- Automatic background removal using AI
- Download option for processed images
- Accessible via a public URL using ngrok

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- pyngrok
- python-multipart
- backgroundremover

## Installation

1. Clone this repository:
git clone https://github.com/yourusername/background-remover.git
cd background-remover
2. Install the required dependencies:
pip install -r requirements.txt
3. Set up your ngrok authtoken:
- Sign up for a free ngrok account at https://ngrok.com/
- Get your authtoken from the ngrok dashboard
- Set it as an environment variable:
  ```
  export NGROK_TOKEN=your_ngrok_authtoken
  ```

## Usage

1. Run the application:
python main.py
2. The console will display a public URL where your application is accessible.
3. Open the URL in a web browser to use the background remover:
- Click "Select Your Image" to choose an image file
- Click "Remove Background" to process the image
- Once processing is complete, you can view and download the result

## File Structure

- `main.py`: FastAPI application and server setup
- `utils.py`: Background removal utility functions
- `frontend.html`: HTML template for the web interface
- `requirements.txt`: List of Python dependencies

## How It Works

1. The user uploads an image through the web interface.
2. The image is sent to the FastAPI backend.
3. The backend uses the `backgroundremover` library to process the image.
4. The processed image is saved and a URL is returned to the frontend.
5. The frontend displays the original and processed images, allowing the user to download the result.

## Troubleshooting

- If you encounter any issues with ngrok, make sure your authtoken is correctly set.
- For image processing problems, check that all dependencies are correctly installed.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/yourusername/background-remover/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)

