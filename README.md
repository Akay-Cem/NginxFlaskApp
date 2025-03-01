# Flask Web App with Gunicorn and Nginx

This `README.md`file describes how to deploy a simple Flask web application using Gunicorn as the WSGI server and Nginx as the reverse proxy server. The Flask app is by no means done. This is an initial setup and I will continue to work on it when time is appropriate.. 

## Project Structure
```
.
├── app.py
├── README.md
├── requirements.txt
├── templates
│   ├── home.html
│   └── index.html
└── wsgi.py
```

## Steps to Run the Application

### 1. Clone this repository

```bash
git clone https://github.com/Akay-Cem/NginxFlaskApp.git
cd NginxFlaskApp
```

### 2. Create a virtual environment
```bash
python3 -m venv .venv
```
### 3. Activate the virtual environment
```bash
source .venv/bin/activate
```
### 4. Install the required packages/dependencies
```bash
pip install -r requirements.txt
```
### 5. Run the Flask App with Gunicorn
```bash
gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app   
```
## Configure Nginx
##### [Ubuntu guide](https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview)
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
```

### Test Nginx configuration
```bash
sudo nginx -t
```
### Restart Nginx
```bash
sudo systemctl restart nginx
```



## Docker

### Install Docker
```bash
sudo apt install -y docker.io
```
### Enable Docker
```bash
sudo systemctl enable docker --now
```

### Run docker without sudo

```bash
sudo usermod -aG docker $USER
```

### Install Docker Compose and make it executable
##### [Install Docker](https://docs.docker.com/compose/install/standalone/)

```bash
curl -SL https://github.com/docker/compose/releases/download/v2.32.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
and now reboot and you're good to go.