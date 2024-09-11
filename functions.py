from manim import *
import numpy as np

class Functions(Scene):
    def construct(self):

      # Initial function: f(x) = 3x^2 + 5
        #function = MathTex("f(x)", "=", "3x^2", "+", "5").shift(UP * 2)
        function = MathTex("f(x) = 3x^2 - 5")
        function_with_input = MathTex("f(-5) = 3(-5)^2 - 5")
        # Question: Find f(-4)
        #question = MathTex("Find", "f(-4)").next_to(function, DOWN * 2)
        question = MathTex("Find\\quad f(-5)").shift(1*UP)
        neg5 = question[0][6:8]
        self.play(function.animate.shift(2*UP))
        self.play(Write(question))
        self.wait(3)
        self.play(Indicate(function))
        self.play(Indicate(Group(function[0][2], function[0][6])))
        self.play(Indicate(question[0][6:8]))
        self.play(Write(function_with_input[0][0:2]))
        self.play(Write(function_with_input[0][4:8]))
        self.play(Write(function_with_input[0][10:]))
        self.play(ReplacementTransform(neg5.copy(), function_with_input[0][2:4]))
        self.play(ReplacementTransform(neg5.copy(), function_with_input[0][8:10]))



        self.wait(5)
