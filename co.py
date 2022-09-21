import time
import logging
import pathlib
import os
import argparse
import concurrent.futures

read_dir = "test_read_dir/"
write_dir = "test_write_dir/"
write_file_path = []

def copy_file(source_path, dest_path):
    with open(source_path, "rb") as src:
        with open(dest_path, "wb") as dest:
            for line in src:
                dest.write(line)

def run_sample():
    # reset some variables before doing it linearly
    write_file_path = []
    with concurrent.futures.ThreadPoolExecutor(args.threads) as pool:
        for root, dirs, files in os.walk(write_dir):
            for name in files:
                file = pathlib.Path(os.path.join(root, name))
                if file.is_file():
                    write_file_path.append(file.resolve())

        # get full path to read dir + all files inside read_dir/
        for root, dirs, files in os.walk(read_dir):
            for idx, name in enumerate(files):
                file = pathlib.Path(os.path.join(root, name))
                if file.is_file():
                    #copy the file from source to destination byte-by-byte
                    copy_file(source_path=file.resolve(), dest_path=write_file_path[idx])

def run_concurrent_sample():
    with concurrent.futures.ThreadPoolExecutor(args.threads) as pool:
        # get full path to write dir/write_files
        for root, dirs, files in os.walk(write_dir):
            for name in files:
                file = pathlib.Path(os.path.join(root, name))
                if file.is_file():
                    write_file_path.append(file.resolve())

        # get full path to read dir + all files inside read_dir/
        for root, dirs, files in os.walk(read_dir):
            for idx, name in enumerate(files):
                file = pathlib.Path(os.path.join(root, name))
                if file.is_file():
                    #copy the file from source to destination byte-by-byte
                    pool.submit(copy_file, file.resolve(), write_file_path[idx])

parser =  argparse.ArgumentParser()
parser.add_argument("-t", "--threads", type=int, default=10, help="Number of threads to use.")
args = parser.parse_args()

if __name__ == '__main__':
    start_time = time.time()
    run_concurrent_sample()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time to execute script concurrently: {total_time}")
    start_time = time.time()
    run_sample()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Time to execute linear script: {total_time}")
