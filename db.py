from tinydb import TinyDB

class LikeDB:
    def __init__(self, file_path):
        # Initialize the database
        self.db = TinyDB(file_path)

    def add_student(self, user_id):
        """
        Add student in Database
        """
        pass
        
        return self.db[user_id]
    
    def all_likes(self):
        """
        Count all users likes
        """
        pass

    def all_dislikes(self):
        """
        Count all users dislikes
        """
        pass

    def add_like(self, user_id:str):
        """
        Add like to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        pass

    def add_dislike(self, user_id:str):
        """
        Add dislike to the database
        
        Args:
            user_id (str): telegram user id
        Returns:
            The number of likes and dislikes for the post
        """
        pass
            



