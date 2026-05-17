from manim import Scene, MathTex, Write

class FormulaHeron(Scene):
	def construct(self):
		formula = MathTex("A=\\sqrt{s(s-a)(s-b)(s-c)}")
		self.play(Write(formula))
		self.wait(1)
