from crewai import Crew, Process
from tasks import create_campaign_tasks
from agents import (
    research_agent,
    copywriter_agent,
    art_director_agent,
    manager_agent
)
import os
from dotenv import load_dotenv

load_dotenv()

def run_campaign_creator(campaign_topic: str):
    """Run the multi-agent workflow for creating a marketing campaign"""
    
    print(f"\n{'='*60}")
    print(f"Starting Marketing Campaign Creation")
    print(f"Topic: {campaign_topic}")
    print(f"{'='*60}\n")
    
    # Create tasks
    tasks = create_campaign_tasks(campaign_topic)
    
    # Create crew
    crew = Crew(
        agents=[
            research_agent,
            copywriter_agent,
            art_director_agent,
            manager_agent
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the workflow
    result = crew.kickoff()
    
    print(f"\n{'='*60}")
    print("FINAL MARKETING CAMPAIGN BRIEF")
    print(f"{'='*60}\n")
    print(result)
    
    # Save to file
    filename = f"campaign_brief_{campaign_topic.replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(result))
    
    print(f"\n✅ Brief saved to: {filename}")
    
    return result

if __name__ == "__main__":
    campaign_topic = input("Enter your campaign topic: ")
    
    if not campaign_topic:
        campaign_topic = "Eco-Friendly Water Bottles"
    
    run_campaign_creator(campaign_topic)