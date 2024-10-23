import argparse
import numpy as np

class ArgparseInputs:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("Path", help="Path to data folder")
        parser.add_argument("basename", help="Base name of SILO files")
        parser.add_argument("img_dir", help="Path to image directory")
        parser.add_argument("-q", "--fluidquantity", help="Desired fluid quantity to plot", default="Density")
        parser.add_argument("-s", "--surface", help ="3D Plot surface - XY, XZ, YZ", default="XY")
        parser.add_argument("-l", "--log", help="Logarithmic plot", default=True)
        parser.add_argument('--lim', nargs='+', type=float, default=[-19, -11])
        parser.add_argument('--cmap', default='plasma')
        parser.add_argument("-mm", "--make_movie", help="Make movie from images", action="store_true")
        args = parser.parse_args()

        self.path = args.Path
        self.basename = args.basename
        self.fluidquantity = args.fluidquantity
        self.surface = args.surface
        self.limits = args.lim
        self.cmap = args.cmap
        self.make_movie = args.make_movie
        self.img_dir = args.img_dir
        self.log = args.log
