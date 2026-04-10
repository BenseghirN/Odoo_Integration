class game:
    def __init__(self, igdb_id, name, summary=None, release_date=None, cover_url=None):
        self.igdb_id = igdb_id
        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url

    def __repr__(self):
        return f"Game(igdb_id={self.igdb_id}, name='{self.name}', summary='{self.summary}', release_date='{self.release_date}', cover_url='{self.cover_url}')"
    
    def create_new_game(self, igdb_id, name, summary=None, release_date=None, cover_url=None):
        return game(igdb_id, name, summary, release_date, cover_url)
    
    def update_game(self, name, summary=None, release_date=None, cover_url=None):
        self.name = name
        self.summary = summary
        self.release_date = release_date
        self.cover_url = cover_url
    
    def delete_game(self):
        del self