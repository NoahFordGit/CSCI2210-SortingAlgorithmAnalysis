class DataGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_sorted_1000():
        return list(range(1000))
    
    @staticmethod
    def generate_random_1000():
        import random
        arr = list(range(1000))
        random.shuffle(arr)
        return arr
    
    @staticmethod
    def generate_reverse_1000():
        return list(range(999, -1, -1))
    
    @staticmethod
    def generate_sorted_100000():
        return list(range(100000))
    
    @staticmethod
    def generate_random_100000():
        import random
        arr = list(range(100000))
        random.shuffle(arr)
        return arr  
    
    @staticmethod
    def generate_reverse_100000():
        return list(range(99999, -1, -1))
    
    @staticmethod
    def read_words_from_file(filepath):
        """
        Reads words from a text file and returns them as a list.
        
        Args:
            filepath (str): Path to the text file
            
        Returns:
            list: List of words from the file
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                words = [word.strip() for word in file.readlines() if word.strip()]
            return words
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.")
            return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []
