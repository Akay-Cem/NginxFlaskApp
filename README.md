# Flask Web App with Gunicorn and Nginx

This project demonstrates how to deploy a simple Flask web application using Gunicorn as the WSGI server and Nginx as the reverse proxy server.

## Project Structure
.
├── app.py
├── README.md
├── requirements.txt
├── templates
│   ├── home.html
│   └── index.html
└── wsgi.py

# Steps to Run the Application

### 1. Install Dependencies
First, make sure the dependencies are installed in your virtual environment.

### 2. Create a virtual environment
python3 -m venv .venv

### 3. Activate the virtual environment
source .venv/bin/activate

### 4. Install the required packages
pip install -r requirements.txt

### 5. Run the Flask App with Gunicorn
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app   

# Configure Nginx
```nginx
server {
    listen 80;
    server_name localhost;  # Use your domain or IP address

    location / {
        proxy_pass http://127.0.0.1:5000;  # Flask app running on port 5000
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    error_log /var/log/nginx/flaskapp_error.log;
    access_log /var/log/nginx/flaskapp_access.log;
}

### Test Nginx configuration
sudo nginx -t

### Restart Nginx
sudo systemctl restart nginx