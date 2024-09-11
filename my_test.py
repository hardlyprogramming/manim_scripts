from manim import *
import numpy as np

class NumberLineDescription(Scene):
    def construct(self):
        # Introduction: Display the title and introduce the number line
        title = Text("A Number Line").scale(1.5).to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Step 1: Create the number line
        number_line = NumberLine(
            x_range=[-6, 6, 1],
            length=12,
            color=WHITE,
            include_numbers=True,
            include_ticks=True,
            tick_size=0.1,
            numbers_to_exclude=[-6, 6],
            label_direction=DOWN,
            include_tip=True
        )
        
        number_line.add_tip(at_start=True)
        # Fix scaling
        number_line.remove(number_line.ticks).remove(number_line.numbers)
        number_line.add_numbers()
        number_line.numbers_to_exclude=[-6,6]
        #number_line.add_ticks()
        for n in range(-5,6):
        
         mytick = number_line.get_tick(n, size=0.1)
         number_line.add(mytick)
        self.play(FadeIn(number_line))
        self.wait(1)
        
        # Description of the left side of the number line
        left_description = Text("As we move to the left, numbers get smaller or more negative.").scale(0.8).next_to(title, DOWN)
        self.play(Write(left_description))
        self.wait(1)
        
        # Highlight left side
        #my_ticks = number_line.get_tick([n for n in range(-5,1)], size=0.1)
        for number in reversed(number_line.numbers[:6]):
            self.play(Indicate(number, color=YELLOW), run_time=0.5)
        
        # Explain negative infinity
        neg_inf_label = MathTex(r"-\infty").next_to(number_line.get_start(), DOWN)
        self.play(Write(neg_inf_label))
        self.wait(1)
        
        # Describe moving to the right side
        right_description = Text("As we move to the right, numbers get larger or more positive.").scale(0.8).next_to(left_description, DOWN)
        self.play(Transform(left_description, right_description))
        self.wait(1)
        
        # Highlight right side
        for number in number_line.numbers[6:]:
            self.play(Indicate(number, color=YELLOW), run_time=0.5)
        
        # Explain positive infinity
        pos_inf_label = MathTex(r"\infty").next_to(number_line.get_end(), DOWN)
        self.play(Write(pos_inf_label))
        self.wait(5)

        # Fix scaling
        number_line.remove(number_line.ticks).remove(number_line.numbers)
        number_line.add_numbers()
        number_line.numbers_to_exclude=[-6,6]
        for n in range(-5,6):
        
         mytick = number_line.get_tick(n, size=0.1)
         number_line.add(mytick)

        # Explain plotting a point
        self.remove(left_description)
        point_desc = Text("Let's plot the number 2 as a point on the numberline", t2c={'2':RED}).scale(0.8).next_to(title, DOWN, buff=1)
        point_desc2 = Text("Let's plot the number -4 as a point on the numberline", t2c={'-4':BLUE}).scale(0.8).next_to(title, DOWN, buff=1)
        #point_desc.set_color_by_tex("2", RED)
        self.play(Write(point_desc))
        self.wait(1)
        point_pos = 2
        dot = Dot(point=number_line.number_to_point(point_pos), radius=.15, color = RED)
        self.play(FadeIn(dot))
        self.wait(3)
        self.play(Transform(point_desc, point_desc2))
        point_pos = -4
        dot2 = Dot(point=number_line.number_to_point(point_pos), radius=.15, color = BLUE)
        self.play(Transform(dot, dot2))
        self.wait(3)
        self.play(FadeOut(point_desc))
        self.wait(5)
        
        dot_2d_1 = Dot(point=np.array([1,2,0]), radius=0.15, color=GREEN)
        dot_2d_2 = Dot(point=np.array([-2,2,0]), radius=0.15, color=RED)
        dot_2d_3 = Dot(point=np.array([-1,-1,0]), radius=0.15, color=YELLOW)
        self.remove(dot)
        title2 = Text("?").scale(1.5).to_edge(UP)
        self.play(Transform(title, title2))
        self.wait(2)
        self.add(dot_2d_1)
        self.wait(2)
        self.play(Transform(dot_2d_1, dot_2d_2))
        self.wait(2)
        self.play(Transform(dot_2d_1, dot_2d_3))
        self.wait(3)
       
        self.remove(title)
        self.remove(point_desc)
        self.play(FadeOut(dot_2d_1))

        self.wait(2)
        title = Text("Coordinate Plane").scale(1.5).to_edge(UP)
        ax = Axes(x_range=(-6,6,1), y_range=(-3,3,1), x_length=12, y_length=7, axis_config={"include_numbers":True}).next_to(title, DOWN, buff=1.2)
        self.play(Transform(number_line,ax))
        self.remove(neg_inf_label)
        self.remove(pos_inf_label)
        self.play(FadeIn(title))

        p1 = Dot(ax.c2p(1,2), radius=0.15, color=GREEN)
        p2 = Dot(ax.c2p(-2,2), radius=0.15, color=RED)
        p3 = Dot(ax.c2p(-1,-1), radius=0.15, color=YELLOW)

        x_label = Text("x-axis").scale(0.7)
        y_label = Text("y-axis").scale(0.7)

        labels = ax.get_axis_labels(x_label, y_label)
        self.play(Write(labels))
        self.wait(2)
        self.play(Indicate(x_label))
        self.wait(2)
        self.play(Indicate(y_label))
        self.wait(2)
        self.play(FadeOut(labels))
        y_label= Text("y").scale(0.7)
        x_label = Text("x").scale(0.7)
        labels = ax.get_axis_labels(x_label,y_label)
        self.play(FadeIn(labels))
        self.wait(2)
        self.play(FadeIn(p1,p2,p3))
        self.wait(2)
        self.play(AnimationGroup(
            Indicate(x_label, color=YELLOW),
            Indicate(ax.x_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(1)
        self.play(AnimationGroup(
            Indicate(y_label, color=YELLOW),
            Indicate(ax.y_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(2)
        self.play(Indicate(p1, color=GREEN, scale_factor=2))
        xl1 = ax.get_vertical_line(ax.c2p(1,2), line_config={"dashed_ratio": 0.85})
        yl1 = ax.get_horizontal_line(ax.c2p(1,2), line_config={"dashed_ratio": 0.85})
        self.play(Write(xl1))
        self.wait(2)
        self.play(Write(yl1))
        self.wait(2)
        label1 = Text("(1,2)").scale(0.8).next_to(p1, RIGHT)
        self.play(FadeIn(label1))
        self.wait(5)

class OpenInterval(MovingCameraScene):
    def construct(self):
        # Step 1: Create the number line
        number_line = NumberLine(
            x_range=[0, 7, 1],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=DOWN
        )
        self.play(Create(number_line))
        self.wait(1)

        # Step 2: Highlight the open interval (2, 5)
        open_interval_start = number_line.n2p(2.01)
        open_interval_end = number_line.n2p(5)
        
        # Create open circles at the endpoints
        start_circle = Arc(radius=0.3, start_angle=(3.14/2), angle=3.14, color=YELLOW).move_to(number_line.n2p(2.095))
        #end_circle = Arc(radius=0.5, start_angle=(3.14/2), angle=-3.14, color=YELLOW).move_to(number_line.n2p(4.85))
        
        # Create the line for the interval
        interval_line = Line(start=open_interval_start, end=open_interval_end, color=YELLOW)
        
         # bracket
        end_bracket = VGroup(
            Line(color=YELLOW, start=number_line.n2p(5)+UP*0.3, end=number_line.n2p(5)+DOWN*0.3),
            Line(color=YELLOW,start=number_line.n2p(4.75)+UP*0.3, end=number_line.n2p(5)+UP*0.3),
            Line(color=YELLOW,start=number_line.n2p(4.75)+DOWN*0.3, end=number_line.n2p(5)+DOWN*0.3)
        )
        # Animate the creation of the open interval
        self.play(Create(interval_line))
        self.play(Create(start_circle), FadeIn(end_bracket))
        self.wait(1)
        
        # Step 3: Zoom in on the start point (2) to emphasize that it is not included
        self.play(
            self.camera.frame.animate.move_to(number_line.n2p(2)).set(width=1)
        )
        
        # Highlight the gap between 2 and 2.015
        gap_line = Line(
            start=number_line.n2p(2.005), 
            end=number_line.n2p(2.01), 
            color=RED,
            stroke_width=4
        )
        #gap_brace = Brace(gap_line, direction=DOWN, color=RED)
        #gap_brace_text = gap_brace.get_text("Tiny gap", font_size=24, color=RED)
        
        self.play(Create(gap_line))
        #self.play(Create(gap_brace), Write(gap_brace_text))
        self.wait(2)
        
        # Step 4: Zoom out to show the full interval again
        self.play(
            self.camera.frame.animate.move_to(number_line.get_center()).set(width=12)
        )
        self.wait(1)
        self.play(Indicate(start_circle, color=WHITE), run_time=0.5)
        text = Text("2 is not included", font_size=24, color=RED).next_to(start_circle, UP)
        self.play(Write(text))
        
        # Final explanation text
        explanation = Text("This is the interval (2, 5]").next_to(number_line, DOWN, buff=1)
        self.play(Write(explanation))
        self.wait(2)

class AFunction(Scene):
    def construct(self):
        # Introduction: Display the title and introduce the number line
        title = Text("Anatomy of a function").scale(1.5).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        func1 = MathTex(r"f(x) = 2x+3", substrings_to_isolate="x").scale(1.5)
        func1.set_color_by_tex("x", YELLOW)

        # Display the original function
        self.play(Write(func1))
        self.wait(2)
        
        # Indicate the machine part
        self.play(
            Indicate(func1[0][0], color=RED),
            Indicate(func1[0][1], color=RED),
            Indicate(func1[2][0], color=RED),
            )
        self.wait(2)

        self.play(
            Indicate(func1[1], color=RED),
            Indicate(func1[3], color=RED)
        )
        self.wait(2)
        self.play(func1.animate.shift(UP * 2))
        
        func2 = MathTex(r"f(x) = 2x+3", substrings_to_isolate="x").scale(1.5)
        func2.set_color_by_tex("x", YELLOW)

        self.play(Write(func2))
        self.wait(2)
        # Target function with 7
        func3 = MathTex(r"f(7) = 2(7) + 3", substrings_to_isolate="7").scale(1.5)
        func3.set_color_by_tex("7", YELLOW)


        # Transform the x to 7
        self.play(TransformMatchingTex(func2, func3))
        self.wait(3)

           # Simplify the expression
        simplified_func = MathTex(r"f(7) = 14 + 3").scale(1.5)
        self.play(ReplacementTransform(func3, simplified_func))
        self.wait(1)

        # Final result
        final_result = MathTex(r"f(7) = 17").scale(1.5)
        self.play(ReplacementTransform(simplified_func, final_result))
        self.wait(2)