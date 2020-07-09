
def put_parent_node(db, parent_node, child_node):
    db.change_parent_node(parent_node, child_node)
    return {
        "status": "Success"
    }
