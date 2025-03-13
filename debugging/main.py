def ask_user_for_phone_number() -> str:
    phone_number = input("What is the phone number to validate? ")
    valid_numbers = ""
    for letter in phone_number:
        if letter.isnumeric() or letter == "+":
            valid_numbers += letter
    return valid_numbers

# Not truthy: "", [], None

def format_uk_number():
    phone_number = ask_user_for_phone_number()
    formatted_number = convert_phone_to_UK_Format(phone_number)
    if formatted_number:
        print(" ".join(formatted_number))
    else:
        raise ValueError(f"{phone_number} is not a valid UK number. Please try again.")


def is_number_valid_length(phoneNo: str) -> bool:
    return len(phoneNo) == 11


def is_UK_number(phone_no: str) -> bool:
    return phone_no.startswith("07")


def has_country_code(phone_no: str) -> bool:
    return "+44" in phone_no


def convert_phone_to_UK_Format(input: str) -> list:
    if has_country_code(input):
        input = input.replace("+44", "07")

    if is_number_valid_length(input) and is_UK_number(input):
        return convert_string_to_phone_format(input)


def convert_string_to_phone_format(phone_str: str) -> list:
    phoneA = phone_str[:5]
    phoneB = phone_str[5:]
    return [phoneA, phoneB]


def print_invalid_input_error():
    print()


if __name__ == "__main__":
    format_uk_number()
