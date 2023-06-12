import os


def resource_paths(directory, extensions):
    """Create a dictionary of paths to resource files in given directory
    if their extension is in extensions."""
    paths = {}
    for file in os.listdir(directory):
        name, extension = os.path.splitext(file)

        if extension.lower() in extensions:
            paths[name] = os.path.join(directory, file)
    return paths
