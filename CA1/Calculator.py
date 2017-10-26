class Calculator(object):

    # Function to calculate addition

    def add(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

    # Function to calculate subtraction
    def subtract(self, x, y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError


    # Function to calculate multiplication
    def multiply(self, x, y):
        number_types = (int, long, float, complex)
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x * y
        else:
            raise ValueError


    # Function to calculate division
    def divide(self, x, y):
        number_types = (int, long, float, complex)


        if isinstance(x, number_types) and isinstance(y, number_types):
            if y == 0:
                return 'Nan'
            return x / float(y)
        else:
            raise ValueError


    # Function to calculate exponential
    def exponent(self, x, y):
        number_types = (int, long, float, complex)


        if isinstance(x, number_types) and isinstance(y, number_types):
            return x ** y
        else:
            raise ValueError


    # Function to calculate square root
    def squareRoot(self, x):
        from math import sqrt
        number_types = (int, float, long)
        if isinstance(x, number_types):
            x = sqrt(x)
            return round(x, 3)
        else:
            raise ValueError


    # Function to calculate squaring a number
    def squared(self, x):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types):
            return x ** 2
        else:
            raise ValueError


    # Function to calculate cubing a number
    def cubed(self, x):
        number_types = (int, long, float, complex)


		if isinstance(x, number_types):
			return x ** 3
		else:
			raise ValueError


    # Function to calculate sine
    def sin(self, x):
        from math import sin
		number_types = (int, long, float)
		
		if isinstance(x, number_types):
			x = sin(x)
			return round(x, 3)
		else:
			raise ValueError


    # Function to calculate cosine
    def cos(self, x):
        from math import cos

		number_types = (int, long, float)
		if isinstance(x, number_types):
			x = cos(x)
			return round(x, 3)
		else:
			raise ValueError

   