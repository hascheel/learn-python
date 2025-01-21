'''
Operatoren - Entwickeln Sie ein einfaches Programm, das zwei Zahlen 
vom Benutzer abfragt und die Ergebnisse der vier Grundrechenarten (+, -, *, /) ausgibt. 
'''

a = int(input('Gib die erste Zahl ein: '))
select = input('Wähle ein Rechenart (+ - / *): ')
b = int(input('Gib die zweite Zahl ein: '))

def sum(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    if b == 0:
        return 'Division durch 0 nicht möglich.'
    else:
        return (a / b)

match select:
    case "+":
        result = sum(a, b)
    case "-":
        result = sub(a, b)
    case "*":
        result = mul(a, b)
    case "/":
        result = div(a, b)

print(a,select,b,'=',result)