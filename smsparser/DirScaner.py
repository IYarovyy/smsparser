import os
from .console import out
from os.path import join


class DirScaner:
    def __init__(self, in_folder, fileParser):
        self.in_folder = in_folder
        self.fileParser = fileParser

    def run(self):
        with out.status("[bold green]Working..."):
            for root, dirs, files in os.walk(self.in_folder):
                for file in files:
                    if not file.startswith(".") and not file.startswith("~"):
                        self.fileParser.parse(join(root, file))
                        out.print("[green]:heavy_check_mark: {}[/green]".format(file))
