from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("archive/Employee_Handbook.pdf")
pages = loader.load_and_split()
pages = pages[4:]  # Skip the first few pages as they are not required
text = "\n".join([doc.page_content for doc in pages])

print(text)