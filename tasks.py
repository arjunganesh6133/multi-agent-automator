from crewai import Task
from agents import (
    research_agent, 
    copywriter_agent, 
    art_director_agent, 
    manager_agent
)

def create_campaign_tasks(campaign_topic: str):
    """Create all tasks for the marketing campaign"""
    
    # Task 1: Research
    research_task = Task(
        description=f"""
        Research current trends and audience insights for: {campaign_topic}
        
        Provide:
        1. Top 3-5 current trends
        2. Target audience preferences
        3. Competitor analysis
        4. Key messaging opportunities
        """,
        agent=research_agent,
        expected_output="Detailed research report with trends and insights"
    )
    
    # Task 2: Copywriting
    copywriting_task = Task(
        description=f"""
        Based on the research findings, create compelling ad copy for: {campaign_topic}
        
        Deliver:
        1. Main headline (attention-grabbing)
        2. Sub-headline (value proposition)
        3. Body copy (3-4 sentences)
        4. Call-to-action
        5. 3 variations of the headline
        """,
        agent=copywriter_agent,
        expected_output="Complete ad copy with headlines, body text, and CTA",
        context=[research_task]
    )
    
    # Task 3: Art Direction
    art_direction_task = Task(
        description=f"""
        Create visual direction and image prompts for: {campaign_topic}
        
        Provide:
        1. Visual concept description
        2. Color palette recommendations
        3. 2-3 detailed image prompts for DALL-E/Stable Diffusion
        4. Layout suggestions
        """,
        agent=art_director_agent,
        expected_output="Visual direction with detailed image generation prompts",
        context=[research_task, copywriting_task]
    )
    
    # Task 4: Final Assembly
    management_task = Task(
        description=f"""
        Compile all elements into a comprehensive marketing campaign brief for: {campaign_topic}
        
        Assemble:
        1. Executive Summary
        2. Research Insights
        3. Complete Ad Copy (all variations)
        4. Visual Direction & Image Prompts
        5. Implementation Recommendations
        6. Success Metrics
        
        Format as a professional marketing brief.
        """,
        agent=manager_agent,
        expected_output="Complete professional marketing campaign brief",
        context=[research_task, copywriting_task, art_direction_task]
    )
    
    return [research_task, copywriting_task, art_direction_task, management_task]