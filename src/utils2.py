# def validate_input(data):
#     test_value = []
#     errors = []
    
#     EXPECTED_FEATURES = ("Alcohol", "Malic acid", "Ash", "Alcalinity of ash",
#                          "Magnesium", "Total phenols", "Flavanoids", "Nonflavanoid phenols",
#                          "Proanthocyanins", "Color intensity", "Hue",
#                          "OD280/OD315 of diluted wines", "Proline")
    
#     if not data:
#         errors.append("Form data must not be empty")
#     else:
#         for feature in EXPECTED_FEATURES:
#             if feature not in data:
#                 errors.append(f"'{feature}' is a required field")
#             else:
#                 try:
#                     test_value.append(float(data[feature]))
#                 except ValueError:
#                     errors.append(f"Invalid value for field {feature}: '{data[feature]}'")

#     return test_value, errors

def final_data(data,data_ng,data_geo):
    # (data,data_ng,data_n,data_rt,data_nlp,data_minimum)

    EXPECTED_FEATURES=['host_is_superhost', 'accommodates',
       'bathrooms', 'bedrooms', 'beds', 'cleaning_fee'
    #    , 'number_of_reviews'
    #    ,
    #    'neighbourhood_group: Ballard', 'neighbourhood_group: Beacon Hill',
    #    'neighbourhood_group: Capitol Hill', 'neighbourhood_group: Cascade',
    #    'neighbourhood_group: Central Area', 'neighbourhood_group: Delridge',
    #    'neighbourhood_group: Downtown', 'neighbourhood_group: Interbay',
    #    'neighbourhood_group: Lake City', 'neighbourhood_group: Magnolia',
    #    'neighbourhood_group: Northgate',
    #    'neighbourhood_group: Other neighborhoods',
    #    'neighbourhood_group: Queen Anne',
    #    'neighbourhood_group: Rainier Valley',
    #    'neighbourhood_group: Seward Park',
    #    'neighbourhood_group: University District',
    #    'neighbourhood_group: West Seattle'
       ]
    test_value = []
    errors =[]
    for feature in EXPECTED_FEATURES:
        test_value.append(float(data[feature]))
    test_value.append(5.0)
    for n in data_ng:
        for n in n:
            test_value.append(float(n))
    for n in data_geo:
        test_value.append(round(n,6))
        # test_value.append(data_n)
        # test_value.append(data_rt)
        # test_value.append(data_nlp)
        # test_value.append(data_minimum)
    return test_value, errors