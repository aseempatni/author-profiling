## Instructions to extract features

The first step is to copy `config.py.template` to `config.py`
Then in `config.py`, change the configurations as per your setup and requirements.

Make sure the directory you set as `input_blog_directory` and `output_dump_directory` directory already exist and the `input_blog_directory` directory already contains the downloaded Koppel dataset.
Then set the other configs like `starting_index` and `count`.

**Note:** Setup requires installing the required python packages. If they are not already present on your system, please do install them. We don't have a complete list of packages. (Install whenever you get error :-P)

Most packages can be installed with `pip install [package_name]`. 

Use `python main.py` to run.
