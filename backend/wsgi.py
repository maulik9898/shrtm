import os

from app import app

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
