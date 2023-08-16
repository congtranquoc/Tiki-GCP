import subprocess
import datetime
import os

# this script is demo, since it should be changed when it need to run
mongodb_uri = "mongodb://<username>:<password>@<hostname>:<port>/<database>"
backup_folder = "/tmp"
gcs_bucket = "gs://tiki-bucke"

def main():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_path = os.path.join(backup_folder, f"backup_{timestamp}")

    # mongodump
    command = [
        "mongodump",
        "--uri", mongodb_uri,
        "--out", backup_path
    ]
    subprocess.run(command, check=True)

    #gsutil
    gsutil_command = f"gsutil -m cp -r {backup_path} {gcs_bucket}"
    subprocess.run(gsutil_command, shell=True, check=True)

if __name__ == "__main__":
    main()
