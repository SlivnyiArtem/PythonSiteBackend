def convert_dict_to_str(input_dict: dict) -> str:
    result_str = ""
    for key, value in input_dict.items():
        result_str += f"{str(key)} : {str(value)}\n"
    return result_str
