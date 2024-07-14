#!/usr/bin/env bash
set -euo pipefail

git log --pretty='%h | %an | %ad' --date=iso

