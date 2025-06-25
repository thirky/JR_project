#
 # @Date: 2025-06-25 17:24:53
 # @Author: thirky
 # @Description: 
 #
import tomlkit

def load_toml_file(file_path):
    """
    Load a TOML file and return its content as a dictionary.
    
    :param file_path: Path to the TOML file.
    :return: Dictionary containing the TOML data.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        toml_data = tomlkit.load(file)
    return toml_data

def save_toml_file(file_path, data):
    """
    Save a dictionary to a TOML file.
    
    :param file_path: Path to the TOML file.
    :param data: Dictionary containing the data to save.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        tomlkit.dump(data, file)