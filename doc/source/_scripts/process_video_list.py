#! /usr/bin/env python3
import os

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, "..", "..", "build", "book", "videos.csv"),
          "r") as videos:
    with open(os.path.join(dirname, "..", "videos.csv"), "w") as out:

        for video in videos:
            video = video.split("Video: ")
            video[1] = video[1][0].upper() + video[1][1:]
            out.write("".join(video))
