import pandas as pd

from utils.custom_exception import CustomException

class AnimeDataLoader:
    def __init__(self,original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
        
    def load_and_process(self):
        try:
            df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()
            
            required_cols = {"Name",'Genres',"sypnopsis"}
            
            missing = required_cols - set(df.columns)
            if missing:
                raise ValueError(f"Missing columns in CSV File")
            
            df['combined_info'] = (
                "Title: " + df['Name'] + ".. Overview: " + df['sypnopsis'] + "Genres : " + df['Genres']   
            )
            
            df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')
            
            return self.processed_csv
        except Exception as e:
            print(f"Error loading or processing data: {e}")
            return None