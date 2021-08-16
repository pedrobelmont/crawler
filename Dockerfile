FROM istresearch/scrapy-cluster:crawler-1.3.0-dev
RUN pip install psycopg2
WORKDIR /app
COPY ./pizza /app
CMD ["scrapy", "crawl", "quotes"]

