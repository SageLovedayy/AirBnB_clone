#!/usr/bin/bash
find . -type f -name "*.py" -exec pycodestyle {} +
