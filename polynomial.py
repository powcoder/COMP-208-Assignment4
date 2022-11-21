https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

class Polynomial:
    def __init__(self):
        self.power2coeff = {}
    
    def add_term(self, coeff, power):
        self.power2coeff[power] = coeff

    def __str__(self):      
        result = ''
        for power, coeff in self.power2coeff.items():
            result += '{:.2f}x{} '.format(coeff, power)
        return result

    # Add new methods below as required by Q2

