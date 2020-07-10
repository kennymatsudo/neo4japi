from neo4j import GraphDatabase


class NeoDB:

    def __init__(self, uri: str, user: str, password: str):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_all(self):
        with self.driver.session() as session:
            results = session.run("MATCH(n) RETURN n")
            return results.data()

    def get_node_info(self, node_id: int):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (n:Company {id:$node_id}) "
                "RETURN n", node_id=int(node_id))
            return results.single()

    def get_node_descendants(self, node_id: int):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (root:Company{id:$node_id})-[:CHILD*]->(descendants:Company) "
                "RETURN descendants", node_id=int(node_id))
            return results.data()

    def delete_current_pc_relation(self, node_id: int):
        with self.driver.session() as session:
            session.run(
                "MATCH (curr:Company{id:$node_id})-[pr:PARENT]->(), (curr:Company{id:$node_id})<-[cr:CHILD]-() "
                "DELETE pr,cr", node_id=int(node_id))

    def create_pc_relation(self, parent_node: int, child_node: int):
        with self.driver.session() as session:
            session.run(
                "MATCH(child: Company{id: $child_node}), (parent: Company{id: $parent_node}) "
                "MERGE(child)-[:PARENT] -> (parent) "
                "MERGE (child)<-[:CHILD]-(parent) ",
                parent_node=int(parent_node),
                child_node=int(child_node))

    def get_parent_node(self, node_id: int):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (node:Company)-[:PARENT]->(parent:Company) "
                "WHERE node.id=$node_id "
                "RETURN parent", node_id=int(node_id)).single()
            if results:
                return results.value()
            return None

    def get_node_height(self, node_id: int):
        with self.driver.session() as session:
            results = session.run(
                "MATCH k=(n: Company)-[r:PARENT*0..] -> (c: Company) "
                "WHERE n.id=$node_id "
                "WITH n, collect(length(k)) as height "
                "UNWIND height as e "
                "RETURN max(e) as height", node_id=int(node_id)).single()
            if results:
                return results.value()
            return None

    def get_root_node(self):
        with self.driver.session() as session:
            results = session.run(
                "MATCH(root: Company)-[:CHILD*0..] -> (child: Company) "
                "WHERE NOT()-[:CHILD] -> (root) "
                "RETURN root").single()
            if results:
                return results.value()
            return None
