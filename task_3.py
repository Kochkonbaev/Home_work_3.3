def func(first, second):
    count = 0
    for a, b in zip(first, second):
        if a == b:
            count += 1
        else:
            continue

    result = int((count * 100) / 10)
    print(f'\n{first} = {second}:\n{result}% - схожесть этих строк.\n')

func('asdfghjklo', 'qseftgjukl')
func('helloworld', 'helloworld')
