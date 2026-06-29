from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='students.csv')

docs=loader.load()

print(docs[0])
print(len(docs))
print(docs)
