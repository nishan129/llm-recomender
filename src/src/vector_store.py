from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv

load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_directory:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_directory = persist_directory
        self.embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        
    def build_and_save_vector_store(self):
        try:
            loader = CSVLoader(file_path=self.csv_path, encoding='utf-8')
            documents = loader.load()
            
            text_splitter = CharacterTextSplitter( chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(documents)
            
            vector_store = Chroma.from_documents(documents=texts, embedding=self.embedding, persist_directory=self.persist_directory)
            vector_store.persist()
            
            return vector_store
        except Exception as e:
            print(f"Error building or saving vector store: {e}")
            return None
        
    def load_vector_store(self):
        try:
            vector_store = Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding)
            return vector_store
        except Exception as e:
            print(f"Error loading vector store: {e}")
            return None