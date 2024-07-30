Sure, here's the detailed README file with appropriately sized images:

---

# Crypto Alert App

This project consists of a web application that allows users to set alerts for cryptocurrency prices. The application uses Streamlit for the frontend and Flask for the backend. It also integrates with the CoinGecko API to fetch real-time cryptocurrency prices and Redis for storing alerts.

## Features

- **Streamlit App:** A user interface to set alerts for cryptocurrency prices and view price charts.
  <img src="https://github.com/user-attachments/assets/fc8162a0-5cf6-4d18-a79f-d39b45f23119" alt="Streamlit App" width="400">

- **Flask API:** A RESTful API to manage alerts and fetch cryptocurrency prices.
  <img src="https://github.com/user-attachments/assets/b7c46933-3dde-4025-9cee-d12999e2f086" alt="Flask API" width="400">

- **CoinGecko Integration:** Fetch real-time cryptocurrency prices.
  <img src="https://github.com/user-attachments/assets/139a298a-6900-4795-bce0-dbcbe3988fd7" alt="CoinGecko Integration" width="400">

- **Redis:** Store and manage alert data.
  <img src="https://github.com/user-attachments/assets/10e13ba6-192a-46ef-b292-08f308d8af29" alt="Redis" width="400">

## Getting Started

### Prerequisites
![image](https://github.com/user-attachments/assets/9adc0a03-00c1-4638-9870-1210fb1a41b7)


- Docker
- Docker Compose

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/crypto-alert-app.git
   cd crypto-alert-app
   ```

2. **Create the `requirements.txt` file:**

   ```txt
   flask
   streamlit
   requests
   redis
   pandas
   numpy
   matplotlib
   ```

3. **Create the Dockerfile:**

   ```dockerfile
   # Use an official Python image as the base
   FROM python:3.9-slim

   # Set the working directory in the container
   WORKDIR /app

   # Copy the requirements file
   COPY requirements.txt .

   # Install the dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy the app code
   COPY app.py .
   COPY api.py .

   # Make ports available to the world outside this container
   EXPOSE 8501
   EXPOSE 5000

   # Run the Flask API and Streamlit app when the container launches
   CMD ["sh", "-c", "python api.py & streamlit run app.py"]
   ```

4. **Create the `docker-compose.yml` file:**

   ```yaml
   version: '3.7'

   services:
     redis:
       image: "redis:alpine"
       container_name: "redis"
       ports:
         - "6379:6379"

     app:
       build: .
       container_name: "crypto-alert-app"
       ports:
         - "8501:8501"
         - "5000:5000"
       depends_on:
         - redis
       environment:
         - REDIS_HOST=redis
         - REDIS_PORT=6379
   ```

### Running the Application

1. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

2. **Access the Streamlit app:**

   Open your browser and go to `http://localhost:8501`.

3. **Access the Flask API:**

   The API will be running at `http://localhost:5000`.

### Usage

#### Streamlit App

1. Select a cryptocurrency (Bitcoin, Ethereum, Ripple).
2. View the current price fetched from the CoinGecko API.
3. Enter the price at which you want to receive an alert.
4. Enter your email address.
5. Click on "Set Alert" to save the alert.

#### Flask API

- **Create Alert:**

  ```bash
  curl -X POST http://localhost:5000/alerts/create/ -H "Content-Type: application/json" -d '{"coin": "bitcoin", "price": 30000, "email": "user@example.com", "status": "created"}'
  ```

- **Get Alerts:**

  ```bash
  curl -X GET http://localhost:5000/alerts/
  ```

- **Delete Alert:**

  ```bash
  curl -X DELETE http://localhost:5000/alerts/delete/ -H "Content-Type: application/json" -d '{"coin": "bitcoin", "price": 30000, "email": "user@example.com"}'
  ```

- **Get Price:**

  ```bash
  curl -X GET http://localhost:5000/price/bitcoin/
  ```

### Project Structure

```
crypto-alert-app/
│
├── app.py                # Streamlit app code
├── api.py                # Flask API code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Dockerfile for building the image
└── docker-compose.yml    # Docker Compose configuration
```

### Contributing

If you would like to contribute, please open a pull request or issue on GitHub.

### License

This project is licensed under the MIT License. See the `LICENSE` file for details.

### Contact

For questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).

---

Feel free to customize this README file further based on your project's specific needs and details.
