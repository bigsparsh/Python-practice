import zipfile
import pathlib
import time


def compress(source_add, dest_add):
    dest_path = pathlib.Path(dest_add, f'{time.strftime("%H%w_%S%M")}.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filename in source_add:
            source_path = pathlib.Path(filename)
            archive.write(source_path, arcname=source_path.name)