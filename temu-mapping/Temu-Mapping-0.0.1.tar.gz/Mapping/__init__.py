class Mapping:
    def __init__(self,p_no):
        self.phone = p_no

    def character(self):
        digit_mapping = {
            "0" : "zero",
            "1" : "one",
            "2" : "two",
            "3" : "three",
            "4" : "four",
            "5" : "five",
            "6" : "six",
            "7" : "seven",
            "8" : "eight",
            "9" : "nine"
        }
        output = " "
        for ch in self.phone:
            output += digit_mapping.get(ch) + " "
        return(output)
