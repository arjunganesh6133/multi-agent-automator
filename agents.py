from crewai import Agent
from tools import research_trends, generate_image_prompt
import os
from dotenv import load_dotenv

load_dotenv()

# Research Agent
research_agent = Agent(
    role='Research Agent',
    goal='Analyze current market trends and consumer behavior',
    backstory="""You are an expert market researcher with 10 years of experience 
    in analyzing consumer trends and market dynamics. You have a keen eye for 
    emerging patterns and data-driven insights.""",
    tools=[research_trends],
    verbose=True,
    allow_delegation=False
)

# Copywriter Agent
copywriter_agent = Agent(
    role='Copywriter Agent',
    goal='Create compelling and persuasive ad copy',
    backstory="""You are a creative copywriter with expertise in crafting 
    engaging marketing messages that convert. You understand psychology, 
    persuasion techniques, and brand voice.""",
    verbose=True,
    allow_delegation=False
)

# Art Director Agent
art_director_agent = Agent(
    role='Art Director Agent',
    goal='Generate creative visual concepts and image prompts',
    backstory="""You are a visionary art director with a background in 
    digital design and visual storytelling. You excel at translating 
    concepts into powerful visual directions.""",
    tools=[generate_image_prompt],
    verbose=True,
    allow_delegation=False
)

# Manager Agent
manager_agent = Agent(
    role='Manager Agent',
    goal='Coordinate the team and assemble the final marketing brief',
    backstory="""You are an experienced marketing project manager who 
    excels at coordinating creative teams and ensuring all elements 
    come together cohesively.""",
    verbose=True,
    allow_delegation=True
)