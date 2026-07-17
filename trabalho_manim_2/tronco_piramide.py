from manim import *
import numpy as np

class VolumeTroncoPiramide(Scene):

    def caixa(self, mobject, cor=YELLOW, buff=0.18):
        return SurroundingRectangle(mobject, color=cor, buff=buff)

    def limpar(self):
        """Remove tudo da tela de uma vez."""
        self.play(*[FadeOut(m) for m in self.mobjects])

    # =========================================================
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self._cena_titulo()
        self._cena_secao_transversal()
        self._cena_tronco_definicao()
        self._cena_semelhanca()
        self._cena_razao_areas_volumes()
        self._cena_formula1()
        self._cena_formula2()
        self._cena_formula3()
        self._cena_combinacao()
        self._cena_diferenca_cubos()
        self._cena_resultado_final()
        self._cena_exemplo_pucsp()

    # =========================================================
    # CENA 0 — Título
    # =========================================================
    def _cena_titulo(self):
        linha1 = Text("Volume do Tronco de Pirâmide", font_size=46, color=YELLOW, weight=BOLD)
        linha2 = Text("Dedução completa", font_size=32, color=WHITE)
        linha3 = Text("A partir da relação de semelhança entre pirâmides", font_size=22, color=GRAY)
        grupo = VGroup(linha1, linha2, linha3).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(linha1, shift=UP*0.3))
        self.play(Write(linha2))
        self.play(FadeIn(linha3))
        self.wait(2)
        self.limpar()

    # =========================================================
    # CENA 1 — Secção transversal: S1 = S2
    # =========================================================
    def _cena_secao_transversal(self):
        titulo = Text("Secções transversais equidistantes do vértice", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        def piramide(pos, escala_topo, label_topo, label_base):
            V = np.array([0, 2.0, 0])
            B1 = np.array([-1.6, -1.6, 0])
            B2 = np.array([1.6, -1.6, 0])
            base = Polygon(B1, B2, B1 + np.array([0.5, -0.4, 0]), color=WHITE, stroke_width=2.2)
            lat1 = Line(V, B1, color=WHITE, stroke_width=2.2)
            lat2 = Line(V, B2, color=WHITE, stroke_width=2.2)
            T1 = V + (B1 - V) * escala_topo
            T2 = V + (B2 - V) * escala_topo
            secao = DashedLine(T1, T2, color=GREEN, stroke_width=3)
            grupo = VGroup(base, lat1, lat2, secao)
            grupo.scale(0.85).move_to(pos)
            return grupo

        p1 = piramide(LEFT*3.2, 0.45, "S1", "Sb")
        p2 = piramide(RIGHT*3.2, 0.45, "S2", "Sb")

        self.play(Create(p1), Create(p2))
        self.wait(1)

        formula = Text("Se Sb = Sb  e  h = h  →  S1 = S2", font_size=26, color=GREEN)
        formula.next_to(VGroup(p1, p2), DOWN, buff=0.6)
        self.play(Write(formula))
        self.wait(2)

        obs = Text(
            "Duas pirâmides com mesma área de base e mesma altura têm\nsecções transversais iguais quando equidistantes do vértice.",
            font_size=22, color=GRAY, line_spacing=1.2
        )
        obs.next_to(formula, DOWN, buff=0.35)
        self.play(FadeIn(obs, shift=DOWN*0.2))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 2 — Definição de tronco de pirâmide
    # =========================================================
    def _cena_tronco_definicao(self):
        titulo = Text("Tronco de Pirâmide", font_size=34, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        V = np.array([0, 2.6, 0])
        A = np.array([-2.2, -2.0, 0])
        D = np.array([2.2, -2.0, 0])
        Ap = V + (A - V) * 0.42
        Dp = V + (D - V) * 0.42

        base_maior = Line(A, D, color=WHITE, stroke_width=2.5)
        lat_esq = Line(V, A, color=WHITE, stroke_width=2.5)
        lat_dir = Line(V, D, color=WHITE, stroke_width=2.5)
        base_menor = DashedLine(Ap, Dp, color=GREEN, stroke_width=3)

        lV = Text("V", font_size=24).next_to(V, UP, buff=0.1)
        lA = Text("A", font_size=22).next_to(A, DL, buff=0.1)
        lD = Text("D", font_size=22).next_to(D, DR, buff=0.1)
        lAp = Text("A'", font_size=20, color=GREEN).next_to(Ap, LEFT, buff=0.1)
        lDp = Text("D'", font_size=20, color=GREEN).next_to(Dp, RIGHT, buff=0.1)

        seta_h = DoubleArrow(V + RIGHT*3.0, np.array([3.0, A[1], 0]), color=BLUE, buff=0, stroke_width=2)
        lh = Text("h", font_size=22, color=BLUE).next_to(seta_h, RIGHT, buff=0.1)
        seta_d = DoubleArrow(V + RIGHT*3.0, np.array([3.0, Ap[1], 0]), color=ORANGE, buff=0, stroke_width=2)
        ld = Text("d", font_size=22, color=ORANGE).next_to(seta_d, RIGHT, buff=0.1).shift(UP*0.15)

        figura = VGroup(base_maior, lat_esq, lat_dir, base_menor, lV, lA, lD, lAp, lDp, seta_h, lh, seta_d, ld)

        self.play(Create(lat_esq), Create(lat_dir), Create(base_maior))
        self.play(Write(lV), Write(lA), Write(lD))
        self.play(Create(base_menor), Write(lAp), Write(lDp))
        self.play(Create(seta_h), Write(lh))
        self.play(Create(seta_d), Write(ld))
        self.wait(1.5)

        texto = VGroup(
            Text("O plano paralelo à base separa a pirâmide em duas partes:", font_size=22),
            Text("a pirâmide menor (topo) e o tronco de pirâmide (base).", font_size=22),
            Text("k = h - d  é a altura do tronco.", font_size=24, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        texto.to_edge(LEFT, buff=0.6).shift(DOWN*2.6)
        self.play(FadeIn(texto, shift=UP*0.2))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 3 — Relações de semelhança
    # =========================================================
    def _cena_semelhanca(self):
        titulo = Text("Relações de semelhança", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        texto = Text(
            "As pirâmides VA'D' (menor) e VAD (maior) são semelhantes.\nAs arestas laterais são proporcionais às alturas:",
            font_size=24, line_spacing=1.3
        )
        texto.next_to(titulo, DOWN, buff=0.5)
        self.play(Write(texto))

        razao1 = Text("VA' / VA  =  VD' / VD  =  d / h", font_size=27, color=GREEN)
        razao1.next_to(texto, DOWN, buff=0.5)
        self.play(Write(razao1))
        self.wait(1)

        texto2 = Text("O mesmo vale para as arestas da base:", font_size=22)
        texto2.next_to(razao1, DOWN, buff=0.4)
        self.play(Write(texto2))

        razao2 = Text("A'D' / AD  =  d / h", font_size=27, color=GREEN)
        razao2.next_to(texto2, DOWN, buff=0.35)
        self.play(Write(razao2))

        cx = self.caixa(VGroup(razao1, razao2), cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 4 — Razão entre áreas e volumes
    # =========================================================
    def _cena_razao_areas_volumes(self):
        titulo = Text("Razão entre áreas e entre volumes", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Razão entre áreas (quadrado da razão de semelhança):", font_size=21, color=BLUE),
            Text("Sb / SB = (d / h)²", font_size=26),
            Text("Razão entre volumes:", font_size=21, color=BLUE),
            Text("Vp' / Vp = [(1/3).Sb.d] / [(1/3).SB.h]", font_size=23),
            Text("Vp' / Vp = (d/h)² . (d/h)", font_size=23),
            Text("Vp' / Vp = (d / h)³", font_size=27, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos.move_to(ORIGIN)

        for p in passos:
            self.play(Write(p))
            self.wait(0.5)

        cx = self.caixa(passos[5], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 5 — Fórmula (1): volume do tronco por subtração
    # =========================================================
    def _cena_formula1(self):
        titulo = Text("Volume do tronco = pirâmide maior - pirâmide menor", font_size=26, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Vtronco = Vpirâmide maior - Vpirâmide menor", font_size=24),
            Text("Vpirâmide maior = (1/3) . SB . h", font_size=24),
            Text("Vpirâmide menor = (1/3) . Sb . (h - k) = (1/3) . Sb . d", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        passos.move_to(ORIGIN + UP*0.3)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)

        resultado = Text("Vtronco = (1/3) . ( SB . h - Sb . d )      (I)", font_size=26, color=GREEN)
        resultado.next_to(passos, DOWN, buff=0.5)
        self.play(Write(resultado))
        cx = self.caixa(resultado, cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._formula1 = VGroup(resultado.copy(), cx.copy())
        self.limpar()
        self._formula1.scale(0.55).to_corner(UL, buff=0.3)
        self.add(self._formula1)

    # =========================================================
    # CENA 6 — Fórmula (2): isolando d
    # =========================================================
    def _cena_formula2(self):
        titulo = Text("Isolando d  →  fórmula (II)", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Sb / SB = (d / h)²  →  d / h = sqrt(Sb) / sqrt(SB)", font_size=24),
            Text("Como h = d + k, substituindo:", font_size=22, color=BLUE),
            Text("d . sqrt(SB) = (d + k) . sqrt(Sb)", font_size=24),
            Text("d . ( sqrt(SB) - sqrt(Sb) ) = k . sqrt(Sb)", font_size=24),
            Text("d = k . sqrt(Sb) / ( sqrt(SB) - sqrt(Sb) )", font_size=27, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        passos.move_to(ORIGIN + DOWN*0.1)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)

        cx = self.caixa(passos[4], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._formula2 = VGroup(passos[4].copy(), cx.copy())
        self.limpar()
        self._formula2.scale(0.55).to_corner(UL, buff=0.3)
        self._formula1.scale(1).next_to(self._formula2, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(self._formula1, self._formula2)

    # =========================================================
    # CENA 7 — Fórmula (3): altura h da pirâmide maior
    # =========================================================
    def _cena_formula3(self):
        titulo = Text("Encontrando h  →  fórmula (III)", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("h = d + k, substituindo (II):", font_size=22, color=BLUE),
            Text("h = k.sqrt(Sb)/(sqrt(SB)-sqrt(Sb)) + k", font_size=24),
            Text("h = [ k.sqrt(Sb) + k.sqrt(SB) - k.sqrt(Sb) ] / (sqrt(SB)-sqrt(Sb))", font_size=22),
            Text("h = k . sqrt(SB) / ( sqrt(SB) - sqrt(Sb) )", font_size=27, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        passos.move_to(ORIGIN + DOWN*0.1)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)

        cx = self.caixa(passos[3], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._formula3 = VGroup(passos[3].copy(), cx.copy())
        self.limpar()
        self._formula3.scale(0.55).to_corner(UL, buff=0.3)
        self._formula2.next_to(self._formula3, DOWN, buff=0.15, aligned_edge=LEFT)
        self._formula1.next_to(self._formula2, DOWN, buff=0.15, aligned_edge=LEFT)
        self.add(self._formula1, self._formula2, self._formula3)

    # =========================================================
    # CENA 8 — Combinando (I), (II) e (III)
    # =========================================================
    def _cena_combinacao(self):
        titulo = Text("Combinando (I), (II) e (III)", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Vtronco = (1/3).(SB.h - Sb.d)", font_size=23),
            Text("= (1/3).[ SB.(k.sqrt(SB)/(sqrt(SB)-sqrt(Sb))) - Sb.(k.sqrt(Sb)/(sqrt(SB)-sqrt(Sb))) ]", font_size=18),
            Text("= (k/3) . [ (sqrt(SB))³ - (sqrt(Sb))³ ] / ( sqrt(SB) - sqrt(Sb) )", font_size=23, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        passos.move_to(ORIGIN)

        for p in passos:
            self.play(Write(p))
            self.wait(0.7)

        cx = self.caixa(passos[2], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._combinada = VGroup(passos[2].copy(), cx.copy())
        self.limpar()
        self._combinada.scale(0.55).to_corner(UR, buff=0.3)
        self.add(self._combinada)

    # =========================================================
    # CENA 9 — Diferença de dois cubos
    # =========================================================
    def _cena_diferenca_cubos(self):
        titulo = Text("Diferença de dois cubos", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        identidade = Text("x³ - y³ = (x - y) . (x² + xy + y²)", font_size=28, color=BLUE)
        identidade.move_to(UP*1.2)
        cx0 = self.caixa(identidade, cor=BLUE)
        self.play(Write(identidade), Create(cx0))
        self.wait(1)

        passos = VGroup(
            Text("Fazendo x = sqrt(SB)  e  y = sqrt(Sb):", font_size=23),
            Text("(sqrt(SB))³-(sqrt(Sb))³ = (sqrt(SB)-sqrt(Sb)) . (SB + sqrt(SB.Sb) + Sb)", font_size=21, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        passos.next_to(identidade, DOWN, buff=0.7)

        for p in passos:
            self.play(Write(p))
            self.wait(0.7)
        self.wait(2)

        self.limpar()
        self.add(self._combinada)

    # =========================================================
    # CENA 10 — Resultado final: cancelamento e fórmula do volume
    # =========================================================
    def _cena_resultado_final(self):
        titulo = Text("Simplificando: o termo comum se cancela", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Vtronco = (k/3) . [(sqrt(SB)-sqrt(Sb)).(SB+sqrt(SB.Sb)+Sb)] / (sqrt(SB)-sqrt(Sb))", font_size=19),
            Text("(sqrt(SB) - sqrt(Sb)) cancela em cima e embaixo", font_size=20, color=RED),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        passos.move_to(UP*0.6)

        self.play(Write(passos[0]))
        self.wait(0.8)
        self.play(FadeIn(passos[1]))
        self.wait(1.5)

        final = Text("Vtronco = (k/3) . ( SB + sqrt(SB . Sb) + Sb )", font_size=34, color=WHITE)
        final.next_to(passos, DOWN, buff=0.6)
        cx = self.caixa(final, cor=YELLOW, buff=0.3)
        self.play(Write(final))
        self.play(Create(cx))
        self.play(Circumscribe(final, color=YELLOW, run_time=1.5))

        onde = VGroup(
            Text("onde:", font_size=20, color=BLUE),
            Text("SB = área da base maior,  Sb = área da base menor", font_size=20),
            Text("k = altura do tronco", font_size=20),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        onde.next_to(final, DOWN, buff=0.4)
        self.play(FadeIn(onde))
        self.wait(3)

        self._formula_final = VGroup(final.copy(), cx.copy())
        self.limpar()
        self._formula_final.scale(0.5).to_corner(UR, buff=0.3)
        self.add(self._formula_final)

    # =========================================================
    # CENA 11 — Exemplo de aplicação (PUC-SP)
    # =========================================================
    def _cena_exemplo_pucsp(self):
        titulo = Text("Aplicação: Exemplo (PUC-SP)", font_size=32, color=YELLOW, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        enunciado = Text(
            "Um tronco de pirâmide de bases quadradas tem 2814 cm³ de volume.\n"
            "A altura do tronco mede 18 cm e o lado do quadrado da base maior\n"
            "mede 20 cm. Qual o lado do quadrado da base menor?",
            font_size=22, line_spacing=1.25
        )
        enunciado.next_to(titulo, DOWN, buff=0.4)
        self.play(FadeIn(enunciado, shift=UP*0.2))
        self.wait(2)

        calc = VGroup(
            Text("SB = 20² = 400 cm²          Sb = L²", font_size=22),
            Text("2814 = (18/3) . [400 + sqrt(400.L²) + L²]", font_size=22),
            Text("L² + 20L - 69 = 0", font_size=24, color=BLUE),
            Text("L' = 3   ou   L'' = -23 (não convém)", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        calc.next_to(enunciado, DOWN, buff=0.5).to_edge(LEFT, buff=0.7)

        for c in calc:
            self.play(Write(c))
            self.wait(0.6)

        resultado = Text("Lado da base menor = 3 cm", font_size=28, color=GREEN, weight=BOLD)
        resultado.next_to(calc, DOWN, buff=0.4).to_edge(LEFT, buff=0.7)
        cx = self.caixa(resultado, cor=GREEN)
        self.play(Write(resultado), Create(cx))
        self.wait(3)

        self.limpar()

        fim = VGroup(
            Text("Fim da apresentação", font_size=42, color=YELLOW, weight=BOLD),
            Text("Dedução do Volume do Tronco de Pirâmide", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(fim, shift=UP*0.3))
        self.wait(3)
        self.play(FadeOut(fim))


# =============================================================
#  EXECUTAR NO CMD (dentro da pasta do projeto):
#
#  Teste rápido:   py -3.12 -m manim -pql tronco_piramide.py VolumeTroncoPiramide
#  Versão final:   py -3.12 -m manim -pqh tronco_piramide.py VolumeTroncoPiramide
# =============================================================