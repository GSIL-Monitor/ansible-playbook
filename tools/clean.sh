#!/bin/bash
#

REPO_HOME=`git rev-parse --show-toplevel`

find $REPO_HOME -name "*.retry" -delete

