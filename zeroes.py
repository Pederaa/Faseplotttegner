from typing import Iterable
from sympy import lambdify, FiniteSet, Interval, ProductSet, ImageSet, ComplexRegion, ConditionSet, Naturals, Naturals0, Integers, Reals, Complexes, EmptySet, ConditionSet
from sympy.solvers import solve, solveset, nonlinsolve
from scipy.integrate import solve_ivp


class zero:
    def __init__(self) -> None:
        self.x = None
        self.y = None
        self.z = None


class zeroes(list):
    def __init__(self, type_="Set") -> None:
        self.type_ = type_

    
    def getZeros(self, system, symbols):
        p = nonlinsolve(system.getList(), symbols)
        
        z = zeroes(type_="tuple")

        if isinstance(p, FiniteSet):
            for s in p:
                z.extend(self.iterateZero(s))
        
        elif p is EmptySet:
            return []
        
        else:
            z.extend(self.iterateZero(p))
        
        return z
    
    def iterateZero(self, s):       
        x = self.extractPointFromSet(s[0])
        y = self.extractPointFromSet(s[1])

        zeroes = []
        for i in x:
            for j in y:
                zeroes.append((i, j))
        return zeroes


    def extractPointFromSet(self, setToExtract):
        if isinstance(setToExtract, int) or isinstance(setToExtract, float) or isinstance(setToExtract, Number):
            return [setToExtract]
        
        if isinstance(setToExtract, ConditionSet):
            raise ValueError("Unhandled type of zeroes: ConditionSet", setToExtract)

        elif isinstance(setToExtract, FiniteSet):
            raise ValueError("Unhandled type of zeroes: FiniteSet", setToExtract)
        
        elif isinstance(setToExtract, Interval):
            raise ValueError("Unhandled type of zeroes: Interval", setToExtract)
        
        elif isinstance(setToExtract, ProductSet):
            raise ValueError("Unhandled type of zeroes: ProductSet", setToExtract)
        
        elif isinstance(setToExtract, ImageSet):
            values = []
            for i in range(-2, 3):
                values.append(setToExtract.lamda(i))
            return values
        
        elif isinstance(setToExtract, ComplexRegion):
            raise ValueError("Unhandled type of zeroes: ComplexRegion", setToExtract)
        
        # elif isinstance(s, Naturals):
        #     raise ValueError("Unhandled type of zeroes: Naturals", s)
        
        # elif isinstance(s, Naturals0):
        #     raise ValueError("Unhandled type of zeroes: Naturals0", s)
        
        # elif isinstance(s, Reals):
        #     raise ValueError("Unhandled type of zeroes: Reals", s)
        
        # elif isinstance(s, Complexes):
        #     raise ValueError("Unhandled type of zeroes: Complexes", s)
        
        # elif isinstance(setToExtract, EmptySet):
            pass 

        else:
            raise ValueError("Unidentified type of zeroes", setToExtract)  