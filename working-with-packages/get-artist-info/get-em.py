#!/usr/bin/env python -tt

import musicbrainzngs
import time
import sys

musicbrainzngs.set_useragent("getting-info", 1)

def sprint(message):
    sys.stderr.write("{}\n".format(message))


whole = open("./artist-info.csv", "r").read()

pieces = whole.split("\n")

THELEN = len(pieces)


with open("output.txt", "w") as fh:
    for ind, piece in enumerate(pieces):
        sprint("On {} of {}\t\t{}%".format(ind, piece, (round(ind/THELEN*100, 2))))
        sprint("MBID: {}".format(piece))
        try:
            result = musicbrainzngs.get_artist_by_id(piece)
            # code = result["artist"]["area"]["iso-3166-1-code-list"]
            areaname = result["artist"]["area"]["name"]
            countryname = result["artist"]["country"]
            thename = result["artist"]["name"]
            outstr = '"{}"\t"{}"\t"{}"\t"{}"'.format(piece, thename, countryname, areaname)
            print(outstr)
            fh.write(outstr)
            fh.write("\n")
            fh.flush()
        except:
            pass
        sprint("")
        time.sleep(1)
