#
# conversions.py - module with functions to convert between units
#
# fahr2cel : Convert from Farenheit to Celcius.
#

def fahr2cel(fahr):
    """Convert from Fahrenheit to Celcius.
    Argument:
    fahr - the temperture in Fahrenheit
    """
    celcius = (fahr - 32) * (5/9)
    return celcius

def cel2fahr(cel):

    """Convert from Celcius to Fahrenheit.
    Argument:
    cel - the temperture in Celcius
    """
    fahrenheit = cel * (9/5) + 32
    return fahrenheit


def cel2kel(cel):

    """Convert from Celcius to Kelvin.
    Argument:
    cel - the temperture in Celcius
    """
    kelvin = cel + 273.15
    return kelvin


def kel2cel(kel):

    """Convert from Kelvin to Celcius.
    Argument:
    kel - the temperture in Kelvin
    """
    celcius = kel - 273.15
    return celcius


def fahr2kel(fahr):

    """Convert from Fahrenheit to Kelvin.
    Argument:
    fahr - the temperture in Fahrenheit
    """
    kelvin = fahr -  32
    return kelvin


def kel2fahr(kel):

    """Convert from Kelvin to Fahrenheit.
    Argument:
    Kel - the temperture in Kelvin
    """
    fahrenheit = (kel - 273.15) * 1.8 + 32
    return fahrenheit
def main():
    print('\nTesting textfun.py')
    print('200 Fahrenheit in Celcius is:', fahr2cel(200))
    # put your testing code here
    print('\nTesting complete\n')
if __name__ == "__main__":
    main()
