
def square(input_data):
    result = []
    for num in input_data:
        res = num*num
        result.append(res)
    return result

input_data = [1,2,3,4,5,6]

result = square(input_data)
print ('result: ', result)

#result:  [1, 4, 9, 16, 25, 36]


def square_generator(input_data):
    for num in input_data:
        res = num*num
        yield res

input_data = [1,2,3,4,5,6]

square_gen = square_generator(input_data)
print(square_gen)

square_num = next(square_gen)
print ('result: ',square_num)

square_gen = square_generator(input_data)
for i in range(len(input_data)):
    square_num = next(square_gen)
    print ('result: ',square_num)
