# Use Python 3.12 slim image
FROM python:3.12-slim-bookworm

# Install PDM
RUN pip install pdm

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml pdm.lock* ./

# Install dependencies
RUN pdm install --prod --no-self

# Copy application code
COPY . .

# Expose the application port
EXPOSE 9001

# Run the Litestar application
CMD ["pdm", "run", "litestar", "run", "--host", "0.0.0.0", "--port", "9001"]