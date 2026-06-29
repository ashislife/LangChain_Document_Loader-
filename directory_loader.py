from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)
docs=loader.load()

print(len(docs)) #evry pdf page count 

print(docs[0].page_content)
print(docs[0].metadata) #read pdf1 page 1

