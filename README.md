# 🚀 CI/CD Pipeline for Flask Application using GitHub Actions & AWS EC2

Automated deployment of a Python Flask application to an Amazon EC2 instance using GitHub Actions. Every push to the `main` branch automatically deploys the latest version of the application to the server, demonstrating a complete Continuous Integration and Continuous Deployment (CI/CD) workflow.

---

## 📌 Project Overview

This project showcases a complete DevOps pipeline where a Flask application is automatically deployed to an AWS EC2 instance whenever code is pushed to GitHub.

The application is hosted on an Ubuntu EC2 instance and managed using a Linux systemd service. GitHub Actions automates the deployment process, eliminating manual updates and ensuring faster, more reliable releases.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Git & GitHub
- GitHub Actions
- AWS EC2
- Ubuntu Linux
- SSH
- systemd

---

## ☁️ AWS Services Used

- Amazon EC2
- IAM
- Security Groups

---

## 📂 Project Structure

```
flask-sample-app/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .gitattributes
```

---

## ⚙️ CI/CD Workflow

```
Developer
      │
      ▼
Push Code to GitHub
      │
      ▼
GitHub Actions Triggered
      │
      ▼
SSH Connection to AWS EC2
      │
      ▼
Pull Latest Code
      │
      ▼
Install Dependencies
      │
      ▼
Restart Flask Service
      │
      ▼
Updated Application Goes Live
```

---

## ✨ Features

- Automated deployment using GitHub Actions
- Python Flask REST API
- Continuous Deployment to AWS EC2
- Linux service management using systemd
- Simple and lightweight deployment workflow
- Easy to extend for larger applications

---

## 📡 API Endpoints

### Home

**GET /**

Returns

```json
{
  "message": "Hello from GitHub Actions CI/CD 🚀"
}
```

---

### About

**GET /about**

Returns project information.

---

### Health Check

**GET /health**

Returns

```json
{
  "status": "healthy"
}
```

---

## 🚀 Running Locally

### Clone Repository

```bash
git clone https://github.com/DivyaBhamare533/flask-sample-app.git
cd flask-sample-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

Application will run at

```
http://localhost:5000
```

---

## ☁️ Deployment

This project is deployed using:

- GitHub Actions
- AWS EC2 (Ubuntu)
- SSH Authentication
- systemd Service

Deployment is triggered automatically whenever changes are pushed to the `main` branch.

---

## 📸 Project Screenshots

> Add screenshots here after deployment.

Suggested screenshots:

- GitHub Repository
- GitHub Actions Workflow
- Successful Deployment
- AWS EC2 Instance
- Flask Application Running

---

## 📚 Learning Outcomes

Through this project I learned:

- Continuous Integration (CI)
- Continuous Deployment (CD)
- GitHub Actions Workflow Automation
- AWS EC2 Deployment
- SSH-based Remote Deployment
- Linux Service Management
- Flask Application Hosting
- Git Version Control

---

## 🔮 Future Enhancements

- Dockerize the Flask application
- Deploy using Amazon ECS
- Add Nginx Reverse Proxy
- Configure HTTPS with SSL
- Add Monitoring using Amazon CloudWatch
- Integrate Infrastructure as Code (Terraform)

---

## 👩‍💻 Author

**Divya Bhamare**

GitHub: https://github.com/DivyaBhamare533

---

⭐ If you found this project useful, consider giving it a star!
