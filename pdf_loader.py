from langchain_community.document_loaders import PyPDFLoader

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader=PyPDFLoader('Syllabi.pdf')


docs=loader.load()

print(docs)

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)