# Deployment Guide

This is how you can run the TalentScout Hiring Assistant on your computer. I am not an expert but I hope this helps.

## What you need

- Python 3 (I used 3.8 but newer should work)
- Git (for downloading the code)
- Internet connection

## How to run it on your computer

1. Download the code:

   Open Command Prompt or Terminal and type:
   
   ```
   git clone https://github.com/yourusername/talentscout-hiring-assistant.git
   cd talentscout-hiring-assistant
   ```

2. Install the stuff it needs:

   ```
   pip install -r requirements.txt
   ```

3. Start the app:

   ```
   streamlit run app.py
   ```

4. Open your browser and go to the link it shows (usually http://localhost:8501 or something like that)

## If you want to put it online

I only tried running it on my computer, but you can try these:

- Streamlit Cloud: You need a GitHub account. Go to https://share.streamlit.io and follow the steps.
- Heroku: I think you need a Procfile and a free account. I didn't try this.
- Railway: I saw people use it for Python apps. You connect your GitHub and follow their steps.
- Docker: If you know Docker, you can use the Dockerfile in the repo.

## Problems I had

- Sometimes the port is busy. Try closing other Streamlit apps or restart your computer.
- If you get errors about missing packages, try running `pip install -r requirements.txt` again.
- If you see OpenAI errors, you probably need an API key. I didn't set this up.

## That's it

Sorry if this isn't very detailed. I just followed what I found online. Good luck! 