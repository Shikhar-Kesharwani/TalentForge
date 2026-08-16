<!-- palette: #0F172A, #3B82F6 | theme: RAG Architecture & Vector Intelligence -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0F172A&height=220&section=header&text=TalentForge&fontSize=65&fontColor=ffffff&fontAlignY=38" alt="TalentForge Header Banner" width="100%" />

<a href="https://readme-typing-svg.demolab.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=3B82F6&center=true&width=650&lines=Resume+Retrieval-Augmented+Generation+(RAG);Pinecone+Vector+Database+%26+Semantic+Search;AI-Powered+Candidate+Classification" alt="TalentForge Typing Tagline" />
</a>

<p align="center">
  <b>Resume Retrieval-Augmented Generation (RAG) system with AI classification and semantic search.</b>
</p>

<p align="center">
  <a href="https://github.com/Shikhar-Kesharwani/TalentForge/graphs/contributors"><img src="https://img.shields.io/github/contributors/Shikhar-Kesharwani/TalentForge?style=for-the-badge&color=0F172A" alt="Contributors" /></a>
  <a href="https://github.com/Shikhar-Kesharwani/TalentForge/network/members"><img src="https://img.shields.io/github/forks/Shikhar-Kesharwani/TalentForge?style=for-the-badge&color=3B82F6" alt="Forks" /></a>
  <a href="https://github.com/Shikhar-Kesharwani/TalentForge/stargazers"><img src="https://img.shields.io/github/stars/Shikhar-Kesharwani/TalentForge?style=for-the-badge&color=0F172A" alt="Stargazers" /></a>
  <a href="https://github.com/Shikhar-Kesharwani/TalentForge/issues"><img src="https://img.shields.io/github/issues/Shikhar-Kesharwani/TalentForge?style=for-the-badge&color=3B82F6" alt="Issues" /></a>
  <a href="https://github.com/Shikhar-Kesharwani/TalentForge/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Shikhar-Kesharwani/TalentForge?style=for-the-badge&color=0F172A" alt="License" /></a>
</p>

---

</div>

## 📑 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🖼️ Architecture Framework](#️-architecture-framework)
- [💻 Tech Stack](#-tech-stack)
- [🏗️ RAG Pipeline Workflow](#️-rag-pipeline-workflow)
- [🚀 Getting Started](#-getting-started)
  - [📋 Prerequisites](#-prerequisites)
  - [⚙️ Installation](#️-installation)
  - [🔑 Environment Variables](#-environment-variables)
- [📖 Usage](#-usage)
- [📁 Project Structure](#-project-structure)
- [🧪 Testing](#-testing)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Contact & Support](#-contact--support)

---

## 🎯 Overview

**TalentForge** is an AI-powered Resume Retrieval-Augmented Generation (RAG) platform designed to query, analyze, and classify candidate resumes using vector embeddings and Large Language Models. 

Instead of relying on basic keyword matching, TalentForge converts unstructured candidate documents into high-dimensional vector embeddings stored in a Pinecone vector index. Recruiters can query candidate repositories in natural language, retrieve contextually relevant resume chunks, and receive AI-generated candidate evaluations and skill summaries in real time.

> **Key Takeaway:** Combines **Pinecone Vector Search** + **OpenAI LLM Reasoning** + **Streamlit UI** to deliver accurate, context-aware candidate retrieval.

---

## ✨ Key Features

### 🔍 Semantic Resume Search & Q&A
* Natural language querying across candidate CV databases (e.g., *"Find candidates with 3+ years in PyTorch and AWS"*).
* Vector similarity retrieval powered by OpenAI embeddings and Pinecone Indexing.

### 🤖 AI Candidate Classification & Scoring
* Automatic skill extraction and competency categorization across 24 predefined domain categories.
* Generates contextual candidate summaries based on retrieved resume chunks.

### 📄 Multi-Document Processing Pipeline
* Ingests and processes candidate resumes from the `Resume/` directory using `scripts/upsert_resumes.py`.
* Automated text chunking, tokenization, and embedding generation.

### 🖥️ Interactive Web Dashboard
* Clean Streamlit interface (`app.py`) for entering queries, viewing matches, and inspecting processing traces.

---

## 🖼️ Architecture Framework

<div align="center">

![TalentForge Framework](framework.png)

*Figure 1: High-Level TalentForge RAG Architecture & Ingestion Flow*

</div>

---

## 💻 Tech Stack

<div align="center">

### Core Language & Framework
[![Python](https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit_1.33+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)

### Vector Database & AI Services
[![Pinecone](https://img.shields.io/badge/Pinecone_3.0+-000000?style=for-the-badge&logo=pinecone&logoColor=white)](https://www.pinecone.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI_1.14+-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)

### Document Parsing & Vector Utilities
[![Pandas](https://img.shields.io/badge/Pandas_2.1+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic_2.4+-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev/)

</div>

---

## 🏗️ RAG Pipeline Workflow

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'primaryColor': '#0F172A', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#3B82F6', 'lineColor': '#3B82F6', 'secondaryColor': '#3B82F6', 'tertiaryColor': '#F4F6F8'}}}%%
graph TD
    A[📄 Resumes in Resume/ Folder] --> B[⚙️ Text Extraction & Chunking - scripts/upsert_resumes.py]
    B --> C[🧠 OpenAI Embeddings API - src/embed.py]
    C --> D[(🌲 Pinecone Vector Index - src/pinecone_client.py)]
    E[💬 Recruiter Query / Prompt] --> C
    D -->|Top-K Similar Chunks| F[🤖 OpenAI LLM Context Synthesis - src/query_pipeline.py]
    F --> G[🖥️ Streamlit Interactive UI - app.py]
```

---

## 🚀 Getting Started

### 📋 Prerequisites

Verify that your local system has the following requirements:

* **Python**: `v3.10` or higher
* **pip**: `v22.0` or higher
* **OpenAI API Key**: [Get key from OpenAI](https://platform.openai.com/)
* **Pinecone API Key & Index**: [Get key from Pinecone](https://www.pinecone.io/)

### ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shikhar-Kesharwani/TalentForge.git
   cd TalentForge
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

   # On Windows:
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=sk-proj-xxxxxxxxxxxx
   PINECONE_API_KEY=pcsk_xxxxxxxxxxxx
   PINECONE_INDEX=resumes-index
   PINECONE_CLOUD=aws
   PINECONE_REGION=us-east-1
   ```

5. **Run Resume Ingestion & Vector Embedding**
   ```bash
   python scripts/upsert_resumes.py --csv Resume/Resume_cleaned.csv
   ```

6. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

### 🔑 Environment Variables

| Variable Name | Description | Required | Example |
| :--- | :--- | :---: | :--- |
| `OPENAI_API_KEY` | Secret API key for OpenAI text embeddings and LLM | Yes | `sk-proj-xxxxxxxxxxxx` |
| `PINECONE_API_KEY` | Secret API key for Pinecone vector store | Yes | `pcsk_xxxxxxxxxxxx` |
| `PINECONE_INDEX` | Name of your target Pinecone vector index | Yes | `resumes-index` |
| `PINECONE_CLOUD` | Cloud provider hosting Pinecone index | No | `aws` |
| `PINECONE_REGION` | Pinecone deployment region | No | `us-east-1` |

---

## 📖 Usage

### Running Ingestion & Web App

1. Place candidate resume CSV/documents inside the `Resume/` folder.
2. Run the script to generate embeddings and populate Pinecone index:
   ```bash
   python scripts/upsert_resumes.py --csv Resume/Resume_cleaned.csv
   ```
3. Start the Streamlit user interface:
   ```bash
   streamlit run app.py
   ```
4. Ask natural language questions like:
   * *"Which candidates have experience with Docker and Kubernetes?"*
   * *"Summarize top candidates for a Senior Data Scientist role."*

---

## 📁 Project Structure

```
TalentForge/
├── 📄 app.py                  # Main Streamlit web application entrypoint
├── 📄 framework.png           # Architecture diagram asset
├── 📁 Resume/                 # Storage folder for candidate resumes
├── 📁 scripts/                # Utility scripts for data processing & ingestion
│   └── 📄 upsert_resumes.py   # Embeddings generation and Pinecone upload
├── 📁 src/                    # Core RAG pipeline modules
│   ├── 📄 config.py           # API keys and environment configuration
│   ├── 📄 embed.py            # OpenAI embedding generation
│   ├── 📄 llm.py              # LLM prompt templates and text generation
│   ├── 📄 pinecone_client.py  # Pinecone index management & query execution
│   ├── 📄 query_pipeline.py   # End-to-end RAG query workflow
│   └── 📄 tools.py            # Helper tools & formatters
├── 📄 requirements.txt        # Python package dependencies
├── 📄 .gitignore              # Files ignored by version control
└── 📄 README.md               # Repository documentation
```

---

## 🧪 Testing

Run unit tests and verify RAG query connections:

```bash
# Execute test scripts
pytest tests/ -v
```

---

## 🗺️ Roadmap

- [x] Pinecone vector database integration & document chunking
- [x] Streamlit web UI with live query interface
- [x] OpenAI RAG retrieval pipeline
- [ ] Multi-file drag-and-drop ingestion directly in Streamlit UI
- [ ] Hybrid BM25 + Dense vector retrieval strategy
- [ ] Automated candidate score summary export (PDF/CSV)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Repository.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 📬 Contact & Support

* **Maintainer**: Shikhar Kesharwani - [@Shikhar-Kesharwani](https://github.com/Shikhar-Kesharwani)
* **GitHub Repository**: [Shikhar-Kesharwani/TalentForge](https://github.com/Shikhar-Kesharwani/TalentForge)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0F172A&height=30" width="100%" alt="Footer Bar" />

<p><sub>Built with care for recruiters and data teams worldwide • Star this repo if you find it helpful! 🌟</sub></p>

</div>
