#!/bin/sh
# Downloads the course into /course (./course on the laptop) on the first start and updates it on
# later starts, gives the student the lessons they do not have yet, then serves the webpage
# (port 8000) and JupyterLab (port 8888).
set -e
cd /course

if [ ! -d .git ]; then
    echo "Downloading the course into ./course ..."
    # clone next to /course and copy, since /course is not empty (it holds a README)
    git clone -q "$REPO_URL" /tmp/course
    cp -a /tmp/course/. /course/
    rm -rf /tmp/course
elif ! git pull -q --ff-only; then
    # git refuses to overwrite changed files, so nothing is lost
    echo "WARNING: the course was not updated (no internet, or a file in ./course was changed)."
    echo "         Your notebooks and pages are untouched. Deleting ./course downloads it again."
fi

# the lessons the student does not have yet; their own notebooks are never overwritten
mkdir -p /app/notebooks/lessons
cp -rn /course/examples/. /app/notebooks/lessons/

# rebuilds the webpage every time a page, a slide or a figure is saved; docs/source/conf.py
# copies the student's pages (/app/pages, see STUDENT_PAGES) into the sources as my_pages/
sphinx-autobuild /course/docs/source /course/docs/build/html --host 0.0.0.0 --port 8000 \
    --watch /app/pages --watch /course/slides --watch /course/examples/Fig \
    --ignore "*/docs/source/my_pages/*" -q &

cd /app
echo "JupyterLab: http://localhost:8888   Webpage and slides: http://localhost:8000"
exec jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
