# 🚀 Deployment Guide

This guide will help you deploy the TalentScout Hiring Assistant to various platforms.

## 📋 Prerequisites

- Python 3.8 or higher
- Git installed
- GitHub account (for cloud deployment)

## 🏠 Local Deployment

### Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## ☁️ Cloud Deployment Options

### 1. Streamlit Cloud (Recommended)

**Step 1: Prepare Your Repository**
- Push your code to GitHub
- Ensure all files are committed and pushed

**Step 2: Deploy to Streamlit Cloud**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository and branch
5. Set the main file path to `app.py`
6. Click "Deploy"

**Step 3: Configure (Optional)**
- Add environment variables if needed
- Set up custom domain (if available)

### 2. Heroku Deployment

**Step 1: Create Procfile**
Create a file named `Procfile` (no extension) in your project root:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

**Step 2: Create runtime.txt**
Create a file named `runtime.txt`:
```
python-3.9.18
```

**Step 3: Deploy**
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Deploy
git push heroku main
```

### 3. Railway Deployment

**Step 1: Connect Repository**
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Railway will auto-detect the Python project

**Step 2: Configure**
- Set the start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- Add environment variables if needed

### 4. Docker Deployment

**Step 1: Create Dockerfile**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Step 2: Build and Run**
```bash
# Build the image
docker build -t hiring-assistant .

# Run the container
docker run -p 8501:8501 hiring-assistant
```

### 5. AWS/GCP/Azure Deployment

#### AWS Elastic Beanstalk
1. Create a `requirements.txt` file
2. Create a `Procfile` for the start command
3. Deploy using AWS Elastic Beanstalk console or CLI

#### Google Cloud Run
1. Create a Dockerfile (see above)
2. Build and push to Google Container Registry
3. Deploy to Cloud Run

#### Azure App Service
1. Create a `requirements.txt` file
2. Deploy using Azure CLI or GitHub Actions

## 🔧 Environment Variables

The application doesn't require any environment variables by default, but you can add them for customization:

```bash
# Optional: Set custom port
STREAMLIT_SERVER_PORT=8501

# Optional: Set custom address
STREAMLIT_SERVER_ADDRESS=0.0.0.0
```

## 📊 Monitoring and Logs

### Streamlit Cloud
- Built-in monitoring dashboard
- Automatic log collection
- Performance metrics

### Heroku
```bash
# View logs
heroku logs --tail

# Monitor dyno usage
heroku ps
```

### Docker
```bash
# View container logs
docker logs <container_id>

# Monitor resource usage
docker stats
```

## 🔒 Security Considerations

1. **HTTPS**: Ensure your deployment uses HTTPS
2. **Environment Variables**: Store sensitive data in environment variables
3. **Access Control**: Implement authentication if needed
4. **Rate Limiting**: Consider adding rate limiting for production use

## 🚨 Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Kill process using port 8501
lsof -ti:8501 | xargs kill -9
```

**Dependencies Not Found**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

**Streamlit Version Issues**
```bash
# Upgrade Streamlit
pip install --upgrade streamlit
```

### Getting Help

- Check the [Streamlit documentation](https://docs.streamlit.io/)
- Review the application logs
- Open an issue on GitHub

## 📈 Performance Optimization

1. **Caching**: Use Streamlit's caching for expensive operations
2. **Session State**: Optimize session state usage
3. **Resource Limits**: Monitor memory and CPU usage
4. **CDN**: Use CDN for static assets

---

**Happy Deploying! 🎉** 