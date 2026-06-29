from langchain_community.document_loaders import WebBaseLoader

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

url="https://www.flipkart.com/audio-video/headset/earphones/wireless-earphones/neckband/~cs-2a0c4b3036f2339cfee37c9c64a79f41/pr?sid=0pm%2Cfcn%2C821%2Ca7x%2C2rv&marketplace=FLIPKART&restrictLocale=true&BU=Mixed"


loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs)) 

print(docs[0].page_content)