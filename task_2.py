"""task_2"""
from task_1 import reverse

with open("stdin.txt", "r", encoding = "utf-8") as input_file,\
    open("stdout.txt", "w", encoding = "utf-8") as output_file:
    data = input_file.read()
    out = output_file.write(str(reverse(data)))
