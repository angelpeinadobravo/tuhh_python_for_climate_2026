FROM python:3.11-slim

# Install git and system tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    libgeos-dev \
    libproj-dev \
    proj-bin \
    libhdf5-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# FIX: Explicitly upgrade to modern versions to avoid the traitlets bug
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir jupyterlab notebook jupyter-server

# Only the Python environment lives in the image. start.sh downloads the course into
# ./course on the laptop, so the students' work survives the container.
ARG REQUIREMENTS_URL=https://raw.githubusercontent.com/angelpeinadobravo/tuhh_python_for_climate_2026/main/requirements.txt
ADD $REQUIREMENTS_URL /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# ./course belongs to the student's user, not to the container's user
RUN git config --system --add safe.directory '*'

COPY start.sh /usr/local/bin/start.sh
# a zip edited on Windows may carry CRLF line ends, which break sh
RUN sed -i 's/\r$//' /usr/local/bin/start.sh && chmod +x /usr/local/bin/start.sh

# 8888: JupyterLab, 8000: webpage and slides
EXPOSE 8888 8000

CMD ["start.sh"]
