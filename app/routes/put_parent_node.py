"""Module responsible for re-assigning the parent of a given node.
"""


def put_parent_node(db, parent_node: int, child_node: int) -> dict:
    db.delete_current_pc_relation(child_node)
    db.create_pc_relation(parent_node, child_node)
    return {
        "status": "Success"
    }
