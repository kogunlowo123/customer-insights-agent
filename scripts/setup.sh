#!/bin/bash
set -euo pipefail
echo "Setting up Customer Insights Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
