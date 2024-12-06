import toml
import click

from smsparser.DirScaner import DirScaner
from smsparser.FileParser import FileParser

from validator import is_valid


@click.command()
@click.option("-c", "--config", "config_file", default="config.toml", help="Config file name.")
@click.option("-i", "--in", "in_folder", default="in", help="Input folder name.")
@click.option("-o", "--out", "out_folder", default="out", help="Output folder name.")
@click.option("-of", "--out-file", "out_file", default="sms.csv", help="Output file name.")
@click.option("-e", "--err", "err_folder", default="err", help="Error folder name.")
def cli(config_file, in_folder, out_folder, err_folder):
    # config = toml.load(config_file)
    scaner = DirScaner(in_folder, FileParser(out_folder, err_folder, is_valid))
    scaner.run()


if __name__ == "__main__":
    cli()
