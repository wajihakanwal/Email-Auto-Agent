# EmailAutoAgent Crew

Welcome to the EmailAutoAgent Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/email_auto_agent/config/agents.yaml` to define your agents
- Modify `src/email_auto_agent/config/tasks.yaml` to define your tasks
- Modify `src/email_auto_agent/crew.py` to add your own logic, tools and specific args
- Modify `src/email_auto_agent/main.py` to add custom inputs for your agents and tasks
- Modify environment variables in .env

## Set Up Gmail API Authentication
1. **Enable Gmail API**:
- Go to [Google Cloud Console](https://console.cloud.google.com/).
- Enable the **Gmail API**.
- Create **OAuth 2.0 credentials** and download the `credentials.json` file.
2. **Place `credentials.json` in the root directory** of the project.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
or 

```bash
$ uv run auto_run
```
if you are using uv package manager


This command initializes the email_auto_agent Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The email_auto_agent Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the EmailAutoAgent Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
