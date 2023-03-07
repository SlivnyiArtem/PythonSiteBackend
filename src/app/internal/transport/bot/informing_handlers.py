def dict_ser_to_str_ser(input_dict):
    result_str = ""
    for key, value in input_dict.items():
        result_str += f"{str(key)} : {str(value)}\n"
        # result_str += str(key) + " : " + str(value) + "\n"
    return result_str
