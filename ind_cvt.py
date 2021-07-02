"""
Transform the current indentation into something else.
With this script, you can change one kind of indentation to another type.
"""
import argparse
import regex as re
from config import config


def main():
    # Define 4 arguments here:
    # file: <str> the path to the file to format.
    # prev: <str> the previous indentation to be converted.
    # target: <str> the target indentation to convert to.
    # appendix: <str> what to append to the converted file.
    parser = argparse.ArgumentParser(description="arguments for converting indentations")
    parser.add_argument("-f", "--file",
                        type=str, help="path to the file")
    parser.add_argument("-p", "--prev",
                        type=str, default=config['default_prev_indent'],
                        help="the previous indentation to be converted")
    parser.add_argument("-t", "--target",
                        type=str, default=config['default_target_indent'],
                        help="the target indentation to convert to")
    parser.add_argument("-a", "--appendix",
                        type=str, default=config['appendix'],
                        help="what to append to the converted file")
    args = parser.parse_args()
    file_path = args.file
    prev_ind = args.prev
    target_ind = args.target

    # escape the raw input of tabs (\t)
    prev_ind = prev_ind.replace('\\t', '\t')

    dot_idx = file_path.rfind('.')
    if dot_idx == -1:
        # in case there's no extensions :)
        print("Please include the file name extension in your file path.")
        exit(-1)
    else:
        # read the file to in_f.
        in_f = open(file_path, 'r', encoding='utf-8')
        # define the output file.
        out_fp = file_path[:dot_idx]+config['appendix']+file_path[dot_idx:]
        out_f = open(out_fp, 'w', encoding='utf-8')

        if config['method'] == 'search':
            # method 1: search by line for prev_ind and substitude them.
            search_sub(in_f, out_f, prev_ind, target_ind)
        else:
            # method 2: match prev_ind by regular expression and substitude.
            re_sub(in_f, out_f, prev_ind, target_ind)

        out_f.close()
        in_f.close()


def search_sub(in_f, out_f, prev_ind, target_ind):
    """
    Line by line, searching from the start for the matched indentations and
    then replace them.
    """
    while True:
        line = in_f.readline()
        if line == '':
            break
        cnt = 0
        print(line[cnt*len(prev_ind):(cnt+1)*len(prev_ind)])
        print(prev_ind)
        try:
            while line[cnt*len(prev_ind):(cnt+1)*len(prev_ind)] == prev_ind:
                cnt += 1
        except IndexError:
            pass
        out_f.write(cnt*target_ind + line[cnt*len(prev_ind):])


def re_sub(in_f, out_f, prev_ind, target_ind):
    """
    Substitude those indentations with the help of regular expression!
    """
    text = in_f.read()
    pattern = re.compile(
        '^%s|((?<=^%s+)%s)' % (prev_ind, prev_ind, prev_ind),
        flags=re.M
    )
    cvt_text = re.sub(pattern, target_ind, text)
    out_f.write(cvt_text)


if __name__ == '__main__':
    main()
