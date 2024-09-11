from manim import *
import numpy as np

class Functions(Scene):
    def construct(self):

      # Initial function: f(x) = 3x^2 - 1
        function = MathTex("f(x) = 3x^2 - 1")
      # Function showing input of -5
        function_with_input = MathTex("f(-5) = 3(-5)^2 - 1")
      # Asking question
        question = MathTex("Find\\quad f(-5)").shift(2*UP)
      # Isolates the "-5" from the question
        neg5 = question[0][6:8]
        neg5_final = Group(function_with_input[0][2:4],function_with_input[0][8:10])
        neg5_final.set_color(BLUE)
        xs = Group(function[0][2], function[0][6])
      # Show initial function
        self.play(function.animate.shift(3*UP))
      # Show the question
        self.play(Write(question))
        self.wait(3)
      # Highlight the function
        self.play(Indicate(function))
      # Highlight the "x's" within the function
        self.play(Indicate(Group(function[0][2], function[0][6]), color=BLUE))
        xs.set_color(BLUE)
      # Highlight the "-5" within the question
        self.play(Indicate(neg5, color=BLUE))
        neg5.set_color(BLUE)
      # Rewrite the function with parenthesis instead of "x's"
        self.play(Write(function_with_input[0][0:2]))
        self.play(Write(function_with_input[0][4:8]))
        self.play(Write(function_with_input[0][10:]))
      # Show replacement animation "-5" --> ( )
        self.play(ReplacementTransform(neg5.copy(), function_with_input[0][2:4]))
        self.play(ReplacementTransform(neg5.copy(), function_with_input[0][8:10]))



        self.wait(10)
