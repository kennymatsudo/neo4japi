// Create Owner Table
MATCH ownership = shortestPath((owner:Company)-[:CHILD*0..]->(acquired:Company))
WHERE NOT ()-[:CHILD]->(owner)
RETURN acquired.id AS company, head(nodes(ownership)).id AS owner;