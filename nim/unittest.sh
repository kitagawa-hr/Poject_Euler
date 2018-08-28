#! /usr/bin/env sh
TEST_DIR=`dirname $0`/unittest
cd ${TEST_DIR}
nimble unittest 

exit 0
