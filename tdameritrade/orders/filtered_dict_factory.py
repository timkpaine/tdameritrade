def filtered_dict_factory(list_of_tuples):
    filtered_dict = {key: value for key, value in list_of_tuples if value is not None}
    return dict(filtered_dict)
