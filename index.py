import math

#we need to get the three points
p1 = [float(num) for num in input('Enter coordinators of first point: ').split(",")]
p2 = [float(num) for num in input('Enter coordinators of second point: ').split(",")]
p3 = [float(num) for num in input('Enter coordinators of third point: ').split(",")]


if p1[0] == p2[0] or p3[0] == p1[0] or p2[0] == p3[0]:
    print("Detected two same X values, this will cause an error that I'm not responsible for :P (0 division will occur)")


def getA():
    #formula for A-- a = ({[(y1-y2)/(x1-x2)]} - {[(y2-y3)/(x2-x3)]}) / (x1-x3)
    partA = (p1[1] - p2[1])/(p1[0] - p2[0])
    partB = (p2[1] - p3[1])/(p2[0] - p3[0])
    denom = p1[0] - p3[0]
    return (partA - partB) / denom

def getB():
    a = getA()
    #formula for B when we know A-- B = [(y1-y2)/(x1-x2)] - a(x1+x2)
    partA = (p1[1] - p2[1])/(p1[0] - p2[0])
    summed = p1[0] + p2[0]
    return partA - (a*summed)

def getC():
    a = getA()
    b = getB()
    #if we know A and B and x and y, obviously y = Ax^2 + Bx + c, then c = y - Ax^2 - Bx
    expressionWithAAndB = a*(p1[0])*(p1[0]) + b*(p1[0])
    return p1[1] - expressionWithAAndB

def contstructPolynomial(a: float, b: float, c: float):
    return "(" + str(a) + ")x^2 + (" + str(b) + ")x + " + str(c)

def extractABCFromPolynomial(polynomial: str):
    terms = polynomial.split(" + ")

    a = float(terms[0].split(")")[0].split("(")[1])
    b = float(terms[1].split(")")[0].split("(")[1])
    c = float(terms[2])

    return [a, b, c]

def getFunctionForPolynomial(polynomial: str):
    terms = extractABCFromPolynomial(polynomial)

    print("when contruction function, found a b and c to be", terms[0], terms[1], terms[2])

    return lambda x: terms[0]*x*x + terms[1]*x + terms[2]

def getDiscriminant(polynomial: str):
    terms = extractABCFromPolynomial(polynomial)

    return (terms[1])*(terms[1]) - 4*(terms[0]*terms[2])

def getVertex(polynomial: str):
    terms = extractABCFromPolynomial(polynomial)
    D = getDiscriminant(polynomial)

    vertexX = terms[1]/(-2 * terms[0]) #vertex lies at -b/2a

    ## a*(-b/2a)^2 = b^2 / 4a
    ## b*(-b/2a) = -b^2/2a = -2b^2 / 4a
    ## b^2/4a + (-2b^2/4a) + c = -b^2/4a + 4ac/4a = (-b^2 + 4ac) / 4a = -D/4a
    vertexY = -D / (4 * terms[0])

    return str(vertexX) + "," + str(vertexY)

def printSolutions(polynomial):
    terms = extractABCFromPolynomial(polynomial)
    D = getDiscriminant(polynomial)

    if(D < 0):
        print("No real roots")
        return

    solutions = [(-terms[1] + math.sqrt(D))/(2*terms[0]), (-terms[1] - math.sqrt(D))/(2*terms[0])]

    if(D > 0): 
        print("There are 2 solutions: x = "+str(solutions[0]) + ", and x = " + str(solutions[1]))
    if(D == 0):
        print("There is one distinct solution: x = "+str(solutions[0]))

################# outputs
        
a = getA()
b = getB()
c = getC()

poly = contstructPolynomial(a, b, c)

print("The polynomial is y = " + poly)

if(a != 0):
    print("Vertex lies at " + str(getVertex(poly)))
    printSolutions(poly)
    
functionForCurrPolynomial = getFunctionForPolynomial(poly)

print("function for polynomial has been found")

while True:
    x = str(input("Enter a value for x: "))
    if(x == "exit"):
        break
    print(functionForCurrPolynomial(float(x)))