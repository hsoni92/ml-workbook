#!/bin/bash
set -e

# Setup directories for Ivy cache
mkdir -p /opt/spark/.ivy2/cache /opt/spark/.ivy2/jars

# Set environment variables
export IVY_HOME=/opt/spark/.ivy2
export HOME=/opt/spark
export SPARK_HOME=/opt/spark

# Install PyYAML if not already installed
# Check both python3 and python, and install for the system Python
if ! python3 -c "import yaml" 2>/dev/null; then
    echo "Installing PyYAML..."
    python3 -m pip install --quiet --no-cache-dir PyYAML==6.0.1 || \
    pip3 install --quiet --no-cache-dir PyYAML==6.0.1 || \
    pip install --quiet --no-cache-dir PyYAML==6.0.1
fi

# Also ensure it's available for any Python that might be used
python3 -m pip install --quiet --no-cache-dir --user PyYAML==6.0.1 2>/dev/null || true

# Execute the original command passed to the container
exec "$@"

