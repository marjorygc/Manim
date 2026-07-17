from manim import *
import numpy as np

class ExercicioCone(Scene):

    def caixa(self, mobject, cor=YELLOW, buff=0.18):
        return SurroundingRectangle(mobject, color=cor, buff=buff)

    def limpar(self):
        """Remove tudo da tela de uma vez."""
        self.play(*[FadeOut(m) for m in self.mobjects])

    # =========================================================
    def construct(self):
        self.camera.background_color = "#1a1a2e"
        self._cena_titulo()
        self._cena_enunciado()
        self._cena_interpretacao()
        self._cena_volume_agua()
        self._cena_volume_oleo()
        self._cena_momento_critico()
        self._cena_equacao_final()
        self._cena_resposta()

    # =========================================================
    # CENA 0 — Título
    # =========================================================
    def _cena_titulo(self):
        linha1 = Text("Exercício 10 (EsPCEx-SP)", font_size=44, color=YELLOW, weight=BOLD)
        linha2 = Text("Cone com água e óleo", font_size=32, color=WHITE)
        linha3 = Text("360º Matemática Fundamental — pág. 169", font_size=22, color=GRAY)
        grupo = VGroup(linha1, linha2, linha3).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(linha1, shift=UP*0.3))
        self.play(Write(linha2))
        self.play(FadeIn(linha3))
        self.wait(2)
        self.limpar()

    # =========================================================
    # CENA 1 — Enunciado e figura do cone
    # =========================================================
    def _cena_enunciado(self):
        titulo = Text("Enunciado", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        enunciado = Text(
            "Um recipiente cônico (vértice para baixo), com raio da base R e\n"
            "altura h, está completamente cheio de água e óleo. A superfície\n"
            "de contato entre os líquidos está inicialmente na metade da\n"
            "altura h. Abrindo a torneira no vértice até escoar toda a água e\n"
            "nenhum óleo, qual a altura do óleo medida a partir do vértice?",
            font_size=21, line_spacing=1.3
        )
        enunciado.next_to(titulo, DOWN, buff=0.35)
        self.play(FadeIn(enunciado, shift=UP*0.2))
        self.wait(3)

        self._cone_group = self._desenhar_cone(0.5)
        self._cone_group.scale(0.75).next_to(enunciado, DOWN, buff=0.4)
        self.play(Create(self._cone_group))
        self.wait(2)

        self.limpar()

    def _desenhar_cone(self, frac_interface):
        """Desenha o triângulo (secção do cone) com vértice para baixo,
        base R no topo, água embaixo e óleo em cima, interface na fração dada."""
        H = np.array([0, -2.2, 0])       # vértice (torneira)
        topoE = np.array([-2.0, 1.8, 0]) # canto esquerdo da base (topo)
        topoD = np.array([2.0, 1.8, 0])  # canto direito da base (topo)

        lado_esq = Line(H, topoE, color=WHITE, stroke_width=2.5)
        lado_dir = Line(H, topoD, color=WHITE, stroke_width=2.5)
        base = Line(topoE, topoD, color=WHITE, stroke_width=2.5)

        interfE = H + (topoE - H) * frac_interface
        interfD = H + (topoD - H) * frac_interface
        interface = DashedLine(interfE, interfD, color=BLUE, stroke_width=2.5)

        lR = Text("R", font_size=20).next_to(base, UP, buff=0.1)
        lH = Text("H", font_size=18, color=YELLOW).next_to(H, DOWN, buff=0.1)
        lh = Text("h", font_size=20, color=GRAY).next_to(VGroup(lado_esq), LEFT, buff=0.5)
        loleo = Text("óleo", font_size=20, color=ORANGE).move_to((topoE + topoD)/2 + DOWN*0.6)
        lagua = Text("água", font_size=20, color=BLUE).move_to((interfE + interfD)/2 + DOWN*0.7)

        seta = Line(np.array([-2.6, 1.8, 0]), np.array([-2.6, -2.2, 0]), color=GRAY, stroke_width=1.5)

        return VGroup(lado_esq, lado_dir, base, interface, lR, lH, lh, loleo, lagua, seta)

    # =========================================================
    # CENA 2 — Interpretação física do escoamento
    # =========================================================
    def _cena_interpretacao(self):
        titulo = Text("Interpretação física", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        cone = self._desenhar_cone(0.5).scale(0.65).to_edge(LEFT, buff=1.0)
        self.play(Create(cone))

        texto = VGroup(
            Text("A torneira fica no vértice, embaixo.", font_size=22),
            Text("A água é mais densa e está no fundo,", font_size=22),
            Text("logo é a água que sai primeiro, por inteiro.", font_size=22, color=BLUE),
            Text("Enquanto isso, o óleo permanece intacto,", font_size=22),
            Text("apenas descendo para ocupar o espaço.", font_size=22),
            Text("No instante em que a última gota de água sai,", font_size=22, color=YELLOW),
            Text("o cone contém só óleo — todo o óleo original.", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        texto.next_to(cone, RIGHT, buff=0.7).scale(0.9)
        self.play(LaggedStart(*[Write(t) for t in texto], lag_ratio=0.3))
        self.wait(3)

        self.limpar()

    # =========================================================
    # CENA 3 — Volume inicial de água
    # =========================================================
    def _cena_volume_agua(self):
        titulo = Text("Volume inicial de água", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Volume total do cone:  V = (1/3) . π . R² . h", font_size=24),
            Text("Na metade da altura (h/2), por semelhança de triângulos,", font_size=22, color=BLUE),
            Text("o raio da secção é R/2.", font_size=22, color=BLUE),
            Text("Vágua = (1/3) . π . (R/2)² . (h/2)", font_size=24),
            Text("Vágua = (1/3) . π . (R²/4) . (h/2) = (1/8) . (1/3) . π . R² . h", font_size=23),
            Text("Vágua = V / 8", font_size=28, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos.move_to(ORIGIN)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)

        cx = self.caixa(passos[5], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._v_agua = VGroup(passos[5].copy(), cx.copy())
        self.limpar()
        self._v_agua.scale(0.55).to_corner(UL, buff=0.3)
        self.add(self._v_agua)

    # =========================================================
    # CENA 4 — Volume inicial de óleo
    # =========================================================
    def _cena_volume_oleo(self):
        titulo = Text("Volume inicial de óleo", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("O óleo ocupa o restante do cone:", font_size=24),
            Text("Vóleo = V - Vágua = V - V/8", font_size=26),
            Text("Vóleo = (7/8) . V", font_size=30, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        passos.move_to(ORIGIN)

        for p in passos:
            self.play(Write(p))
            self.wait(0.7)

        cx = self.caixa(passos[2], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self._v_oleo = VGroup(passos[2].copy(), cx.copy())
        self.limpar()
        self._v_oleo.scale(0.55).to_corner(UL, buff=0.3)
        self._v_agua.next_to(self._v_oleo, DOWN, buff=0.2, aligned_edge=LEFT)
        self.add(self._v_agua, self._v_oleo)

    # =========================================================
    # CENA 5 — O momento crítico
    # =========================================================
    def _cena_momento_critico(self):
        titulo = Text("O instante em que só resta óleo", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        cone_antes = self._desenhar_cone(0.5).scale(0.55)
        cone_depois = self._desenhar_cone(1.0).scale(0.55)
        # remove o rótulo "água" do cone depois (não há mais água)
        cone_depois[8].set_opacity(0)

        seta = Text("→", font_size=36, color=WHITE)

        grupo = VGroup(cone_antes, seta, cone_depois).arrange(RIGHT, buff=0.8)
        grupo.next_to(titulo, DOWN, buff=0.5)

        self.play(Create(cone_antes))
        self.play(Write(seta))
        self.play(Create(cone_depois))
        self.wait(1)

        texto = Text(
            "Nesse instante, o cone de altura y (a partir do vértice)\n"
            "contém exatamente todo o volume de óleo original.",
            font_size=22, line_spacing=1.3, color=WHITE
        )
        texto.next_to(grupo, DOWN, buff=0.5)
        self.play(FadeIn(texto, shift=UP*0.2))
        self.wait(2.5)

        self.limpar()
        self.add(self._v_agua, self._v_oleo)

    # =========================================================
    # CENA 6 — Montando e resolvendo a equação
    # =========================================================
    def _cena_equacao_final(self):
        titulo = Text("Montando a equação", font_size=30, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))

        passos = VGroup(
            Text("Cone de óleo restante, altura y, raio (R.y/h):", font_size=22, color=BLUE),
            Text("Vy = (1/3) . π . (R.y/h)² . y  =  Vóleo", font_size=24),
            Text("(1/3) . π . R² . y³ / h² = (7/8) . (1/3) . π . R² . h", font_size=21),
            Text("y³ / h² = (7/8) . h", font_size=24),
            Text("y³ = (7/8) . h³", font_size=26, color=GREEN),
            Text("y = h . cuberoot(7/8) = h . cuberoot(7) / 2", font_size=27, color=GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
        passos.move_to(ORIGIN + DOWN*0.1)

        for p in passos:
            self.play(Write(p))
            self.wait(0.6)

        cx = self.caixa(passos[5], cor=GREEN)
        self.play(Create(cx))
        self.wait(2)

        self.limpar()

    # =========================================================
    # CENA 7 — Resposta final
    # =========================================================
    def _cena_resposta(self):
        titulo = Text("Resposta", font_size=36, color=YELLOW, weight=BOLD).to_edge(UP)
        self.play(Write(titulo))

        resultado = Text("y = ( ³√7 / 2 ) . h", font_size=42, color=WHITE)
        resultado.move_to(UP*0.5)
        cx = self.caixa(resultado, cor=YELLOW, buff=0.3)
        self.play(Write(resultado))
        self.play(Create(cx))
        self.play(Circumscribe(resultado, color=YELLOW, run_time=1.5))

        alternativa = Text("Alternativa correta: (a)", font_size=30, color=GREEN, weight=BOLD)
        alternativa.next_to(resultado, DOWN, buff=0.6)
        self.play(Write(alternativa))
        self.wait(3)

        self.limpar()

        fim = VGroup(
            Text("Fim da resolução", font_size=42, color=YELLOW, weight=BOLD),
            Text("Exercício 10 — EsPCEx-SP", font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.5).move_to(ORIGIN)
        self.play(FadeIn(fim, shift=UP*0.3))
        self.wait(3)
        self.play(FadeOut(fim))


# =============================================================
#  EXECUTAR NO CMD (dentro da pasta do projeto):
#
#  Teste rápido:   py -3.12 -m manim -pql cone_espcex.py ExercicioCone
#  Versão final:   py -3.12 -m manim -pqh cone_espcex.py ExercicioCone
# =============================================================