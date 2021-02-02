import yaml


with open("cal.yaml") as f:
    data=yaml.safe_load(f)["con"]
    print(data["add"])
    print(data["div"])
    print(data["divids"])

    # divids_data=yaml.safe_load(f)["divids"]
    # print(divids_data)
    # div_data = yaml.safe_load(f)["div"]
    # print(div_data)