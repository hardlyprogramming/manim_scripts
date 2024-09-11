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
        self.wait(5)
        
        # Description of the left side of the number line
        left_description = Text("As we move to the left, numbers get smaller or more negative.").scale(0.8).next_to(title, DOWN)
        self.play(Write(left_description))
        self.wait(1)
        
        # Highlight left side
        #my_ticks = number_line.get_tick([n for n in range(-5,1)], size=0.1)
        for number in reversed(number_line.numbers[:6]):
            self.play(Indicate(number, color=YELLOW), run_time=0.6)
        
        # Explain negative infinity
        neg_inf_label = MathTex(r"-\infty").next_to(number_line.get_start(), DOWN)
        self.wait(6)
        self.play(Write(neg_inf_label))
        self.wait(3)
        
        # Describe moving to the right side
        right_description = Text("As we move to the right, numbers get larger or more positive.").scale(0.8).next_to(left_description, DOWN)
        self.play(Transform(left_description, right_description))
        self.wait(1)
        
        # Highlight right side
        for number in number_line.numbers[6:]:
            self.play(Indicate(number, color=YELLOW), run_time=0.5)
        
        # Explain positive infinity
        pos_inf_label = MathTex(r"\infty").next_to(number_line.get_end(), DOWN)
        self.wait(5)
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
        self.remove(dot)
        self.wait(4)
        dot_2d_1 = Dot(point=np.array([1,2,0]), radius=0.15, color=GREEN)
        dot_2d_2 = Dot(point=np.array([-2,2,0]), radius=0.15, color=RED)
        dot_2d_3 = Dot(point=np.array([-1,-1,0]), radius=0.15, color=YELLOW)
        
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

        self.wait(8)

        # ENTER COORDINATE PLANE
        title = Text("Coordinate Plane").scale(1.1).to_corner(UL)
        ax = Axes(x_range=(-6,6,1), y_range=(-3,3,1), x_length=12, y_length=7, axis_config={"include_numbers":True})
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
        self.play(AnimationGroup(
            Indicate(x_label, color=YELLOW),
            Indicate(ax.x_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(4)
        self.play(AnimationGroup(
            Indicate(y_label, color=YELLOW),
            Indicate(ax.y_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(2)
        self.play(FadeOut(labels))
        y_label= Text("y").scale(0.7)
        x_label = Text("x").scale(0.7)
        labels = ax.get_axis_labels(x_label,y_label)
        self.play(FadeIn(labels))
        self.wait(4)
        self.play(FadeIn(p1,p2,p3))
        self.wait(2)
        self.play(AnimationGroup(
            Indicate(x_label, color=YELLOW),
            Indicate(ax.x_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(0.5)
        self.play(AnimationGroup(
            Indicate(y_label, color=YELLOW),
            Indicate(ax.y_axis, color=YELLOW),
            lag_ratio=0  # Simultaneously
        ))
        self.wait(2)
        self.play(Indicate(p1, color=GREEN, scale_factor=2))
        xl1 = ax.get_vertical_line(ax.c2p(1,2), color=GREEN_B, line_config={"dashed_ratio": 0.85})
        yl1 = ax.get_horizontal_line(ax.c2p(1,2), color=GREEN_B, line_config={"dashed_ratio": 0.85})
        self.play(Write(xl1))
        self.wait(1)
        self.play(Write(yl1))
        self.wait(1)
        label1 = Text("(1,2)", color=GREEN).scale(0.8).next_to(p1, RIGHT)
        label2 = Text("Ordered Pair").scale(0.5).next_to(label1, UP)
        
        self.wait(2)
        self.play(FadeIn(label1))
        self.wait(3)
        self.play(FadeIn(label2))
        self.wait(5)
        label3 = Text("(-2,2)", color=RED).scale(0.8).next_to(p2, LEFT)
        label4 = Text("(-1,-1)", color=YELLOW).scale(0.8).next_to(p3, LEFT)

        xl2 = ax.get_vertical_line(ax.c2p(-2,2), color=RED_B, line_config={"dashed_ratio": 0.85})
        yl2 = ax.get_horizontal_line(ax.c2p(-2,2), color=RED_B, line_config={"dashed_ratio": 0.85})
        self.play(Write(xl2))
        self.wait(0.25)
        self.play(Write(yl2))
        self.play(FadeIn(label3))
        xl3 = ax.get_vertical_line(ax.c2p(-1,-1), color=YELLOW_B, line_config={"dashed_ratio": 0.85})
        yl3 = ax.get_horizontal_line(ax.c2p(-1,-1), color=YELLOW_B, line_config={"dashed_ratio": 0.85})
        self.play(Write(xl3))
        self.wait(0.25)
        self.play(Write(yl3))
        self.play(FadeIn(label4))
        self.wait(4)

        # REMOVE ALL POINTS

        self.play(AnimationGroup(
           FadeOut(xl1),
           FadeOut(yl1),
           FadeOut(xl2),
           FadeOut(yl2),
           FadeOut(xl3),
           FadeOut(yl3),
           FadeOut(p1),
           FadeOut(p2),
           FadeOut(p3),
           FadeOut(label1),
           FadeOut(label2),
           FadeOut(label3),
           FadeOut(label4),
           FadeOut(title))
        )
        self.wait(6)
        # Create rectangles to represent the four quadrants
        quadrant_1 = Rectangle(width=6, height=6).move_to([3, 3, 0]).set_fill(BLUE, opacity=0.5)
        quadrant_2 = Rectangle(width=6, height=6).move_to([-3, 3, 0]).set_fill(GREEN, opacity=0.5)
        quadrant_3 = Rectangle(width=6, height=6).move_to([-3, -3, 0]).set_fill(YELLOW, opacity=0.5)
        quadrant_4 = Rectangle(width=6, height=6).move_to([3, -3, 0]).set_fill(RED, opacity=0.5)

        # Highlight each quadrant briefly
        self.play(FadeIn(quadrant_1))
        self.wait(0.1)
        self.play(FadeOut(quadrant_1))
        
        self.play(FadeIn(quadrant_2))
        self.wait(0.1)
        self.play(FadeOut(quadrant_2))
        
        self.play(FadeIn(quadrant_3))
        self.wait(0.1)
        self.play(FadeOut(quadrant_3))
        
        self.play(FadeIn(quadrant_4))
        self.wait(0.1)
        self.play(FadeOut(quadrant_4))

        self.wait(2)
        q1_label = Text("I").next_to(ax.c2p(3,2), UP)
        q2_label = Text("II").next_to(ax.c2p(-3,2), UP)
        q3_label = Text("III").next_to(ax.c2p(-3,-2), DOWN)
        q4_label = Text("IV").next_to(ax.c2p(3,-2), DOWN)

        self.play(FadeIn(q1_label))
        self.wait(1)
        self.play(FadeIn(q2_label))
        self.wait(1)
        self.play(FadeIn(q3_label))
        self.wait(1)
        self.play(FadeIn(q4_label))
        self.wait(5)

        q1p = Dot(ax.c2p(2,1), radius=0.15, color=BLUE)
        q1p_label = Text("(2,1)", color=BLUE).next_to(q1p,RIGHT)
        q3p = Dot(ax.c2p(-2,-1), radius=0.15, color=RED)
        q3p_label = Text("(-2,-1)", color=RED).next_to(q3p,LEFT)

        self.play(FadeIn(q1p))
        self.play(FadeIn(q1p_label))
        self.wait(4)
        self.play(Transform(q1p, q3p))
        self.play(Transform(q1p_label, q3p_label))
        self.wait(4)
        self.remove(q1p)
        self.remove(q1p_label)

        # X and Y Intercepts
        self.wait(5)

        xint =Dot(ax.c2p(3,0), radius=0.15, color=GREEN)
        xint_label = Text("(3,0)", color=GREEN).next_to(xint,UP)
        xint_label2 = Text("x-intercept", color=GREEN).next_to(xint_label,UP)

        self.play(FadeIn(xint))
        self.play(FadeIn(xint_label))
        self.wait(5)
        self.play(FadeIn(xint_label2))
        self.wait(4)
        self.play(FadeOut(xint))
        self.play(FadeOut(xint_label))
        self.play(FadeOut(xint_label2))

        yint = Dot(ax.c2p(0,2), radius=0.15, color=BLUE)
        yint_label = Text("(0,2)", color=BLUE).next_to(yint,RIGHT)
        yint_label2 = Text("y-intercept", color=BLUE).next_to(yint_label,RIGHT)
        self.play(FadeIn(yint))
        self.play(FadeIn(yint_label))
        self.wait(4)
        self.play(FadeIn(yint_label2))
        self.wait(3)
        self.play(FadeOut(yint_label))
        self.play(FadeOut(yint_label2))
        self.play(FadeOut(yint))
        self.wait(10)


