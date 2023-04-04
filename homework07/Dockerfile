# Daniela Sanchez, dls4848
# Dockerfile for homework07

FROM python:3.8.10

RUN pip install Flask==2.2.2 redis requests
RUN pip install requests==2.2.0


COPY gene_api.py /gene_api.py

CMD ["python3", "gene_api.py"]
