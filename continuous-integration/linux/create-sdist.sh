#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ROOT_DIR=$(realpath "$SCRIPT_DIR/../..")

# Install minimal requirements to create the source distributions
pip install --requirement "$SCRIPT_DIR/../python-requirements/dist.txt" || exit $?

# Create source distribution
(cd $ROOT_DIR && python setup.py sdist) || exit $?

echo Success! [$0]