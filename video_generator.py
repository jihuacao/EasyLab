# coding=utf-8
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_img', dest='InputImg', type=str, default='', action='store', help='')
    parser.add_argument('--input_text', dest='InputText', type=str, default='', action='store', help='')
    parser.add_argument('--input_video', dest='InputVideo', type=str, default='', action='store', help='')
    options = parser.parse_args()