#!/bin/bash

# uv run src/database/models.py --initial_commit
# uv run src/database/models.py --philosopher john --quotes ABCDE
uv run src/database/models.py --delete --philosopher john --quotes ABCDE
