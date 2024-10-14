class PredicateDeriver:
    def __init__(self):
        self.relationships = {}

    # Add a relationship between subject, relation, and object
    def add_relationship(self, subject, relation, obj):
        self.relationships[(subject, relation)] = obj

    # Derive the relationship recursively
    def derive(self, subject, relation):
        if (subject, relation) in self.relationships:
            obj = self.relationships[(subject, relation)]
            # If object has further relations, continue deriving
            if (obj, relation) in self.relationships:
                return self.derive(obj, relation)
            return obj
        return None

# Example usage
deriver = PredicateDeriver()
deriver.add_relationship('Sachin', 'is', 'batsman')
deriver.add_relationship('batsman', 'is', 'cricketer')
result = deriver.derive('Sachin', 'is')
print(f"Sachin is Cricketer: {result}")
