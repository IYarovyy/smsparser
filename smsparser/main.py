import toml
import click

from smsparser.DirScaner import DirScaner
from smsparser.FileParser import FileParser


@click.command()
@click.option("-c", "--config", "config_file", default="config.toml", help="Config file name.")
@click.option("-i", "--in", "in_folder", default="in", help="Input folder name.")
@click.option("-o", "--out", "out_folder", default="out", help="Output folder name.")

def cli(config_file, in_folder, out_folder):
    # config = toml.load(config_file)
    # print("===============")
    scaner = DirScaner(in_folder, FileParser(out_folder))
    scaner.run()



if __name__ == "__main__":
    cli()

