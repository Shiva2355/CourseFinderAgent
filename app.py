from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain_tavily import TavilySearch
import os
from langchain.tools import tool
from dotenv import load_dotenv
import requests
load_dotenv()
# Step 1: Initialize the Model
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
YOUTUBE_API_KEY=os.getenv("YOUTUBE_API_KEY")
model=init_chat_model(
    "google_genai:gemini-3.8-flash",
    api_key=GOOGLE_API_KEY,
)

# Step 2: Create Destination Research Tool (Tavily)
course_research_tool=TavilySearch(
    max_results=5,
    search_depth="advanced",
    tavily_api_key=TAVILY_API_KEY
)
@tool
# Step 3: Create Flight Search Tool
def search_courses(skill: str) -> list:
    """Search for free video courses and tutorials on YouTube."""
    url = "https://www.googleapis.com/youtube/v3/search"

    response = requests.get(url, params={
        "part": "snippet",
        "q": skill,
        "type": "video",
        "maxResults": 5,
        "key": YOUTUBE_API_KEY
    })

    data = response.json()

    videos = []

    for item in data.get("items", []):
        videos.append({
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "channel": item["snippet"]["channelTitle"],
            "video_id": item["id"]["videoId"],
            "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })

    return videos

system_prompt="""You are a CourseFinder assistant that helps students discover the best learning resources.
You have access to these tools:
- course_research_tool: Research learning roadmaps, free resources, certification options, and skill prerequisites
- search_courses: Find free video courses and tutorials on YouTube
Help students by:
1. Using course_research_tool to provide a comprehensive learning roadmap
2. Using search_courses to find relevant YouTube tutorials and courses
3. Present results in clear sections: Learning Roadmap and Video Courses
Do NOT use markdown format. Use plain text with clear headings."""
agent=create_agent(
    model=model,
    tools=[course_research_tool,search_courses],
    system_prompt=system_prompt

)
# Step 4: Define System Prompt


# Step 5: Create and Run the Agent

response = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "I want to learn Machine Learning from scratch. Show me the best roadmap and find me beginner-friendly courses"
        }
    ]
})

print(resources["messages"][-1].content["text"][0])