from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build Pipeline...")
        
        data_loader = AnimeDataLoader(original_csv='data/anime_with_synopsis.csv', processed_csv='data/processed_anime.csv')
        process_csv = data_loader.load_and_process()
        
        logger.info(f"Data loaded and processed....")
        
        vector_builder = VectorStoreBuilder(process_csv)
        vector_builder.build_and_save_vector_store()
        
        logger.info("Vector store built successfully.")
    except CustomException as e:
        logger.error(f"Failed to execute pipeline: {e}")
        raise CustomException(e)
        
        
        
if __name__ == "__main__":
    main()