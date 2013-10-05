import re
import os
import subprocess


def render_name():
    if os.path.exists("output/render.txt"):
        return
    f = open("output/render.txt", "wb")
    for i, line in enumerate(open("txts/render.txt")):
        filename = line.split(":")[0]

        render = re.findall("render[( ][\"'](.*?)[\"']", line)
        render_type = "regular"

        if not render:
            render = re.findall("render partial[:] [\"'](.*?)[\"']", line)
            render_type = "partial"
        if not render:
            render = re.findall("render template[:] [\"'](.*?)[\"']", line)
            render_type = "template"
        if render:
            f.write("{0}|{1}|{2}\n".format(filename, render[0], render_type))
    f.close()


def def_name():
    if os.path.exists("output/def.txt"):
        return
    f = open("output/def.txt", "wb")
    for i, line in enumerate(open("txts/def.txt")):
        filename = line.split(":")[0]

        defs = re.findall(r"\bdef (.*)", line)
        if defs:
            defs = defs[0].replace("?", "(")
            defs = defs.split("(")[0]
        cnts = subprocess.check_output('grep -r "{0}" . | wc'.format(defs), shell=True).split()[0]
        f.write("{0}|{1}|{2}\n".format(filename, defs, cnts))
    f.close()


if __name__ == "__main__":
    render_name()
    def_name()
