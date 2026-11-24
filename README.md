
# Business Research Agent

An AI-powered Business Research Agent that searches the web for company information and uses Generative AI to analyze the findings and generate structured business research reports.

## Features

- Searches the web using Tavily Search API.
- Collects company information from multiple online sources.
- Uses Google Gemini to analyze search results.
- Generates structured business research reports.
- Provides company overview, products, services, target customers, and growth opportunities.
- Suggests strategic business recommendations.
- Includes source references and website URLs.
- Automatically saves reports as Markdown files.
- Handles temporary Gemini service errors using retry logic.

## Technologies Used

- Python
- Google Gemini API
- Tavily Search API
- python-dotenv

## Project Structure

```text
business-research-agent/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── reports/
│   └── Generated research reports
│
└── venv/
```

## Setup Instructions

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd business-research-agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never upload your actual API keys to GitHub.

### 6. Run the application

```bash
python main.py
```

Enter a company name when prompted.

## Generated Reports

The application automatically creates a `reports/` directory and saves research reports in Markdown format.

Example:

- infosys_report.md
- tcs_report.md
- wipro_report.md

## Workflow

1. User enters a company name.
2. Tavily searches the web for relevant information.
3. Search results are collected and processed.
4. Gemini analyzes the retrieved information.
5. A structured business research report is generated.
6. The report and source references are saved locally.

## Security

- API keys are stored in a local `.env` file.
- The `.env` file is excluded from Git using `.gitignore`.
- Virtual environment files are not included in the repository.

## Author

Developed as part of the [NEXLEVR](https://github.com/Nexlevr). Agentic AI Developer Intermediate Tasks.
