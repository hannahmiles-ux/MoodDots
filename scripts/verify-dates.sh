#!/usr/bin/env bash
set -euo pipefail

# Show author and committer dates for verification
git log --pretty=format:'%h | %an | %ad | %cd' --date=iso

