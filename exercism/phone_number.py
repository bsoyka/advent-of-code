from re import sub


class PhoneNumber(object):
    def __init__(self, phone_number: str):
        self.number = sub(
            r'[^0-9]', '', phone_number
        )  # Remove all non-numerical characters

        if len(self.number) != 10:
            if len(self.number) != 11:
                raise ValueError('Phone number must contain 10 or 11 digits')

            # Number is 11 digits, check if the first digit is 1
            if self.number[0] == '1':
                self.number = self.number[1:]  # Remove the 1
            else:
                raise ValueError(
                    'First digit in phone number must be 1 if phone number contains 11 digits'
                )

        # Check area code
        if self.number[0] in ('0', '1'):
            raise ValueError('Area code cannot begin with 0 or 1')

        # Check exchange code
        if self.number[3] in ('0', '1'):
            raise ValueError('Exchange code cannot begin with 0 or 1')

    @property
    def area_code(self) -> str:
        return self.number[:3]  # Return the first 3 digits

    def pretty(self) -> str:
        return sub(
            r'^(\d{3})(\d{3})(\d{4})$', r'(\1)-\2-\3', self.number
        )  # Format the number
