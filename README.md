# CourseFinderAgent 🎓

An AI-powered course discovery agent that helps students find learning roadmaps and beginner-friendly video courses.

## 🚀 Features

* AI-generated learning roadmap using Google Gemini
* Research learning resources using Tavily
* Search YouTube for relevant courses and tutorials
* Beginner-friendly course recommendations
* Agent-based workflow using LangChain

## 🛠️ Tech Stack

* Python
* LangChain
* LangGraph
* Google Gemini
* Tavily Search
* YouTube Data API
* Python-dotenv

## 📁 Project Structure

```text
CourseFinderAgent/
│
├── app.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Shiva2355/CourseFinderAgent.git
cd CourseFinderAgent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
YOUTUBE_API_KEY=your_youtube_api_key
```

Never commit your `.env` file to GitHub.

## ▶️ Run

```bash
python app.py
```

## 🔄 How It Works

```text
User
  ↓
LangChain Agent
  ↓
Google Gemini
  ↓
 ┌─────────────────────┐
 │                     │
Tavily Search     YouTube API
 │                     │
Learning Roadmap   Video Courses
 └──────────┬──────────┘
            ↓
       Final Response
```

## 💡 Example

User:

> I want to learn Machine Learning from scratch. Show me the best roadmap and beginner-friendly courses.

The agent researches the required skills, creates a learning roadmap, and searches YouTube for relevant courses.

## 🔐 Security

API keys are stored in environment variables and should never be committed to the repository.

## 👨‍💻 Author

Shiva
