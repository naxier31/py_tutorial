import pathlib

root_dir = pathlib.Path().absolute()
data_dir = root_dir / "data"

for iter in data_dir.iterdir():
    if iter.is_file and iter.name.startswith("《"):
        new_name = iter.name.replace("《", "").replace("》", "")
        iter.rename(root_dir / new_name)
