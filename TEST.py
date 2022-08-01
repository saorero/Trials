CHUNK_SIZE = 100
file_number = 1
with open('convert.csv') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open('file' + str(file_number)) as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)