# 📐 Trabalho Computacional — Matemática 4

**Aluna:** Marjory Gonçalves Cardoso  
**Disciplina:** Matemática 4   
**Ferramenta utilizada:** Manim Community Edition (Python)

---

# 📖 Sobre o projeto

Este repositório reúne os trabalhos computacionais desenvolvidos para a disciplina de Matemática 4 utilizando a biblioteca **Manim**, responsável pela criação de animações matemáticas em Python.

As duas entregas foram mantidas no mesmo repositório para aproveitar toda a estrutura já configurada na primeira entrega, incluindo ambiente virtual, dependências e organização do projeto.

---

# 📂 Conteúdo do repositório

## ✅ Primeira entrega

### (i) Dedução da Fórmula de Heron

Animação completa da dedução da Fórmula de Heron partindo do Teorema de Pitágoras, passando pelas fórmulas intermediárias, fatoração por diferença de quadrados e introdução do semiperímetro.

### (ii) Exercício 37 — Página 457

Livro **360º Matemática Fundamental – Parte II**

Resolução utilizando animação para calcular:

- área do losango verde da bandeira;
- área do círculo amarelo utilizando π ≈ 22/7;
- porcentagem da área verde em relação à área total da bandeira.

---

## ✅ Segunda entrega

### (i) Dedução da fórmula do volume do tronco de pirâmide

Animação mostrando toda a dedução da fórmula do volume do tronco de pirâmide utilizando:

- conceito de seção transversal;
- definição do tronco de pirâmide;
- semelhança entre pirâmides;
- razão entre áreas e volumes;
- fórmulas intermediárias;
- fatoração por diferença de cubos;
- obtenção da fórmula final;
- exemplo de aplicação.

---

### (ii) Exercício 10 — Página 169

Livro **360º Matemática Fundamental**

Resolução do problema envolvendo um recipiente cônico contendo água e óleo.

A animação apresenta:

- interpretação física do problema;
- utilização da semelhança entre triângulos;
- cálculo do volume da água;
- cálculo do volume do óleo;
- montagem da equação;
- obtenção da resposta final.

---

# 📁 Organização do projeto

```
📦 Projeto
│
├── heron.py
├── tronco_piramide.py
├── cone_espcex.py
├── media/
├── .venv/
└── README.md
```

### Arquivos principais

| Arquivo | Descrição |
|----------|-----------|
| `heron.py` | Dedução da Fórmula de Heron e Exercício 37 |
| `tronco_piramide.py` | Dedução da fórmula do volume do tronco de pirâmide |
| `cone_espcex.py` | Resolução do Exercício 10 |
| `README.md` | Documentação do projeto |

---

# ▶️ Como executar

## Requisitos

- Python 3.12
- Manim Community Edition

---

## Criar o ambiente virtual

```bash
python -m venv .venv
```

### Ativar o ambiente

Windows

```bash
.venv\Scripts\activate
```

---

## Instalar o Manim

```bash
pip install manim
```

---

# Executando as animações

## Primeira entrega — Fórmula de Heron

Teste rápido

```bash
py -3.12 -m manim -pql heron.py FormulaHeron
```

Maior qualidade

```bash
py -3.12 -m manim -pqm heron.py FormulaHeron
```

---

## Segunda entrega — Tronco de Pirâmide

Teste rápido

```bash
py -3.12 -m manim -pql tronco_piramide.py VolumeTroncoPiramide
```

Maior qualidade

```bash
py -3.12 -m manim -pqh tronco_piramide.py VolumeTroncoPiramide
```

---

## Segunda entrega — Exercício do Cone

Teste rápido

```bash
py -3.12 -m manim -pql cone_espcex.py ExercicioCone
```

Maior qualidade

```bash
py -3.12 -m manim -pqh cone_espcex.py ExercicioCone
```

---

# 📹 Arquivos gerados

As animações renderizadas são salvas automaticamente na pasta **media/videos**, organizada pelo próprio Manim.

---

# 🎯 Objetivo

O objetivo dos trabalhos é utilizar recursos visuais para facilitar a compreensão de demonstrações matemáticas e da resolução de problemas, tornando o raciocínio mais intuitivo por meio de animações.

---

# 📝 Observações

Durante a gravação dos vídeos de apresentação foram utilizadas versões das animações previamente renderizadas.

Essa escolha foi feita porque o processo de renderização do Manim pode levar alguns minutos, dependendo da complexidade da animação e do desempenho do computador, o que tornaria a apresentação excessivamente longa.

---

# 📧 Contato

Caso ocorra qualquer dificuldade para acessar os arquivos ou executar o projeto, fico à disposição para prestar esclarecimentos.
