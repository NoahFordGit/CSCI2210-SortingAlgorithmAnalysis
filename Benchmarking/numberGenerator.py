class NumberGenerator:
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