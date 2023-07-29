```python
from py2neo import Graph, Node, Relationship

class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))

    def add_node(self, label, properties):
        node = Node(label, **properties)
        self.graph.create(node)
        return node

    def add_relationship(self, node1, node2, rel_type, properties):
        rel = Relationship(node1, rel_type, node2, **properties)
        self.graph.create(rel)
        return rel

    def query(self, query):
        return self.graph.run(query).data()

    def get_node(self, label, properties):
        return self.graph.nodes.match(label, **properties).first()

    def get_relationship(self, node1, node2, rel_type):
        return self.graph.match((node1, node2), rel_type).first()
```