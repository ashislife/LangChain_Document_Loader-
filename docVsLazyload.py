from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# Load (take more time )
docs=loader.load()

for document in docs:
    print(document.metadata)

# Lazy loader (less time taking for loding)


docs=loader.lazy_load()

for document in docs:
    print(document.metadata)