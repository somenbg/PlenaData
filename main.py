def user_input() -> str:

    '''
        Function to gather input from user with a basic validation check
    '''

    input_text = input("Please enter a word: ")

    while not input_text.isalpha():
        print('ERROR. Please enter alphabets only')
        input_text = user_input()

    return input_text


def word_to_dict(word: str) -> dict:

    '''
        Function to convert input text to dictionary with letter frequency
    '''

    dict_to_return = {}

    for i in word:
        if dict_to_return.get(i.lower()):
            dict_to_return[i.lower()] += i
        else:
            dict_to_return[i.lower()] = i

    return dict_to_return


def generate_output(input_dict: dict) -> str:

    '''
        Function to generate the required output.
    '''

    output_string = ''

    # Append only single instance events
    for i in input_dict.items():
        if len(i[1]) == 1:
            output_string += i[0]

    # Filtering out single instance events and sorting the dictionary
    filtered_dict = {k: v for k, v in sorted(input_dict.items(), key=lambda item: len(item[1]), reverse=True) if len(v) != 1}

    for i in filtered_dict.items():
        output_string += i[1]

    return output_string


if __name__ == '__main__':

    user_text = user_input()
    text_dict = word_to_dict(user_text)
    output_string = generate_output(text_dict)

    print(output_string)