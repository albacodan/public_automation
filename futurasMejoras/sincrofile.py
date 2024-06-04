import os
import filecmp
import shutil

def sync_directories(source_dir, target_dir):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)
        if os.path.isdir(source_item):
            if not os.path.exists(target_item):
                shutil.copytree(source_item, target_item)
            else:
                sync_directories(source_item, target_item)
        else:
            if not os.path.exists(target_item) or not filecmp.cmp(source_item, target_item):
                shutil.copy2(source_item, target_item)

source_dir = '/path/to/source'
target_dir = '/path/to/target'
sync_directories(source_dir, target_dir)
