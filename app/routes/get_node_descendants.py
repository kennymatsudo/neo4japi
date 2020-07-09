
def get_node_descendants(db, node_id):
    node_descendants = db.get_node_descendants(node_id)
    return {
        "data": {
            "children": node_descendants
        }
    }
