.PHONY: help test fmt

help:
	@echo "mood: Minimal mood tracker"

test:
	pytest -q || true

fmt:
	@echo "No formatter configured"

