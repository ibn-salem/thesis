#!/bin/sh

set -e

[ -z "${GITHUB_PAT}" ] && exit 0
[ "${TRAVIS_BRANCH}" != "master" ] && exit 0

git config --global user.email "j.ibn-salem@uni-mainz.de"
git config --global user.name "Jonas Ibn-Salem (via travis)"

git clone -b gh-pages https://${GITHUB_PAT}@github.com/${TRAVIS_REPO_SLUG}.git book-output
cd book-output
cp -r ../doc/* ./
git add --all *
git commit -m"Update the book" || true
git push -q origin gh-pages
