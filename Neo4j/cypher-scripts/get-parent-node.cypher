// Get Parent Node
MATCH (node:Company)-[:PARENT]->(parent:Company)
WHERE node.id = 6
RETURN parent