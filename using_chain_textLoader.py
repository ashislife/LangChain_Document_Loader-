from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.document_loaders import TextLoader 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-9b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# prompt create
prompt=PromptTemplate(
    template='Write the summary for the following poem. \n  {poem}',
    input_variables=['poem']
)

# parser for string 
parser=StrOutputParser()

# document loader 
loader=TextLoader('cricket.txt',encoding='utf-8')
docs=loader.load()
# print(docs)


# pipeline
chain=prompt |model |parser

# invoke the chain from doc loader 
print(chain.invoke({'poem': docs[0].page_content}))
