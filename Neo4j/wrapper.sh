#!/bin/bash

set -m

# Start the primary process and put it in the background
/docker-entrypoint.sh neo4j &

# Start helper process to prepopulate graph with nodes.
./create-tree.sh

# now we bring the primary process back into the foreground
# and leave it there
fg %1