import os

# telegram bit API key
TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')

# ES config
ES_URL = os.environ.get('ES_URL')

# file path
EXCEL_DOWNLOAD_PATH = os.environ.get('EXCEL_DOWNLOAD_PATH', '../excel/bread.xlsx')
IMAGE_DOWNLOAD_PATH = os.environ.get('IMAGE_DOWNLOAD_PATH', '../images/')
