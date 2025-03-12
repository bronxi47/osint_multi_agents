# Multi-Agent System for OSINT AI Agent with CrewAI

This repository contains a **multi-agent system** built with **CrewAI**, **OpenAI**, and **Serper** to automate agent that gathers information about our target from Google.

## 🚀 Installation Steps

Follow these steps to set up and run the multi-agent system:

### **1️⃣ Create and Activate a Virtual Environment**
```
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 2️⃣ Install Required Dependencies

```
pip3 install crewai
pip3 install crewai_tools
pip3 install python-dotenv
```

### 3️⃣ Create the .env File

Before running the script, make sure to create a .env file in the project directory with your API keys:
```
OPENAI_API_KEY=your-openai-api-key
SERPER_API_KEY=your-serper-api-key
```

### 4️⃣ Run the Multi-Agent
```
python3 main.py
```
### 🎥 Credits

This implementation was inspired by the video from @ArtificialSecurity. All credit for the original idea goes to them!
🔗 Watch the full tutorial here: [YouTube Video
](https://www.youtube.com/watch?v=GfwUGABFjvs)
