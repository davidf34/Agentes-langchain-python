from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def split_documents(documents:list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50,
        length_function = len,
        separators = ["\n\n", "\n", " ",""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks