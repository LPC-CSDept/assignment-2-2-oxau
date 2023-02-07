def main():
    ##################################################
    # Comlete your code here
    ##################################################
    celsius = float(input('Temperature in Celsius: '))
    fahrenheit = float(9/5*(celsius))+32

    print ('Temperature in Fahrenheit: ' + '{0:.2f}'. format (fahrenheit))
    pass


if __name__ == '__main__':
    main()
