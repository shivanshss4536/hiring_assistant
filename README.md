# 🤖 TalentScout Hiring Assistant

A modern, AI-powered recruitment chatbot built with Streamlit that automates the initial screening process for job candidates. The chatbot collects candidate information, analyzes their tech stack, and generates personalized technical questions.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)

## ✨ Features

### 🤝 **Smart Conversation Flow**
- **Intelligent Greeting**: Welcomes candidates and explains the screening process
- **Context Awareness**: Maintains conversation context throughout the session
- **Graceful Exit**: Ends conversation when candidates use keywords like 'bye', 'exit', 'quit'

### 📋 **Comprehensive Information Collection**
- **Personal Details**: Full name, email, phone number
- **Professional Info**: Years of experience, desired position, current location
- **Tech Stack Analysis**: Programming languages, frameworks, databases, tools

### 🧠 **AI-Powered Question Generation**
- **Dynamic Questions**: Generates 3-5 technical questions based on declared tech stack
- **Technology-Specific**: Tailored questions for Python, Java, JavaScript, React, Django, SQL, AWS, Docker, Git, and more
- **Adaptive Learning**: Questions adapt to the candidate's skill set

### 🎨 **Modern User Interface**
- **Beautiful Design**: Gradient headers, chat bubbles, and modern styling
- **Responsive Layout**: Works seamlessly on desktop and mobile devices
- **Interactive Elements**: Hover effects, smooth animations, and intuitive controls
- **Color-Coded Messages**: Blue for user messages, green for bot responses

### 🔒 **Privacy & Security**
- **Local Processing**: All data processed locally, no external storage
- **Session-Based**: Information is not persisted between sessions
- **GDPR Compliant**: No personal data collection or storage

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/talentscout-hiring-assistant.git
   cd talentscout-hiring-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to access the application

## 📁 Project Structure

```
talentscout-hiring-assistant/
├── app.py                 # Main Streamlit application
├── chatbot.py            # Core chatbot logic and conversation management
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore file
```

## 🔧 Configuration

The application is designed to work out-of-the-box with no additional configuration required. All settings are optimized for immediate use.

## 🚀 Deployment

### Local Deployment
The application runs locally by default and is perfect for:
- Personal use
- Internal company screening
- Development and testing

### Cloud Deployment (Optional)

#### Streamlit Cloud
1. Push your code to GitHub
2. Connect your repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

#### Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Deploy using Heroku CLI or GitHub integration

#### AWS/GCP/Azure
- Use containerization with Docker
- Deploy to cloud platforms using their respective services

## 🎯 Usage Guide

### For Recruiters
1. **Start the Application**: Run `streamlit run app.py`
2. **Share the Link**: Provide candidates with the application URL
3. **Review Results**: Monitor candidate responses and technical assessments

### For Candidates
1. **Access the Chatbot**: Open the provided URL
2. **Provide Information**: Answer questions about your background and skills
3. **Technical Assessment**: Respond to personalized technical questions
4. **Complete Screening**: Finish the conversation when ready

## 🔍 Technical Details

### Architecture
- **Frontend**: Streamlit web interface
- **Backend**: Python-based chatbot engine
- **State Management**: Streamlit session state
- **Question Generation**: Rule-based system with technology-specific prompts

### Key Components
- **HiringAssistant Class**: Core chatbot logic with state machine pattern
- **Session Management**: Persistent conversation state across interactions
- **Dynamic Question Generation**: Technology-aware question creation
- **Responsive UI**: Modern, mobile-friendly interface

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for rapid web application development
- Inspired by modern recruitment automation needs
- Designed for educational and professional use

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the documentation
- Review the code comments for implementation details

---

**Made with ❤️ for modern recruitment**
