#!/bin/bash
OUT="templates/build-info.txt"
echo "buildDate=`date`" > $OUT
echo "buildNumber=$BUILD_NUMBER" >> $OUT
echo "gitRevision=`git rev-list --count HEAD`" >> $OUT
cat $OUT
