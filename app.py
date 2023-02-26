from flask import Flask, render_template
import random
import concurrent.futures
app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route("/summary", methods=["GET"])
def get_summary():
    # return "1\n2\n3"
    with open("files/summary.txt", "a", encoding="utf-8") as f:
         f.write(f"Line {random.randint(1, 100)}\n")
    with open("files/summary.txt", "r", encoding="utf-8") as f:
        return f.readlines()

if __name__ == '__main__':
   concurrent.futures.ThreadPoolExecutor().submit(app.run)