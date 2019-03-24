import sys

sys.path.append("../")
from pycore.tikzeng import *

max_depth = 80

# defined your arch
arch = [
    to_head(".."),
    to_cor(),
    to_begin(),
    to_Conv(
        "layer1",
        r"$\sim$10e6",
        3,
        offset="(0,0,0)",
        to="(1,0,0)",
        height=1,
        depth=max_depth,
        width=3,
        caption="Raw Data",
    ),
    to_Conv(
        "layer2",
        140,
        3,
        offset="(1,0,0)",
        to="(2,0,0)",
        height=3,
        depth=max_depth * 0.4,
        width=3,
        caption="Intracycle\\\\Augmented\\\\Linear\\\\Fit",
    ),
    to_connection("layer1", "layer2"),
    to_Conv(
        "layer3",
        28,
        3,
        offset="(2,0,0)",
        to="(3,0,0)",
        height=3,
        depth=max_depth * 0.1,
        width=3,
        caption="Typewise\\\\Intercycle\\\\Polynomial\\\\Fit",
    ),
    to_connection("layer2", "layer3"),
    to_ConvBlue(
        "layer4",
        252,
        1,
        offset="(4.25,0,0)",
        to="(5.25,0,0)",
        height=1,
        depth=max_depth * 0.65,
        width=1,
        caption="Flattened\\\\Input",
    ),
    to_connection("layer3", "layer4"),
    to_ConvBlue(
        "layer5",
        4032,
        1,
        offset="(5.5,0,0)",
        to="(6.5,0,0)",
        height=1,
        depth=max_depth * 0.9,
        width=1,
        caption="Hidden Layer",
    ),
    to_connection("layer4", "layer5"),
    to_ConvBlue(
        "output",
        1,
        1,
        offset="(6.5,0,0)",
        to="(7.5,0,0)",
        height=1,
        depth=1,
        width=1,
        caption="Regressed Output",
    ),
    to_connection("layer5", "output"),
    to_end(),
]


def main():
    namefile = str(sys.argv[0]).split(".")[0]
    to_generate(arch, namefile + ".tex")


if __name__ == "__main__":
    main()
