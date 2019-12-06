LOG_FORMAT = '%(asctime)s [%(levelname)s] %(funcName)s (%(filename)s:%(lineno)d) %(message)s'
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8080

# To have extended stats, by origin IP, based on the logs.
# https://developers.cloudflare.com/logs/logpull-api/requesting-logs/
LOGS_EXTENDED_METRIC = True
LOGS_EXTENDED_METRIC_COUNT = 10000
LOGS_EXTENDED_METRIC_SAMPLE = 0.01

# Time range in seconds for the logs
# Adjust with you scrape_interval
LOGS_EXTENDED_METRIC_RANGE = 1
