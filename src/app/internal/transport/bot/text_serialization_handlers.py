def convert_dict_to_str(input_dict: dict) -> str:
    input_dict.pop("error_code")
    result_list = []
    for key, value in input_dict.items():
        result_list.append(f"{str(key)} : {str(value)}\n")
    return ''.join(result_list)