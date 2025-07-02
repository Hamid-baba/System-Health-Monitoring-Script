def log_metrics(metrics):
    with open("system_log.txt", "a") as f:
        f.write(metrics + "\n")

log_metrics("System check complete.")
