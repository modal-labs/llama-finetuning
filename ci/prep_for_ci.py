import click
import yaml


@click.command()
@click.option("--config")
@click.option("--data")
def main(config: str, data: str):
    """Set the config for lighter-weight training and truncate the dataset."""
    with open(config) as f:
        cfg = yaml.safe_load(f.read())
    cfg["sequence_len"] = 1024
    cfg["val_set_size"] = 100
    cfg["eval_steps"] = 1000
    cfg["eval_batch_size"] = 10
    cfg["micro_batch_size"] = 10
    cfg["num_epochs"] = 2
    with open(config, "w") as f:
        yaml.dump(cfg, f)

    with open(data) as f:
        data_truncated = f.readlines()[:1000]
    with open(data, "w") as f:
        f.writelines(data_truncated)


if __name__ == "__main__":
    main()
