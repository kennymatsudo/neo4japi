#!/bin/bash

echo "Setting up initial tree..."

until cat /var/lib/neo4j/import/create-tree.cypher |cypher-shell -u neo4j -p password
do
  echo "create initial tree failed, sleeping"
  sleep 10
done

echo "Successfully created inital tree"
