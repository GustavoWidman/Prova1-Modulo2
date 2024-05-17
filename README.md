# Prova2-Modulo1 - Gustavo Wagon Widman

## Descrição

Esse repositório contém a implementação de um sistema de controle do turtlesim do ROS2 via CLI, implementando uma deque de movimentos FIFO, gradualmente consumida pelo node que controla o turtlesim.

## Instalação e execução

### Para instalar as dependências do projeto, comece clonando o repositório

```bash
git clone https://github.com/GustavoWidman/Prova1-Modulo2.git
```

### Depois, entre na pasta do projeto, e crie um ambiente virtual (venv)

```bash
cd Prova2-Modulo1
```

```bash
python -m venv venv
```

OU (usando [uv](https://github.com/astral-sh/uv))

```bash
uv venv venv
```

### Ative o ambiente virtual com o seguinte comando

```bash
source venv/bin/activate
```

OU (no Windows)

```bash
.\venv\Scripts\activate
```

### Finalmente, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

OU (usando [uv](https://github.com/astral-sh/uv))

```bash
uv pip install -r requirements.txt
```

### Para rodar o projeto, primeiro execute o node:

```bash
python node.py
```

### E depois execute a CLI da maneira desejada:

```bash
python cli.py --help
```

## Estrutura do projeto

A estrutura do projeto é composta por pastas e arquivos que organizam os comandos, classes e utilitários. Segue abaixo a estrutura do projeto, resultado do comando `tree --gitignore`

```bash
.
├── cli.py
├── node.py
├── README.md
└── requirements.txt
```

## Utilizacao da CLI

Exemplo:

```bash
python cli.py --vx 0.0 --vy 1.0 --vt 0.0 -t 1000
```

Para mais informações, use o comando `python cli.py --help`

## Demonstracao

![image](https://github.com/GustavoWidman/Prova1-Modulo2/assets/123963822/f51c0a1f-2274-4c41-b861-72c5c7ae81d7)

(Infelizmente nao deu tempo de eu rodar o turtlesim node por causa de uma complicacao tecnica mas confia que funciona 👍)

## Dependências

- Typer 0.12.3
- Numpy 1.26.4
