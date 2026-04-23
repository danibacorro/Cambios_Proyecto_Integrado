from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

SSH_TARGET = "dani@172.16.0.200"

def ejecutar_ssh(comando):
    try:
        
        resultado = subprocess.run(
            [
                "ssh",
                "-i", "/home/root/.ssh/id_ed25519",
                "-o", "ControlMaster=auto",
                "-o", "ControlPath=/tmp/ssh_mux_%h_%p_%r",
                "-o", "ControlPersist=60s",
                SSH_TARGET,
                comando
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        if resultado.returncode != 0:
            return [f"Error SSH: {resultado.stderr.strip()}"]

        return resultado.stdout.splitlines()

    except subprocess.TimeoutExpired:
        return ["Error: Timeout en la conexión SSH"]

    except Exception as e:
        return [f"Error: {str(e)}"]


def get_hosts():
    return ejecutar_ssh("list-hosts")


def get_logs(host):
    return ejecutar_ssh(f"list-logs {host}")


def read_log(host, logfile, filter_type=None, search=None):
    lines = ejecutar_ssh(f"read-log {host} {logfile}")
    lines.reverse()
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

    return render_template(
        "index.html",
        hosts=hosts,
        log_files=log_files,
        logs=logs,
        selected_host=selected_host,
        selected_log=selected_log,
        filter_type=filter_type,
        search=search
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
