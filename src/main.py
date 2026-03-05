#!/usr/bin/env python3

print("Welcome to Git Learning Project!")
print("This is version 1 of the application.")

# Version 2 feature: User greeting
name = "Student"
print(f"Hello, {name}!")
print("Enjoying the Git learning experience?")

def greet_user(name):
    # Function to greet users personalized.
    return f"Welcome, {name}! Ready to learn Git?"

def get_project_info():
    # New function: Get project information
    return "Git Learning Project - Educational repository for learning Git and GitHub workflows"

if __name__ == "__main__":
    result = greet_user("Student")
    print(result)
    print(get_project_info())
