import random
import os
from datetime import datetime
from fpdf import FPDF
import subprocess

def generate_addition_problem(a, b):
    num1 = random.randint(10**(a-1), 10**a - 1)
    num2 = random.randint(10**(b-1), 10**b - 1)
    problem = f"{num1} + {num2} = "
    answer = num1 + num2
    return problem, answer

def generate_subtraction_problem(c, d):
    num1 = random.randint(10**(c-1), 10**c - 1)
    num2 = random.randint(10**(d-1), 10**d - 1)
    num1, num2 = max(num1, num2), min(num1, num2)  # Ensure positive answer
    problem = f"{num1} - {num2} = "
    answer = num1 - num2
    return problem, answer

def generate_multiplication_problem(e, f):
    num1 = random.randint(10**(e-1), 10**e - 1)
    num2 = random.randint(10**(f-1), 10**f - 1)
    problem = f"{num1} × {num2} = "
    answer = num1 * num2
    return problem, answer

def generate_division_problem(g, h):
    num1 = random.randint(10**(g-1), 10**g - 1)
    num2 = random.randint(10**(h-1), 10**h - 1)
    while num2 == 0 or num2 == 1 or num1 % num2 != 0 or num1==num2:  # Ensure non-zero denominator and integer result
        num1 = random.randint(10**(g-1), 10**g - 1)
        num2 = random.randint(10**(h-1), 10**h - 1)
    problem = f"{num1} ÷ {num2} = "
    answer = num1 // num2
    return problem, answer

def command_print(filename):
        command = "{} {}".format('PDFtoPrinter.exe',filename)
        subprocess.call(command,shell=True)

def generate_pdf_with_problems():
    num_problems = 24
    a, b = 1, 1  # 자리수 범위 설정 (덧셈)
    c, d = 1, 1  # 자리수 범위 설정 (뺄셈)
    e, f = 1, 1  # 자리수 범위 설정 (곱셈)
    g, h = 1, 1  # 자리수 범위 설정 (나눗셈)

    current_time = datetime.now()

    weekday_dict = {
        0: '월요일',
        1: '화요일',
        2: '수요일',
        3: '목요일',
        4: '금요일',
        5: '토요일',
        6: '일요일'
    }

    current_date = current_time.strftime("%Y년 %m월 %d일") + ' ' + weekday_dict[current_time.weekday()]
    current_date2 = current_time.strftime("%Y%m%d")
    filename = f"{current_date2}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('NGB', '', 'NanumGothicBold.ttf', uni=True)
    pdf.set_font("NGB", size=15)

    pdf.cell(200, 10, txt=current_date + " 문제", ln=True, align="L")
    pdf.cell(200, 10, txt="====================", ln=True, align="L")

    generated_problems = set()  # Set to store generated problems

    while len(generated_problems) < num_problems:
        problem_type = random.randint(1, 4)
        if problem_type == 1:
            problem, answer = generate_addition_problem(a, b)
        elif problem_type == 2:
            problem, answer = generate_subtraction_problem(c, d)
        elif problem_type == 3:
            problem, answer = generate_multiplication_problem(e, f)
        else:
            problem, answer = generate_division_problem(g, h)
        
        # Check if the problem is already generated, if not, add it to the set
        if problem not in generated_problems:
            generated_problems.add(problem)
            pdf.cell(90, 10, txt=problem, ln=False, align="L")
            pdf.cell(90, 10, txt=str(answer), ln=True, align="R")

    pdf.output(filename, 'F')
    command_print(filename)

generate_pdf_with_problems()
