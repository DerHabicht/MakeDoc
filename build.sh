#!/bin/bash
cd `dirname $0`
source .makedoc
make $1
source after.sh
