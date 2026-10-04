import os
import socket
from flask import Flask, render_template

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "1.0")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/db")
def db():
	import psycopg2
	try:
		conn = psycopg2.connect(
			host=os.environ.get("DB_HOST", "db"),
			dbname=os.environ.get("POSTGRES_DB", "ip-calc"),
			user=os.environ.get("POSTGRES_USER", "ip-calc"),
			password=os.environ.get("POSTGRES_PASSWORD", "ip-calc"),
			connect_timeout=3,
		)
		conn.close()
		return "Databasetilkobling OK"
	except Exception as e:
		return f"Databasefeil: {e}", 500
@app.route("/health")
def health():
	# Kubernetes bruker denne i probene i Samling 2
	return "ok", 200
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
