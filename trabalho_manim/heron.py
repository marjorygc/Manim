from manim import *
import numpy as np

class FormulaHeron(Scene):

    def caixa(self, mobject, cor=YELLOW, buff=0.18):
        return SurroundingRectangle(mobject, color=cor, buff=buff)

    def limpar(self):
        """Remove tudo da tela de uma vez."""
        self.play(*[FadeOut(m) for m in self.mobjects])

    # =========================================================
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self._cena_titulo()
        self._cena_triangulo()
        self._cena_pitagoras()
        self._cena_x_isolado()
        self._cena_h2()
        self._cena_area_quadrada()
        self._cena_algebra()
        self._cena_resultado_heron()
        self._cena_exercicio37()

    # =========================================================
    # CENA 0 — Título
    # =========================================================
    def _cena_titulo(self):
        linha1 = Text("Área do Triângulo", font_size=52, color=YELLOW, weight=BOLD)
        linha2 = Text("Fórmula de Heron",  font_size=44, color=WHITE)
        linha3 = Text("Dedução completa",  font_size=28, color=GRAY)
        grupo  = VGroup(linha1, linha2, linha3).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(linha1, shift=UP*0.3))
        self.play(Write(linha2))
        self.play(FadeIn(linha3))
        self.wait(2)
        self.limpar()

    # =========================================================
    # CENA 1 — Triângulo com altura h
    # =========================================================
    def _cena_triangulo(self):
        titulo = Text("Triângulo com altura h", font_size=34, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        A = np.array([ 0,  2.2, 0])
        B = np.array([-3, -1.2, 0])
        C = np.array([ 3, -1.2, 0])
        H = np.array([ 0, -1.2, 0])

        tri    = Polygon(A, B, C, color=WHITE, stroke_width=2.5)
        h_line = DashedLine(A, H, color=BLUE, dash_length=0.15)
        sq     = Square(side_length=0.2, color=BLUE, stroke_width=1.5)
        sq.move_to(H + np.array([0.1, 0.1, 0]))

        self.play(Create(tri))
        self.play(Create(h_line), Create(sq))

        lA  = Text("A",   font_size=26).next_to(A, UP,    buff=0.1)
        lB  = Text("B",   font_size=26).next_to(B, LEFT,  buff=0.1)
        lC  = Text("C",   font_size=26).next_to(C, RIGHT, buff=0.1)
        lH  = Text("H",   font_size=22, color=BLUE).next_to(H, DOWN, buff=0.1)
        la  = Text("a",   font_size=26, color=GREEN ).next_to((B+C)/2, DOWN,  buff=0.15)
        lb  = Text("b",   font_size=26, color=RED   ).next_to((A+C)/2, RIGHT, buff=0.1)
        lc  = Text("c",   font_size=26, color=ORANGE).next_to((A+B)/2, LEFT,  buff=0.1)
        lx  = Text("x",   font_size=22, color=BLUE).next_to((B+H)/2, DOWN, buff=0.15)
        lax = Text("a-x", font_size=22, color=BLUE).next_to((H+C)/2, DOWN, buff=0.15)
        lh  = Text("h",   font_size=22, color=BLUE).next_to(A*0.3+H*0.7, RIGHT, buff=0.08)

        self.play(Write(lA), Write(lB), Write(lC), Write(lH))
        self.play(Write(la), Write(lb), Write(lc))
        self.play(Write(lx), Write(lax), Write(lh))
        self.wait(2)

        self._tri_mobs = VGroup(tri, h_line, sq, lA, lB, lC, lH, la, lb, lc, lx, lax, lh)
        self.play(FadeOut(titulo))

    # =========================================================
    # CENA 2 — Pitágoras
    # =========================================================
    def _cena_pitagoras(self):
        titulo = Text("Pitágoras em AHB e AHC", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        tri_group = self._tri_mobs
        tri_group.generate_target()
        tri_group.target.scale(0.72).to_edge(LEFT, buff=0.4).shift(DOWN*0.3)
        self.play(MoveToTarget(tri_group))

        eqs = VGroup(
            Text("(I)   c² = h² + x²",       font_size=26),
            Text("(II)  b² = h² + (a - x)²", font_size=26),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        eqs.to_edge(RIGHT, buff=0.7).shift(UP*0.5)

        self.play(Write(eqs[0]))
        self.wait(0.8)
        self.play(Write(eqs[1]))
        self.wait(1.2)

        sub_label = Text("Substituindo (I) em (II):", font_size=24, color=BLUE)
        sub_label.next_to(eqs, DOWN, buff=0.35, aligned_edge=LEFT)
        self.play(Write(sub_label))

        sub_eq = Text("b² = c² - x² + (a - x)²", font_size=25)
        sub_eq.next_to(sub_label, DOWN, buff=0.25, aligned_edge=LEFT)
        self.play(Write(sub_eq))

        exp1 = Text("= c² - x² + a² - 2ax + x²", font_size=25)
        exp1.next_to(sub_eq, DOWN, buff=0.2, aligned_edge=LEFT)
        self.play(Write(exp1))

        cancel_note = Text("(x² cancela)", font_size=20, color=RED)
        cancel_note.next_to(exp1, RIGHT, buff=0.15)
        self.play(FadeIn(cancel_note))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 3 — Isolando x  (fórmula III)
    # =========================================================
    def _cena_x_isolado(self):
        titulo = Text("Isolando x  →  fórmula (III)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("b² = c² + a² - 2ax",           font_size=26),
            Text("2ax = a² + c² - b²",            font_size=26),
            Text("x = (a² + c² - b²) / (2a)",     font_size=27, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)
        passos.move_to(ORIGIN + DOWN*0.2)

        label3 = Text("(III)", font_size=26, color=GREEN)
        label3.next_to(passos[2], RIGHT, buff=0.3)

        for p in passos:
            self.play(Write(p))
            self.wait(0.7)
        self.play(Write(label3))

        caixa3 = self.caixa(VGroup(passos[2], label3), cor=GREEN)
        self.play(Create(caixa3))
        self.wait(2)

        self._x_formula = VGroup(passos[2].copy(), label3.copy(), caixa3.copy())
        self.limpar()
        self._x_formula.scale(0.65).to_corner(UL, buff=0.3)
        self.add(self._x_formula)

    # =========================================================
    # CENA 4 — Calculando h²  (fórmula IV)
    # =========================================================
    def _cena_h2(self):
        titulo = Text("Calculando h²  →  fórmula (IV)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("h² = c² - x²",                               font_size=25),
            Text("Substituindo x = (a²+c²-b²)/(2a):",          font_size=22, color=BLUE),
            Text("h² = c² - [(a²+c²-b²)/(2a)]²",              font_size=25),
            Text("h² = [4a²c² - (a²-b²+c²)²] / (4a²)",        font_size=25, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        passos.move_to(ORIGIN + DOWN*0.3)

        label4 = Text("(IV)", font_size=25, color=GREEN)
        label4.next_to(passos[3], RIGHT, buff=0.25)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)
        self.play(Write(label4))

        caixa4 = self.caixa(VGroup(passos[3], label4), cor=GREEN)
        self.play(Create(caixa4))
        self.wait(2)

        self._h2_formula = VGroup(passos[3].copy(), label4.copy(), caixa4.copy())
        self.limpar()
        self._h2_formula.scale(0.6).to_corner(UL, buff=0.3)
        self.add(self._h2_formula)

    # =========================================================
    # CENA 5 — Área ao quadrado  (fórmula V)
    # =========================================================
    def _cena_area_quadrada(self):
        titulo = Text("Área ao quadrado  →  fórmula (V)", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Sendo A = (a . h) / 2,",              font_size=25),
            Text("A² = (a² . h²) / 4",                 font_size=25),
            Text("Substituindo (IV) em A²:",            font_size=22, color=BLUE),
            Text("A² = a²·[4a²c²-(a²-b²+c²)²]/(16a²)", font_size=24),
            Text("A² = [4a²c² - (a²-b²+c²)²] / 16",   font_size=24, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos.move_to(ORIGIN + DOWN*0.3)

        label5 = Text("(V)", font_size=24, color=GREEN)
        label5.next_to(passos[4], RIGHT, buff=0.25)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)
        self.play(Write(label5))

        caixa5 = self.caixa(VGroup(passos[4], label5), cor=GREEN)
        self.play(Create(caixa5))
        self.wait(2)

        self._a2_formula = VGroup(passos[4].copy(), label5.copy(), caixa5.copy())
        self.limpar()
        self._a2_formula.scale(0.6).to_corner(UL, buff=0.3)
        self.add(self._a2_formula)

    # =========================================================
    # CENA 6 — Álgebra: diferença de quadrados → semiperímetro
    # =========================================================
    def _cena_algebra(self):
        titulo = Text("Fatorando com diferença de quadrados", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        linhas = VGroup(
            Text("4a²c² - (a²-b²+c²)²",                   font_size=23, color=BLUE),
            Text("P² - Q²  =  (P+Q)(P-Q)",                 font_size=22, color=GRAY),
            Text("P = 2ac  ,  Q = a²-b²+c²",               font_size=23),
            Text("= (2ac + a²-b²+c²)(2ac - a²+b²-c²)",    font_size=22),
            Text("= [(a+c)² - b²] · [b² - (a-c)²]",       font_size=22),
            Text("= (a+c+b)(a+c-b)(b+a-c)(b-a+c)",        font_size=22, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        linhas.next_to(titulo, DOWN, buff=0.35).to_edge(LEFT, buff=0.6)

        for l in linhas:
            self.play(Write(l))
            self.wait(0.45)

        div16 = Text(
            "A² = (a+b+c)(-a+b+c)(a-b+c)(a+b-c) / 16",
            font_size=22, color=GREEN
        )
        div16.next_to(linhas, DOWN, buff=0.28).to_edge(LEFT, buff=0.6)
        self.play(Write(div16))
        self.wait(1)

        semi_def = Text("Seja  p = (a+b+c)/2  (semiperímetro)", font_size=23, color=YELLOW)
        semi_def.next_to(div16, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)
        self.play(Write(semi_def))
        self.wait(1)

        equiv = VGroup(
            Text("(a+b+c) = 2p",      font_size=21),
            Text("(-a+b+c) = 2(p-a)", font_size=21),
            Text("(a-b+c) = 2(p-b)",  font_size=21),
            Text("(a+b-c) = 2(p-c)",  font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        equiv.next_to(semi_def, DOWN, buff=0.2).to_edge(LEFT, buff=0.6)
        self.play(LaggedStart(*[Write(e) for e in equiv], lag_ratio=0.3))
        self.wait(1.5)

        final_alg = Text(
            "A² = 16·p(p-a)(p-b)(p-c) / 16  =  p(p-a)(p-b)(p-c)",
            font_size=21, color=GREEN
        )
        final_alg.next_to(equiv, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)
        self.play(Write(final_alg))
        self.wait(1.5)

        simplif = Text("A² = p(p-a)(p-b)(p-c)", font_size=28, color=YELLOW)
        simplif.next_to(final_alg, DOWN, buff=0.25).to_edge(LEFT, buff=0.6)
        caixa_s = self.caixa(simplif, cor=YELLOW)
        self.play(Write(simplif), Create(caixa_s))
        self.wait(2)

        self._simplif_mob = VGroup(simplif.copy(), caixa_s.copy())
        self.limpar()
        self._simplif_mob.scale(0.65).to_corner(UL, buff=0.3)
        self.add(self._simplif_mob)

    # =========================================================
    # CENA 7 — Fórmula de Heron
    # =========================================================
    def _cena_resultado_heron(self):
        titulo = Text("Fórmula de Heron", font_size=42, color=YELLOW, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        heron   = Text("A = sqrt( p(p-a)(p-b)(p-c) )", font_size=38, color=WHITE)
        heron.move_to(ORIGIN + UP*0.5)
        caixa_h = self.caixa(heron, cor=YELLOW, buff=0.3)

        self.play(Write(heron))
        self.play(Create(caixa_h))
        self.play(Circumscribe(heron, color=YELLOW, run_time=1.5))

        obs = Text(
            "Permite calcular a área de qualquer triângulo\nconhecendo apenas os três lados.",
            font_size=24, color=GRAY, line_spacing=1.2
        )
        obs.next_to(caixa_h, DOWN, buff=0.45)
        self.play(FadeIn(obs, shift=DOWN*0.2))

        onde = VGroup(
            Text("onde:", font_size=22, color=BLUE),
            Text("a, b, c = medidas dos lados", font_size=22),
            Text("p = (a+b+c)/2  (semiperímetro)", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        onde.next_to(obs, DOWN, buff=0.35)
        self.play(FadeIn(onde))
        self.wait(3)

        self._heron_mob = VGroup(heron.copy(), caixa_h.copy())
        self.limpar()
        self._heron_mob.scale(0.55).to_corner(UR, buff=0.3)
        self.add(self._heron_mob)

    # =========================================================
    # CENA 8 — Exercício 37
    # =========================================================
    def _cena_exercicio37(self):
        titulo = Text("Exercício 37  (Unicamp-SP)", font_size=36, color=YELLOW, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        enunciado = VGroup(
            Text("Bandeira do Brasil — retângulo 2 m × 1,40 m", font_size=21),
            Text("Losango verde: vértices distam 17 cm dos lados.", font_size=21),
            Text("Círculo amarelo: raio = 35 cm.", font_size=21),
            Text("Usar pi ≈ 22/7  e  A = pi·r²", font_size=21, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        enunciado.next_to(titulo, DOWN, buff=0.3).to_edge(LEFT, buff=0.5)
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT*0.15) for e in enunciado], lag_ratio=0.25))
        self.wait(2)

        sep = Line(LEFT*5.5, RIGHT*5.5, stroke_width=1, color=GRAY)
        sep.next_to(enunciado, DOWN, buff=0.25)
        self.play(Create(sep))

        tit_a = Text("(a) Área pintada de verde", font_size=25, color=BLUE, weight=BOLD)
        tit_a.next_to(sep, DOWN, buff=0.2).to_edge(LEFT, buff=0.5)
        self.play(Write(tit_a))

        calc_a = VGroup(
            Text("Diagonais do losango:", font_size=22, color=YELLOW),
            Text("d1 = 200 - 2×17 = 166 cm", font_size=22),
            Text("d2 = 140 - 2×17 = 106 cm", font_size=22),
            Text("Área losango = (d1 × d2) / 2 = (166 × 106) / 2", font_size=22),
            Text("= 17596 / 2  =  8798 cm²", font_size=22, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
        calc_a.next_to(tit_a, DOWN, buff=0.2).to_edge(LEFT, buff=0.7)

        for c in calc_a:
            self.play(Write(c))
            self.wait(0.45)

        res_a = Text("Área verde = 8798 cm²", font_size=26, color=GREEN, weight=BOLD)
        res_a.next_to(calc_a, DOWN, buff=0.25).to_edge(LEFT, buff=0.5)
        cx_a  = self.caixa(res_a, cor=GREEN)
        self.play(Write(res_a), Create(cx_a))
        self.wait(2)

        self._res_a_mob = VGroup(res_a.copy(), cx_a.copy())
        self.limpar()
        self._res_a_mob.scale(0.65).to_corner(UL, buff=0.25)
        self.add(self._res_a_mob)
        self.add(self._heron_mob)

        tit_b = Text("(b) Porcentagem de verde", font_size=25, color=BLUE, weight=BOLD)
        tit_b.to_edge(UP).shift(DOWN*0.8).to_edge(LEFT, buff=0.5)
        self.play(Write(tit_b))

        calc_b = VGroup(
            Text("Área total do retângulo = 200 × 140 = 28000 cm²", font_size=21),
            Text("Área círculo = (22/7) × 35²", font_size=21, color=YELLOW),
            Text("= (22/7) × 1225 = 22 × 175 = 3850 cm²", font_size=21, color=GREEN),
            Text("Área verde = 8798 - 3850 = 4948 cm²", font_size=21, color=GREEN),
            Text("% verde = (4948 / 28000) × 100", font_size=21, color=YELLOW),
            Text("≈ 17,67%", font_size=28, color=GREEN, weight=BOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        calc_b.next_to(tit_b, DOWN, buff=0.25).to_edge(LEFT, buff=0.7)

        for c in calc_b:
            self.play(Write(c))
            self.wait(0.45)

        res_b = Text("Porcentagem verde ≈ 17,67%", font_size=26, color=GREEN, weight=BOLD)
        res_b.next_to(calc_b, DOWN, buff=0.25).to_edge(LEFT, buff=0.5)
        cx_b  = self.caixa(res_b, cor=GREEN)
        self.play(Write(res_b), Create(cx_b))
        self.wait(3)

        self.limpar()

        fim = VGroup(
            Text("Fim da apresentação", font_size=42, color=YELLOW, weight=BOLD),
            Text("Fórmula de Heron + Exercício 37", font_size=28, color=WHITE),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(fim, shift=UP*0.3))
        self.wait(3)
        self.play(FadeOut(fim))


# =============================================================
#  EXECUTAR NO CMD (dentro da pasta do projeto):
#
#  Teste rápido:   py -3.12 -m manim -pql heron.py FormulaHeron
#  Versão final:   py -3.12 -m manim -pqh heron.py FormulaHeron
# =============================================================