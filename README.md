# Trabalho Computacional — Matemática 4

**Aluna:** Marjory Gonçalves Cardoso  
**Matéria:** Matemática 4 · 1º Bimestre · 2025  
**Ferramenta:** [Manim](https://www.manim.community/) — biblioteca de animação matemática para Python

---

## Conteúdo

**(i) Dedução da Fórmula de Heron**  
Animação completa da dedução partindo do Teorema de Pitágoras, passando pelas fórmulas intermediárias I a V, fatoração por diferença de quadrados e introdução do semiperímetro.

**(ii) Exercício 37 — Pág. 457**  
Livro *360° Matemática Fundamental: Uma Nova Abordagem — Parte II*.  
Cálculo da área do losango verde da bandeira, área do círculo amarelo com π ≈ 22/7 e porcentagem de verde em relação ao retângulo total.

---

## Como executar

**Requisitos:** Python 3.12 · Manim instalado

```bash
# 1. Criar e ativar ambiente virtual
python -m venv .venv
.venv\Scripts\activate

# 2. Instalar o Manim
pip install manim

# 3. Rodar a animação (qualidade baixa — teste rápido)
py -3.12 -m manim -pql heron.py FormulaHeron

# 4. Rodar em qualidade média (entrega)
py -3.12 -m manim -pqm heron.py FormulaHeron
```

O vídeo gerado será salvo em:
```
media/videos/heron/480p15/FormulaHeron.mp4  ← qualidade baixa
media/videos/heron/720p30/FormulaHeron.mp4  ← qualidade média
```

---

## Arquivos

| Arquivo | Descrição |
|---|---|
| `heron.py` | Código completo da animação |
| `README.md` | Este arquivo |

---

## Estrutura da animação

| Cena | Conteúdo |
|---|---|
| 0 | Tela de abertura |
| 1 | Triângulo ABC com altura h |
| 2 | Pitágoras — equações I e II |
| 3 | Isolamento de x — fórmula III |
| 4 | Cálculo de h² — fórmula IV |
| 5 | Área ao quadrado — fórmula V |
| 6 | Fatoração e semiperímetro p |
| 7 | Fórmula de Heron |
| 8 | Exercício 37 |
