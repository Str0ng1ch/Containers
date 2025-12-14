import psycopg2
from flask import Flask
import os
import argparse

app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output-dir', type=str)


def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ['POSTGRES_HOST'],
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn


@app.route('/')
def hello():
    return "Hello from Docker!"


@app.route('/data')
def data():
    # Чтение данных из volume
    data_path = '/app/data/example.txt'
    if os.path.exists(data_path):
        with open(data_path, 'r') as f:
            content = f.read()
        return f"Data from volume: {content}"
    return "No data file found. Create one in /app/data/"


@app.route('/database')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return f'Users in DB: {users}'


@app.route('/health')
def health():
    return 'OK', 200


if __name__ == '__main__':
    args = parser.parse_args()

    # Проверка монтирования
    with open(f"{args.output_dir}/output.txt", "w") as f:
        f.write("Application was started.")

    app.run(host='0.0.0.0', port=5000)
