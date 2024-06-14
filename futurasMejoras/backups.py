import os
import shutil
from datetime import datetime

def backup_files(source_dirs, backup_dir):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    for source in source_dirs:
        dest = os.path.join(backup_dir, f"{os.path.basename(source)}_{timestamp}")
        shutil.copytree(source, dest)
        print(f"Backup de {source} realizado en {dest}")

source_dirs = ['/home/automation/workspace', '/home/automation/aulatic']
backup_dir = '/home/automation/backups'
backup_files(source_dirs, backup_dir)