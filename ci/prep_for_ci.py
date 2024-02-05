import click
import yaml


@click.command()
@click.option("--config")
@click.option("--data")
def main(config: str, data: str):
    """Set the config for lighter-weight training and truncate the dataset."""
    cfg = yaml.safe_load(config)
    cfg["sequence_len"] = 1024
    cfg["val_set_size"] = 32
    cfg["num_epochs"] = 2

    with open(data) as f:
        data_truncated = f.readlines(500)
    with open(data, "w") as f:
        f.writelines(data_truncated)


if __name__ == "__main__":
    main()