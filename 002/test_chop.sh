#!/bin/bash
CHOP=$1

if [ -z "$CHOP" ]; then echo "No executable specified."; exit 1; fi
if [ ! -f "$CHOP" ]; then echo "Can't find $CHOP."; exit 2; fi
CHOP=`find . -name $CHOP`

echo
echo "##### Testing: $CHOP"

function run_test() {
    TEST=$1
    PASS=$2
    echo "Testing: \"$TEST\""
    RESULT=`exec $TEST`
    if [[ "$RESULT" != "$PASS" ]]
    then
        echo "FAILED!"
        echo "Expected: $PASS Got: $RESULT"
        exit 1
    fi
}

run_test "$CHOP 3" "-1"
run_test "$CHOP 3 1" "-1"
run_test "$CHOP 1 1" "0"

run_test "$CHOP 1 1 3 5" "0"
run_test "$CHOP 3 1 3 5" "1"
run_test "$CHOP 5 1 3 5" "2"
run_test "$CHOP 0 1 3 5" "-1"
run_test "$CHOP 2 1 3 5" "-1"
run_test "$CHOP 4 1 3 5" "-1"
run_test "$CHOP 6 1 3 5" "-1"

run_test "$CHOP 1 1 3 5 7" "0"
run_test "$CHOP 3 1 3 5 7" "1"
run_test "$CHOP 5 1 3 5 7" "2"
run_test "$CHOP 7 1 3 5 7" "3"
run_test "$CHOP 0 1 3 5 7" "-1"
run_test "$CHOP 2 1 3 5 7" "-1"
run_test "$CHOP 4 1 3 5 7" "-1"
run_test "$CHOP 6 1 3 5 7" "-1"
run_test "$CHOP 8 1 3 5 7" "-1"

echo "##### $CHOP PASSED"
echo
exit 0
