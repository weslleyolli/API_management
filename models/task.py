class Task:
    def __init__(self, id ,name, description, completed=False):
        self.id = id
        self.name = name
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'completed': self.completed
        }