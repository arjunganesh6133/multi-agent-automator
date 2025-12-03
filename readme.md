@"
# Multi-Agent Marketing Campaign Automator

AI-powered tool that uses multiple specialized agents to create complete marketing campaigns.

## Features

- 🔍 Research Agent: Analyzes market trends
- ✍️ Copywriter Agent: Creates compelling ad copy
- 🎨 Art Director Agent: Generates image prompts
- 📋 Manager Agent: Assembles final campaign brief

## Installation

\`\`\`bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/multi-agent-automator.git
cd multi-agent-automator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
\`\`\`

## Setup

1. Get API key from OpenAI or Google Gemini
2. Create \`.env\` file:
\`\`\`
OPENAI_API_KEY=your-key-here
# OR
GOOGLE_API_KEY=your-key-here
\`\`\`

## Usage

\`\`\`bash
python main.py
\`\`\`

Enter your campaign topic when prompted.

## Technologies

- CrewAI 1.6.1
- LangChain
- OpenAI / Google Gemini
- Python 3.10+

## License

MIT
"@ | Out-File -FilePath README.md -Encoding utf8
