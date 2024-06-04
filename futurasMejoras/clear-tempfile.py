import os
import time

def clean_temp_files(temp_dir, days_old):
    current_time = time.time()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        if os.stat(file_path).st_mtime < current_time - days_old * 86400:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Eliminado {file_path}")

temp_dir = '/path/to/temp'
days_old = 7
clean_temp_files(temp_dir, days_old)
