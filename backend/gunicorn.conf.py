# import multiprocessing
import os

pidfile = 'flask_app.pid'
workers = 2
# workers = multiprocessing.cpu_count() * 2 + 1
port = int(os.environ.get("PORT", 8080))
bind = '0.0.0.0:'+str(port)

# user = 'ubuntu'
# group = 'ubuntu'
