# Solar System API

Welcome to the Solar System API, a FastAPI project providing detailed information about the planets in our solar system, including their moons. This API offers endpoints to retrieve data on the distance from the sun, radius, and interesting facts for each celestial body.

## Features

- **General Information Endpoint**: Get a welcoming message and an overview of what the API offers.
- **Planets and Moons Endpoint**: Access detailed information about each planet and major moons in our solar system, including their distance from the sun, radius, and fascinating facts.
- **Individual Planet Information**: Query information for a specific planet or moon.
- **Planet Images**: Retrieve images for each planet and moon.

## Installation

To run this project locally, you will need Python installed on your system. Then, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt


# Start the FastAPI server:

uvicorn main:app --reload

# Usage
After starting the server, you can access the API at http://127.0.0.1:8000. Here are some endpoints you can try:

/: The root endpoint, which provides a welcome message.
/plants: Retrieves information on all planets and major moons.
/plants/{planet_name}: Fetches detailed information about a specific planet or moon.
/plants/{planet_name}/image: Returns an image of the specified planet or moon.
