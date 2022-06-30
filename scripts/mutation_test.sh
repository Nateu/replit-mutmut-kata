#!/usr/bin/bash
poetry run mutmut run && \
    poetry run mutmut html

if [ ! -d ./html/mut ]
then
    mkdir ./html/mut 
fi
rm -rf ./html/mut/*
mv ./html/src ./html/index.html ./html/mut/
echo '<!doctype html><html lang=en><head><meta charset=utf-8><title>Reports</title></head><body><ul><li><a href="coverage/">Coverage</a></li><li><a href="mut/">Mutation</a></li></ul></body></html>' > ./html/index.html
