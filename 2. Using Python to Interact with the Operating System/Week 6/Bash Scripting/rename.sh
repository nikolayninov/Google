#!/bin/bash

for file in old_website/*.HTM; do
	name=$(basename "$file" .HTM)
	cp "$file" "new_website/$name.html"
done
