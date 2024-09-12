from manim import *
import numpy as np

class Functions(Scene):
    def construct(self):

      # Initial function: f(x) = 3x^2 - 1
        function = MathTex("f(x) = 3x^2 - 1").shift(0.2*LEFT)
      # Function showing input of -5
        function_with_input = MathTex("f(-5) = 3(-5)^2 - 1").shift(1*UP)
      # Asking question
        question = MathTex("Find\\quad f(-5)").shift(2*UP)
      # Step 2 solve
        f2 = MathTex("= 3(25) - 1").shift(0.55*RIGHT)
      # Step 3 solve
        f3 = MathTex("= 75 - 1").shift(1*DOWN, 0.25*RIGHT)
      # Final Answer
        answer = MathTex("= 74").shift(1*DOWN, 0.2*LEFT)

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
        #self.play(function.animate.shift(3*LEFT))
        #self.play(question.animate.shift(1*UP+RIGHT))
        #self.play(Animation(function.to_edge(LEFT)))
        #self.play(Animation(question.to_edge(UP)))
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
        #self.play(function_with_input.animate.shift(1*UP))
        self.play(Circumscribe(function_with_input[0][7:12], run_time=2, time_width=0.5))
        #function_with_input[0][7:12].set_color(YELLOW)
        self.wait(2)
        #f2[0][2:6].set_color(YELLOW)
        self.play(ReplacementTransform(function_with_input.copy(), f2))
        self.wait(1)
        self.play(Circumscribe(f2[0][1:6], run_time=2,time_width=0.5))
        self.wait(1)
        #f2[0][1:6].set_color(RED)
        self.wait(1)
        #f3[0][1:3].set_color(RED)
        self.play(ReplacementTransform(f2.copy(), f3))
        self.wait(2)
        self.play(ReplacementTransform(f3,answer))
        self.play(Circumscribe(answer[0][1:], run_time=2, color=GREEN))
        #self.play(Circumscribe(answer[0][1:], run_time=2, color=GREEN))
        #self.play(Circumscribe(answer[0][1:], run_time=2, color=GREEN))

        self.wait(10)
