"""Module responsible for returning all the descendants of a given node.
"""


def get_node_descendants(db, node_id: int) -> dict:
    node_descendants = db.get_node_descendants(node_id)
    return {
        "data": {
            "children": [record['descendants'] for record in node_descendants]
        }
    }
