FROM python:3.12-slim

# Show Python output immediately in docker logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY grade_calc.py .

# ENTRYPOINT makes the container behave like a command;
# anything after the image name in `docker run` is passed as arguments.
ENTRYPOINT ["python", "grade_calc.py"]
