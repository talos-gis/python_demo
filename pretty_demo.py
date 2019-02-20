from io import StringIO
import sys
import glob
import os.path
import traceback

globs = [
    'demo_core/*.py',
    'demo_numpy/*.py',
    'demo_pandas/*.py',
    'demo_scipy/*.py'
]


def make_nice_print(dst):
    def nice_print(*args, **kwargs):
        if 'file' in kwargs:
            print(*args, **kwargs)
            return
        kwargs.setdefault('end', '')
        buffer = StringIO()
        print(*args, **kwargs, file=buffer)
        to_print = buffer.getvalue()
        del buffer
        if '\n' in to_print:
            to_print = '"""\n' + to_print + '\n"""'
        else:
            to_print = '"' + to_print.replace('"', r'\"') + '"'
        # to_print = textwrap.indent(to_print, prefix='# >>> ')
        print(to_print, end='\n', file=dst, flush=__debug__)

    return nice_print


def make_nice_help(nice_print):
    def nice_help(*args, **kwargs):
        buffer = StringIO()
        sys.stdout = buffer
        help(*args, **kwargs)
        sys.stdout = sys.__stdout__
        nice_print(buffer.getvalue())

    return nice_help


def make_nice_input(nice_print):
    def nice_input(prompt=''):
        to_print = prompt
        result = input(f'input(prompt={prompt}): ')
        to_print += result
        nice_print(to_print)
        return result

    return nice_input


def main(src, dst=None):
    def do_scope():
        nonlocal scope
        print(scope, end='', file=dst, flush=__debug__)
        try:
            exec(scope, namespace)
        except Exception as e:
            result = input(f'exception {e!r} ok?')
            if result == 'y':
                nice_print('exception:\n'+traceback.format_exc())
            else:
                raise
        scope = ''

    def get_indent(line: str):
        i = 0
        while len(line) > i and line[i].isspace():
            i += 1
        return line[:i]

    nice_print = make_nice_print(dst)
    nice_help = make_nice_help(nice_print)
    nice_input = make_nice_input(nice_print)
    namespace = {'print': nice_print, 'help': nice_help, 'input': nice_input}
    scope = ''
    prev_indent = ''
    for line in src:
        if ((line == '\n' or line.lstrip()[0] != '#') and not prev_indent)\
                or not (line[0].isspace() or line.startswith('elif') or line.startswith('else')):
            try:
                compile(scope, filename='<string>', mode='exec')
            except SyntaxError:
                pass
            else:
                do_scope()
        scope += line
        prev_indent = get_indent(line)
    do_scope()


def recommend(src_path, dst_path):
    if os.path.isfile(dst_path):
        return 'n'
    with open(src_path) as r:
        for line in r:
            if 'print(' in line:
                return 'y'
        return 'n'


if __name__ == '__main__':
    wd = os.getcwd()
    for g in globs:
        for filename in glob.iglob(g):
            dst_path = os.path.join('prettified', filename)
            rec = recommend(filename, dst_path)
            if rec == 'n':
                continue
            response = input(f'do {filename} (default {rec})?').lower()
            if response == '':
                response = rec
            if response in ('y', 'yes'):
                src_dir_name = os.path.dirname(filename)


                dst_dir_name = os.path.dirname(dst_path)
                os.makedirs(dst_dir_name, exist_ok=True)
                with open(filename) as src:
                    with open(dst_path, 'w') as dst:
                        os.chdir(src_dir_name)
                        main(src, dst)
                        os.chdir(wd)
