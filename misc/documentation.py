# coding: utf-8
import inspect
import grfc.game.remote_handler as rh


def fetch_documentation(code):
    documentation = []
    comments = False
    for line in code:
        if _function_signature(line):
            documentation.append(line)
        elif _start_comment(line) and not _end_comment(line):
            comments = True
        if comments:
            documentation.append(line)
        if _end_comment(line):
            comments = False

    return documentation


def _function_signature(line):
    return line.startswith('def')


def _start_comment(line):
    return line.find('"""') > 0


def _end_comment(line):
    return line[-3:] == '"""'


if __name__ == '__main__':
    from pprint import pprint as pp
    pp(fetch_documentation(inspect.getsource(rh).split('\n')), width=80)
