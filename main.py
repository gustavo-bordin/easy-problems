import importlib
import os
import sys


PROBLEMS_MODULE = 'problems'
problems_class_path = 'problems.problem_{}.Problem{}'


try:
    specified_problem = int(sys.argv[1])
    files_count = specified_problem + 1
except:
    _, _, files = next(os.walk(PROBLEMS_MODULE))
    files_count = len(files) + 1
    specified_problem = 1


for problem_number in range(specified_problem, files_count):
    problem_file = f'{PROBLEMS_MODULE}.problem_{problem_number}'

    print(f"Running PROBLEM {problem_number} solutions...", end="\n\n")
    
    try:
        problem_module = importlib.import_module(problem_file)
    except:
        print(f"Could not find problem {problem_number} file. Exiting...")

    print('\n\n')