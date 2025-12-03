from crewai.tools import tool

@tool
def research_trends(topic: str) -> str:
    """Research current trends for a given topic."""
    return f"""
    Current trends for {topic}:
    - Trend 1: AI-powered personalization is growing
    - Trend 2: Short-form video content dominates
    - Trend 3: Sustainability messaging resonates
    - Trend 4: Interactive content increases engagement
    """

@tool
def generate_image_prompt(description: str) -> str:
    """Generate image prompt for DALL-E or Stable Diffusion."""
    return f"""
    Image Prompt: Professional marketing visual, {description}, 
    high quality, 8k resolution, vibrant colors, modern aesthetic, 
    clean composition, commercial photography style
    """