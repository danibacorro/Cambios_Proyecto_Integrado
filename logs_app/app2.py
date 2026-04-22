from flask import Flask, render_template, request
import os

app = Flask(__name__)

LOG_BASE = "/logs"


def get_hosts():
    return os.listdir(LOG_BASE)


def get_logs(host):
    path = os.path.join(LOG_BASE, host)
    return os.listdir(path)


def read_log(host, logfile, filter_type=None, search=None):
    path = os.path.join(LOG_BASE, host, logfile)

    if not os.path.exists(path):
        return []

    with open(path, "r", errors="ignore") as f:
        lines = f.readlines()[-200:]  # últimas 200 líneas

    result = []

    for line in lines:
        line_lower = line.lower()

        category = "normal"

        if "error" in line_lower or "failed" in line_lower or "denied" in line_lower:
            category = "error"
        elif "warning" in line_lower:
            category = "warning"
        elif "sshd" in line_lower or "sudo" in line_lower or "login" in line_lower:
            category = "auth"

        # filtro por tipo
        if filter_type and filter_type != "all":
            if category != filter_type:
                continue

        # filtro por búsqueda
        if search:
            if search.lower() not in line_lower:
                continue

        result.append((line.strip(), category))

    return result


@app.route("/", methods=["GET"])
def index():
    hosts = get_hosts()

    selected_host = request.args.get("host")
    selected_log = request.args.get("log")
    filter_type = request.args.get("filter")
    search = request.args.get("search")

    logs = []
    log_files = []

    if selected_host:
        log_files = get_logs(selected_host)

    if selected_host and selected_log:
        logs = read_log(selected_host, selected_log, filter_type, search)

    return render_template("index.html",
                           hosts=hosts,
                           log_files=log_files,
                           logs=logs,
                           selected_host=selected_host,
                           selected_log=selected_log,
                           filter_type=filter_type,
                           search=search)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
