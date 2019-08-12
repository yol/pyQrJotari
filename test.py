#! /usr/bin/env python

import yaml
from csv_interface import build_interface
import pyQRjotari

if __name__ == "__main__":
    confpath = "configuration.yaml"
    conffile = open(confpath)
    config = yaml.load(conffile)

    klein, groot = build_interface()

    schedules = {'klein':klein, "groot":groot}

    def update(*args):
        print args

    assert pyQRjotari.JotariQrBackend(schedules, update, '2019-10-20 09:35').lookup('klein1') == 'Opening'