from cfg import shared as cfg


def is_pipeline_row(row: dict):
    return all([row[specname] for specname in cfg.core_specs])

