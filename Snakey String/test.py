from app import algorithm

def test_algorithm():
    input_array = []
    input_array.append(list("..G....."))
    input_array.append(list(".I.S.U.."))
    input_array.append(list("B...O.T."))
    input_array.append(list(".......H"))

    r = 4
    c = 8

    print(input_array)
    print(algorithm(input_array, r, c))

    expected_output = "BIGSOUTH"
    assert algorithm(input_array, r, c) == expected_output

if __name__ == "__main__":
    test_algorithm()