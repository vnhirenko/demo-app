FROM gcr.io/distroless/python3-debian11@sha256:67871d3bd38d21329a56ea2f3408c3811c2b662ca3e659b95ee157a4ba8adf56
EXPOSE 8080
COPY main.py .

ENTRYPOINT ["python3", "-u", "main.py"]
