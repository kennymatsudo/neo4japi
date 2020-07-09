// Get Node Height
MATCH k = (n:Company)-[r:PARENT*0..]->(c:Company) 
where n.id = 4
with n, collect(length(k)) as height
return height