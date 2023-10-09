#!/bin/python3

import math
import os
import random
import re
import sys

class Result:
    
    def first_function(x: float, y: float):
        return math.sin(x)


    def second_function(x: float, y: float):
        return (x * y)/2


    def third_function(x: float, y: float):
        return y - (2 * x)/y


    def fourth_function(x: float, y: float):
        return x + y

    
    def default_function(x:float, y: float):
        return 0.0

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        else:
            return Result.default_function

    #
    # Complete the 'solveByRungeKutta' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. INTEGER f
    #  2. DOUBLE epsilon
    #  3. DOUBLE a
    #  4. DOUBLE y_a
    #  5. DOUBLE b
    #
    def solveByRungeKutta(f, epsilon, a, y_a, b):
        function = Result.get_function(f)

        x = a
        y = y_a
        
        step = 0.1
        
        
        while x < b:
            RungeKuttaCoeff1 = step * function(x, y)
            RungeKuttaCoeff2 = step * function(x + step/2, y + RungeKuttaCoeff1/2)
            RungeKuttaCoeff3 = step * function(x + step/2, y + RungeKuttaCoeff2/2)
            RungeKuttaCoeff4 = step * function(x + step, y + RungeKuttaCoeff3)
            
            # Tính giá trị mới của hàm số tại điểm x tiếp theo bằng cách sử dụng các hệ số Runge-Kutta đã tính được
            y_result = y + (RungeKuttaCoeff1 + 2*RungeKuttaCoeff2 + 2*RungeKuttaCoeff3 + RungeKuttaCoeff4)/6

            # Tính sai số giữa giá trị mới và giá trị cũ của hàm số
            error = abs(y_result - y)/15
            if error == 0:
                step = epsilon/1000
            step_new=step*(epsilon/(2*error))**0.25
            # Cập nhật giá trị của biến độc lập x và giá trị của hàm số y
            x += step
            y = y_result
            step=min(step_new, b-x)
        
        return y

if __name__ == '__main__':

    # Nhập các tham số đầu vào
    f = int(input().strip())
    epsilon = float(input().strip())
    a = float(input().strip())
    y_a = float(input().strip())
    b = float(input().strip())

    # Gọi hàm giải phương trình vi phân bằng phương pháp Runge-Kutta
    result = Result.solveByRungeKutta(f, epsilon, a, y_a, b)

    # In kết quả
    print(str(result) + '\n')