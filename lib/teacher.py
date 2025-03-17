#!/usr/bin/env python

# teacher.py
from user import User
import random

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History", "Programming"]

    def teach(self):
        return random.choice(self.knowledge)
