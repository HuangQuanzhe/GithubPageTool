import click


def build_page(path):
    print("build {}".format(path))


@click.command()
@click.option("-b", "--build", is_flag=True, help="build command")
@click.option("-p", "--path", default="./docs/", help="build path")
def main(build, path):
    if build:
        build_page(path)


if __name__ == "__main__":
    main()