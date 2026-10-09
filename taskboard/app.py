import socket
from flask import Flask, jsonify, redirect, render_template_string, request, url_for

app = Flask(__name__)

tasks = []      # in-memory task list
counter = {"next_id": 1}

PAGE = """
<!doctype html>
<html>
<head>
  <title>Docker Task Board</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 640px; margin: 40px auto; padding: 0 16px; }
    li { margin: 10px 0; }
    .done { text-decoration: line-through; color: #888; }
    form.inline { display: inline; }
  </style>
</head>
<body>
  <h1>Docker Task Board</h1>
  <form method="post" action="/add">
    <input name="title" placeholder="New task" required>
    <button type="submit">Add</button>
  </form>
  <ul>
  {% for t in tasks %}
    <li class="{{ 'done' if t.done else '' }}">
      {{ t.title }}
      {% if not t.done %}
      <form class="inline" method="post" action="/done/{{ t.id }}"><button>Done</button></form>
      {% endif %}
      <form class="inline" method="post" action="/delete/{{ t.id }}"><button>Delete</button></form>
    </li>
  {% else %}
    <li>No tasks yet. Add one above.</li>
  {% endfor %}
  </ul>
  <p><small>Served by container: {{ host }}</small></p>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(PAGE, tasks=tasks, host=socket.gethostname())


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": counter["next_id"], "title": title, "done": False})
        counter["next_id"] += 1
    return redirect(url_for("index"))


@app.route("/done/<int:task_id>", methods=["POST"])
def done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    tasks[:] = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/api/tasks")
def api_tasks():
    return jsonify(tasks)


@app.route("/health")
def health():
    return jsonify(status="ok", host=socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
