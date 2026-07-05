# LangChain Document Loaders

This repository demonstrates the usage of different document loaders available in LangChain for loading data from various sources such as text files, PDFs, CSV files, directories, Word documents, and web pages.

## Project Structure

```text
LangChain_Document_Loader/
├── books/
├── cricket.txt
├── students.csv
├── Syllabi.pdf
├── text_loader.py
├── pdf_loader.py
├── csv_loader.py
├── directory_loader.py
├── docVsLazyload.py
├── using_chain_textLoader.py
├── webbase_loader.py
├── README.md
├── LICENSE
└── .gitignore
```

## Features

- Text File Loader
- PDF Loader
- CSV Loader
- Directory Loader
- WebBase Loader
- Lazy Loading
- Document Loading with LangChain Chains

## Prerequisites

- Python 3.10+
- LangChain
- langchain-community
- python-dotenv

## Installation

Clone the repository:

```bash
git clone https://github.com/ashislife/LangChain_Document_Loader-.git
```

Navigate to the project directory:

```bash
cd LangChain_Document_Loader-
```

Install the required dependencies:

```bash
pip install langchain langchain-community python-dotenv pypdf pandas beautifulsoup4 lxml
```

## Usage

Run any example individually:

```bash
python text_loader.py
```

```bash
python pdf_loader.py
```

```bash
python csv_loader.py
```

```bash
python directory_loader.py
```

```bash
python webbase_loader.py
```

```bash
python using_chain_textLoader.py
```

```bash
python docVsLazyload.py
```

## Files

| File | Description |
|------|-------------|
| `text_loader.py` | Loads text documents using LangChain's TextLoader. |
| `pdf_loader.py` | Loads PDF documents using a PDF loader. |
| `csv_loader.py` | Loads CSV files as LangChain documents. |
| `directory_loader.py` | Loads multiple documents from a directory. |
| `webbase_loader.py` | Loads web page content using WebBaseLoader. |
| `docVsLazyload.py` | Demonstrates document loading versus lazy loading. |
| `using_chain_textLoader.py` | Uses TextLoader within a LangChain chain. |
| `cricket.txt` | Sample text document. |
| `students.csv` | Sample CSV dataset. |
| `Syllabi.pdf` | Sample PDF document. |
| `books/` | Sample documents used for loading examples. |

## License

This project is licensed under the MIT License.
