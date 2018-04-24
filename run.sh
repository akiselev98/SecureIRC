gunicorn --worker-class eventlet --certfile ${FLASK_CERT_LOCATION} --keyfile ${FLASK_KEY} -b localhost:${FLASK_PORT} -w 1 secureirc:app
