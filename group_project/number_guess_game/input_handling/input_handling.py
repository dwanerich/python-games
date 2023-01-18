def input_handling(type_of_input, input_string, range = None):
    while(True):
        try:
            captured_input = type_of_input(input(input_string))
        except ValueError:
            print(f"You didn't input a valid {type_of_input}")
        else:
            if range:
                if captured_input >= range[0] and captured_input <= range[1]: pass
                else: continue
            break
    return captured_input