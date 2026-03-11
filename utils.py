import os

def create_output_folder():

    if not os.path.exists("output"):
        os.makedirs("output")


def get_output_name(input_file):

    filename = os.path.basename(input_file)

    name, _ = os.path.splitext(filename)

    return f"output/{name}.mp3"