#!/bin/sh

git pull origin source
git add .
git commit -m "Update site"
git push origin source
