#!/bin/bash

pylint --rcfile=./.pylintrc --fail-under=7 $(git ls-files '*.py')