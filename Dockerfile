FROM debian:11-slim AS build

RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip

FROM build AS build-venv
COPY requirements.txt .
RUN /venv/bin/pip install --disable-pip-version-check -r requirements.txt

FROM gcr.io/distroless/python3-debian11@sha256:67871d3bd38d21329a56ea2f3408c3811c2b662ca3e659b95ee157a4ba8adf56
EXPOSE 8080
COPY --from=build-venv /venv /venv
COPY main.py .

ENTRYPOINT ["/venv/bin/python3", "-u", "main.py"]
