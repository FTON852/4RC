from typing import Dict


def convert_var_to_dict(locals: Dict):
    new = {}

    for key, value in locals.items():
        if key != "self":
            new.update({
                key: value
            })
    return new
