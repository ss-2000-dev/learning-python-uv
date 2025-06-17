FROM python:3.12-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        libmariadb-dev \
        pkg-config \
        curl \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Working directory
WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./

# Install project dependencies using uv
# This will create and populate the .venv directory
RUN uv sync

# copy application code
COPY . .

EXPOSE 8080

CMD ["uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8080"]