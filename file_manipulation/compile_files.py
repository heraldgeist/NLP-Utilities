import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Compile files from directory into one',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--data_path', type=str, help='Path to files directory')
parser.add_argument('--out_path', type=str, help='Path and name of output file')
args = parser.parse_args()

def compile():
    data_path = args.data_path
    out_path = args.out_path
    files = os.listdir(data_path)
    with open(out_path, 'wb') as outfile:
        for filename in files:
            if filename == out_path:
                continue
            with open(data_path+'/'+filename, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)

if __name__ == '__main__':
    compile()
