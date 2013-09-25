import re


def render_name():
    f = open("output/render.txt", "wb")
    for i, line in enumerate(open("txts/render.txt")):
        filename = line.split()[0]

        render = re.findall("render[( ][\"'](.*)[\"'][) ]", line)
        render_type = "regular"

        if not render:
            render = re.findall("render partial[:] [\"'](.*)[\"']", line)
            render_type = "partial"
        if not render:
            render = re.findall("render template[:] [\"'](.*)[\"']", line)
            render_type = "template"
        if render:
            f.write("{0}|{1}|{2}\n".format(filename, render[0], render_type))
    f.close()


def def_name():
    for i, line in enumerate(open("txts/def.txt")):
        print i, line

if __name__ == "__main__":
    render_name()
