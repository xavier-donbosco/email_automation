# Databricks notebook source
# DBTITLE 1,Import Statements
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# COMMAND ----------

# DBTITLE 1,Python Questions
python_questions = [
    # Question 1
    [
        "1. Write a Python program to check if a number is prime or not.",
        {"input": 7, "output": "Prime"},
        {"input": 8, "output": "Not Prime"}
    ],
    # Question 2
    [
        "2. Write a Python program to reverse a string without using slicing.",
        {"input": "hello", "output": "olleh"},
        {"input": "world", "output": "dlrow"}
    ],
    # Question 3
    [
        "3. Write a Python program to find the factorial of a number using recursion.",
        {"input": 5, "output": 120},
        {"input": 3, "output": 6}
    ],
    # Question 4
    [
        "4. Write a Python function to check if a string is a palindrome.",
        {"input": "radar", "output": True},
        {"input": "hello", "output": False}
    ],
    # Question 5
    [
        "5. Write a Python program to merge two sorted lists.",
        {"input": ([1, 3, 5], [2, 4, 6]), "output": [1, 2, 3, 4, 5, 6]},
        {"input": ([7, 8], [1, 9]), "output": [1, 7, 8, 9]}
    ],
    # Question 6
    [
        "6. Write a Python program to count the number of vowels in a string.",
        {"input": "hello world", "output": 3},
        {"input": "python programming", "output": 6}
    ],
    # Question 7
    [
        "7. Write a Python program to find the largest element in a list.",
        {"input": [1, 2, 3, 4, 5], "output": 5},
        {"input": [10, 20, 30, 5], "output": 30}
    ],
    # Question 8
    [
        "8. Write a Python program to implement a basic calculator.",
        {"input": (10, 5, 'add'), "output": 15},
        {"input": (10, 5, 'subtract'), "output": 5}
    ],
    # Question 9
    [
        "9. Write a Python program to find the common elements between two lists.",
        {"input": ([1, 2, 3], [2, 3, 4]), "output": [2, 3]},
        {"input": ([5, 6, 7], [7, 8, 9]), "output": [7]}
    ],
    # Question 10
    [
        "10. Write a Python program to remove duplicates from a list.",
        {"input": [1, 2, 2, 3, 4, 4], "output": [1, 2, 3, 4]},
        {"input": ["apple", "banana", "apple"], "output": ["apple", "banana"]}
    ],
    # Question 11
    [
        "11. Write a Python program to check if a string contains only digits.",
        {"input": "12345", "output": True},
        {"input": "abc123", "output": False}
    ],
    # Question 12
    [
        "12. Write a Python program to flatten a nested list.",
        {"input": [[1, 2], [3, 4]], "output": [1, 2, 3, 4]},
        {"input": [[1, [2]], [3]], "output": [1, 2, 3]}
    ],
    # Question 13
    [
        "13. Write a Python program to find the intersection of two lists.",
        {"input": ([1, 2, 3], [2, 3, 4]), "output": [2, 3]},
        {"input": ([5, 6], [6, 7]), "output": [6]}
    ],
    # Question 14
    [
        "14. Write a Python program to sort a dictionary by its keys.",
        {"input": {"b": 2, "a": 1}, "output": {'a': 1, 'b': 2}},
        {"input": {"cat": 3, "ant": 1}, "output": {'ant': 1, 'cat': 3}}
    ],
    # Question 15
    [
        "15. Write a Python program to implement the Fibonacci sequence.",
        {"input": 5, "output": 5},  # Fibonacci(5) = 5
        {"input": 7, "output": 13}  # Fibonacci(7) = 13
    ],
    # Question 16
    [
        "16. Write a Python program to calculate the sum of all even numbers in a list.",
        {"input": [1, 2, 3, 4, 5], "output": 6},
        {"input": [10, 15, 20], "output": 30}
    ],
    # Question 17
    [
        "17. Write a Python program to create a countdown timer.",
        {"input": 5, "output": "4, 3, 2, 1, 0"},
        {"input": 3, "output": "2, 1, 0"}
    ],
    # Question 18
    [
        "18. Write a Python program to generate a random password.",
        {"input": 8, "output": "A8j#k9l!"},
        {"input": 12, "output": "X8y%3l!Pz@8n"}
    ],
    # Question 19
    [
        "19. Write a Python program to check for anagrams.",
        {"input": ("listen", "silent"), "output": True},
        {"input": ("hello", "world"), "output": False}
    ],
    # Question 20
    [
        "20. Write a Python program to convert a list of tuples into a dictionary.",
        {"input": [(1, 'a'), (2, 'b')], "output": {1: 'a', 2: 'b'}},
        {"input": [(3, 'c'), (4, 'd')], "output": {3: 'c', 4: 'd'}}
    ],
    # Question 21
    [
        "21. Write a Python program to find the first non-repeating character in a string.",
        {"input": "swiss", "output": "w"},
        {"input": "success", "output": "u"}
    ],
    # Question 22
    [
        "22. Write a Python program to perform matrix addition.",
        {"input": ([[1, 2], [3, 4]], [[5, 6], [7, 8]]), "output": [[6, 8], [10, 12]]},
        {"input": ([[1, 1], [1, 1]], [[2, 2], [2, 2]]), "output": [[3, 3], [3, 3]]}
    ],
    # Question 23
    [
        "23. Write a Python program to rotate a list by `n` positions.",
        {"input": ([1, 2, 3, 4], 2), "output": [3, 4, 1, 2]},
        {"input": ([5, 6, 7, 8], 3), "output": [8, 5, 6, 7]}
    ],
    # Question 24
    [
        "24. Write a Python program to count the occurrences of each element in a list.",
        {"input": [1, 2, 2, 3], "output": {1: 1, 2: 2, 3: 1}},
        {"input": ['apple', 'banana', 'apple'], "output": {'apple': 2, 'banana': 1}}
    ],
    # Question 25
    [
        "25. Write a Python program to check if a list is a subset of another list.",
        {"input": ([1, 2, 3], [2, 3]), "output": True},
        {"input": ([1, 2, 3], [4, 5]), "output": False}
    ]
]

# COMMAND ----------

# DBTITLE 1,HTML Body
def generate_html_body(random_question):
    question_text       = random_question[0]
    first_input_output  = random_question[1]
    second_input_output = random_question[2]
    html_body = f"""
    <html>
        <body>
            <h2>Today's Python Question</h2>
            <table border="1" style="width:100%; border-collapse: collapse;">
                <tr>
                    <th>Question</th>
                    <th>First Example (Input/Output)</th>
                    <th>Second Example (Input/Output)</th>
                </tr>
                <tr>
                    <td>{question_text}</td>
                    <td>Input: {first_input_output["input"]} <br> Output: {first_input_output["output"]}</td>
                    <td>Input: {second_input_output["input"]} <br> Output: {second_input_output["output"]}</td>
                </tr>
            </table>
            
            <div style="text-align: right; margin-top: 20px;">
                Thanks for your time,<br>
                Team Data Thunders.
            </div>
            
            <div style="text-align: center; margin-top: 20px; color: red; font-style: italic;">
                "This is auto-generated gmail"
            </div>
        </body>
    </html>
    """
    return html_body
