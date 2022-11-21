https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from polynomial import Polynomial

def create(string):
    p = Polynomial()
    for word in string.split():
        nums = word.split('x')
        p.add_term(float(nums[0]), int(nums[1]))
    return p

print('Example 1')
print('-'*10)
poly1 = create("1x3 1x0")
poly2 = create("-1x2")
poly = poly1.add(poly2)
print(poly)
print(poly.evaluate(1.5))


print('\nExample 2')
print('-'*10)
poly = create("-4x3 3x2 25x1 6x0")
poly.plot(-3.0, 3.0, 100, 'myplot.png')
print('open the file myplot.png to see the plot')


print('\nExample 3')
print('-'*10)
poly = create("-4x3 3x2 25x1 6x0")
print('Closed-form integral:', poly.integrate(-2.0, 2.0))

print('\nExample 4')
print('-'*10)
poly = create("-4x3 3x2 25x1 6x0")
print('Approximate integral:', poly.trapz_integrate(-2.0, 2.0, 50))

