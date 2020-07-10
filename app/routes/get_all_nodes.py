"""Module responsible for returning all nodes within the graph.
"""


def get_all_nodes(db) -> dict:
    all_nodes = db.get_all()
    return {
        "data": [node['n'] for node in all_nodes]
    }
