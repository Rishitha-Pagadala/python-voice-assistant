# Dev - The AI Voice Assistant

This is a Python-based AI Voice Assistant named "Dev" that runs locally on your machine. It uses speech recognition to listen to commands, local text-to-speech for responses, and a local LLM (via Ollama) for conversational abilities.

![image](https://github.com/user-attachments/assets/282dbd62-8f1e-43d0-95f6-65486bc9da72)

## Features

- **Voice & Text Interaction**: Control the assistant using your voice or by typing in the chat interface.
- **Real-time Tools**:
  - Get the current time.
  - Get a live weather report.
  - Tell you a random programming joke.
  - Perform basic calculations.
- **Web & Media Control**:
  - Open Google, YouTube, or GitHub.
  - Search Google for any topic.
  - **Play any video on YouTube** by automatically finding and playing the top search result.
  - Play local music from your computer.
- **LLM-Powered Conversations**: For any query not recognized as a command, it uses a local Large Language Model (`llama3.2`) to generate a helpful response.
- **System Control**: Can close all open browser windows.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
1.  **Python 3.8+**
2.  **Git**
3.  **Ollama**: This project requires a locally running Ollama instance to power the conversational AI.
    - [Download and install Ollama here](https://ollama.com/).

## Installation & Setup

Follow these steps to get your local copy of the project up and running.

**1. Clone the Repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```
*(Replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` with your actual details)*

**2. Create and Activate a Virtual Environment:**
It's highly recommended to use a virtual environment to keep dependencies isolated.
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Required Packages:**
The `requirements.txt` file contains all the necessary Python libraries.
```bash
pip install -r requirements.txt
```
> **Note on PyAudio**: If `pip install pyaudio` fails on Windows, a common solution is to use `pipwin`:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

**4. Set up the Local LLM (Ollama):**
Make sure Ollama is running. Then, pull the `llama3.2` model.
```bash
ollama pull llama3.2
```

**5. Configure the Music Directory:**
Open the `dev_logic.py` file and update the `MUSIC_DIR` variable to point to the music folder on your computer.
```python
# In dev_logic.py
MUSIC_DIR = "C:\\Users\\YourUsername\\Music"  # Update this path!
```

## Usage

To run the application, execute the following command in your terminal from the project directory:
```bash
streamlit run app.py
```
This will open the assistant's user interface in your web browser. You can start interacting with it immediately!

---
