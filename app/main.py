from typing import Optional

import rich_click as click



@click.command()
@click.argument("name")
@click.option("--city")
def main(name: str, city: Optional[str] = None):
    print(f"Hello {name}")
    if city:
        print(f"Let's have a coffee in {city}")


if __name__ == "__main__":
    main()
