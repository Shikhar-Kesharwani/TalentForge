# TalentForge

Resume Retrieval-Augmented Generation (RAG) system with AI classification and semantic search.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Overview

TalentForge is a resume search system that uses artificial intelligence and vector embeddings to find top candidates. Instead of keyword matching, it understands context by:

- Classifying queries into 24 job categories using OpenAI
- Embedding both queries and resumes as vectors
- Performing semantic search in Pinecone
- Generating human-readable answers with an LLM
- Showing a complete trace of how results were found

It's designed for recruiters, HR teams, and talent acquisition professionals who need fast, intelligent candidate retrieval.

## Features

- AI-Powered Category Classification - Automatically routes queries to one of 24 predefined job categories
- Semantic Vector Search - Uses 1536-dimensional embeddings for conceptual matching
- Real-Time Answer Generation - Synthesizes top-5 resumes into actionable responses
- Full Pipeline Transparency - Shows classification, embedding, search, and generation steps with timing
- Interactive Streamlit UI - Clean interface with answer and document display
- Batch Upsert - Efficiently load entire resume databases
- Customizable Models - Swap OpenAI models and adjust Pinecone settings

## Tech Stack

- Frontend: Streamlit
- Backend: Python 3.9+
- LLM & Embeddings: OpenAI API (gpt-4o-mini, text-embedding-3-small)
- Vector Database: Pinecone (serverless, cosine distance)
- Data Processing: Pandas, NumPy
- Validation: Pydantic
- Utilities: python-dotenv, tqdm

## Getting Started

### Prerequisites

- Python 3.9 or later
- OpenAI API Key
- Pinecone API Key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Shikhar-Kesharwani/TalentForge.git
cd TalentForge
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the project root:
```
OPENAI_API_KEY=sk-...
PINECONE_API_KEY=pc-...
PINECONE_INDEX=resumes-index
PINECONE_CLOUD=aws
PINECONE_REGION=us-east-1
```

5. Load your resume data (one-time setup):
```bash
python scripts/upsert_resumes.py --csv Resume.csv
```

This will:
- Create/verify the Pinecone index (1536 dimensions, cosine distance)
- Embed each resume
- Upsert records with metadata

6. Launch the Streamlit app:
```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Usage

### Web Interface

1. Enter your query in the Streamlit text box
2. The system automatically classifies the query and searches for matching resumes
3. View the LLM-generated answer in the left panel
4. See matched resumes with scores in the right panel
5. Expand the trace to see detailed execution steps

### Programmatic Use

```python
from src.query_pipeline import retrieve

result = retrieve("Find senior engineers with cloud experience")

print(result['category'])      # Job category
print(result['answer'])        # LLM-generated response
print(result['top_matches'])   # List of matched resumes
print(result['trace'])         # Execution trace
```

## Project Structure

TalentForge/
- app.py - Streamlit web interface
- requirements.txt - Python dependencies
- .env - Environment variables (not committed)
- README.md - This file

scripts/
- upsert_resumes.py - Batch load and index resumes

src/
- config.py - Configuration and constants
- embed.py - OpenAI embeddings
- llm.py - OpenAI LLM integration
- pinecone_client.py - Pinecone setup and queries
- query_pipeline.py - Orchestration logic
- tools.py - Pydantic models for validation

## How It Works

Step 1: Category Classification
User query is sent to OpenAI (gpt-4o-mini) which returns one of 24 job categories.

Step 2: Query Embedding
The query is embedded using OpenAI's text-embedding-3-small model (1536 dimensions).

Step 3: Metadata-Filtered Vector Search
Query vector is searched against Pinecone index with category filter. Returns top-5 resumes by cosine distance.

Step 4: Answer Generation
Top-5 matched resumes and original query are sent to OpenAI LLM to generate a natural language response.

Step 5: Display Results
Answer, matched documents, and execution trace are displayed in the Streamlit UI.

## Environment Variables

OPENAI_API_KEY (required) - API key for OpenAI
PINECONE_API_KEY (required) - API key for Pinecone
PINECONE_INDEX (optional, default: resumes-index) - Name of Pinecone index
PINECONE_CLOUD (optional, default: aws) - Pinecone cloud provider
PINECONE_REGION (optional, default: us-east-1) - Pinecone region

## Data Format

Your resume CSV must have:
- Resume (required) - Full resume text
- Category (required) - One of 24 predefined categories
- id (optional) - If omitted, auto-generated as row_0, row_1, etc.

Supported Categories:
HR, DESIGNER, INFORMATION-TECHNOLOGY, TEACHER, ADVOCATE, BUSINESS-DEVELOPMENT, HEALTHCARE, FITNESS, AGRICULTURE, BPO, SALES, CONSULTANT, DIGITAL-MEDIA, AUTOMOBILE, CHEF, FINANCE, APPAREL, ENGINEERING, ACCOUNTANT, CONSTRUCTION, PUBLIC-RELATIONS, BANKING, ARTS, AVIATION

## Contributing

1. Fork the repository
2. Create a feature branch (git checkout -b feature/my-feature)
3. Commit changes (git commit -m "Add my feature")
4. Push to branch (git push origin feature/my-feature)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See LICENSE file for details.
