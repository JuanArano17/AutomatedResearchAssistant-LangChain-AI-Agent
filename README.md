# Automated Research Assistant - LangChain AI Agent

## Overview

The Automated Research Assistant is an AI-powered tool designed to assist with research tasks. Built using the LangChain framework, it leverages advanced natural language processing to automate tasks such as information retrieval, summarization, and analysis. This project aims to streamline research workflows and enhance productivity.

## Features

- **Information Retrieval**: Fetch relevant data from various sources.
- **Summarization**: Generate concise summaries of large text inputs.
- **Customizable Workflows**: Tailor the assistant to specific research needs.
- **Extensibility**: Easily integrate additional modules or APIs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JuanArano17/AutomatedResearchAssistant-LangChain-AI-Agent.git
   ```
2. Navigate to the project directory:
   ```bash
   cd AutomatedResearchAssistant-LangChain-AI-Agent
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```
2. Follow the prompts to interact with the assistant.

### Example

```bash
> What topic would you like to research?
> Artificial Intelligence
> Fetching information...
> Summarizing data...
> Summary: Artificial Intelligence (AI) is the simulation of human intelligence in machines...
```

## Configuration

To configure the assistant, you need to set up the following environment variables in a `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key for accessing the OpenAI services.
- `OPENAI_MODEL_NAME`: The name of the OpenAI model to use (e.g., `gpt-4`, `gpt-3.5-turbo`).

Example `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-4
```

Place the `.env` file in the root directory of the project.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/hwchase17/langchain) for the foundational framework.
- OpenAI for their APIs and tools.