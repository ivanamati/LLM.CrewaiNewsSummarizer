# Agent News Summarizer

Welcome to **Agent News Summarizer**, a multi-agent AI system designed to research and summarize the latest developments in AI and LLMs. 
This project leverages agentic [crewAI](https://crewai.com) framework to manage and coordinate agents that handle research and reporting tasks efficiently.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/agent_news_summarizer.git
cd agent_news_summarizer 
```

### Step 1: Customizing

**Add your `OPENAI_API_KEY` and `SERPER_API_KEY` into the `.env` file**

- Modify `src\agent_news_summarizer\config\agents.yaml` to define your agents
- Modify `src\agent_news_summarizer\config\agents.yaml` to define your tasks
- Modify `src\agent_news_summarizer\crew.py` to add your own logic, tools and specific args
- Modify `src\agent_news_summarizer\main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
python main.py run
```

This command initializes the agent_news_summarizer Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The project is composed of multiple AI agents, each with unique roles, goals, and tools. 
These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, 
leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

