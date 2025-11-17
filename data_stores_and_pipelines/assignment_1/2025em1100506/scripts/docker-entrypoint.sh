#!/bin/bash
set -e

# Setup directories for Ivy cache
mkdir -p /opt/spark/.ivy2/cache /opt/spark/.ivy2/jars

# Set environment variables
export IVY_HOME=/opt/spark/.ivy2
export HOME=/opt/spark
export SPARK_HOME=/opt/spark

# Install PyYAML if not already installed
if ! python3 -c "import yaml" 2>/dev/null; then
    echo "Installing PyYAML..."
    pip install --quiet --no-cache-dir PyYAML==6.0.1
fi

# Execute the original command passed to the container
exec "$@"

