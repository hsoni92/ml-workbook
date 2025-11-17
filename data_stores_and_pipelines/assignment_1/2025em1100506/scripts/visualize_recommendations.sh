#!/bin/bash

# Visualization script for seller recommendations CSV output
# This script runs the visualization script using Python

PYTHON_SCRIPT="visualize_recommendations.py"

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$( cd "$SCRIPT_DIR/.." && pwd )"

# Check if pandas and matplotlib are available locally
if python3 -c "import pandas, matplotlib" 2>/dev/null; then
    echo "Running visualization locally..."
    python3 "$PROJECT_DIR/src/$PYTHON_SCRIPT" \
        --csv-path "$PROJECT_DIR/data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv" \
        "$@"
# Check if running in Docker
elif command -v docker &> /dev/null && docker ps | grep -q spark-master; then
    echo "Running visualization in Docker container..."
    docker exec spark-master python3 /opt/spark/work-dir/src/$PYTHON_SCRIPT \
        --csv-path /opt/spark/work-dir/data/2025em1100506/processed/recommendations_csv/seller_recommend_data.csv \
        "$@"
else
    echo "Error: pandas and matplotlib are not installed."
    echo "Please install them using: pip install pandas matplotlib"
    echo "Or ensure Docker container is running and packages are installed."
    exit 1
fi

