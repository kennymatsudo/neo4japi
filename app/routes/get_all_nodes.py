
def get_all_nodes(db):
    all_nodes = db.get_all()
    return {
        "data": all_nodes
    }
