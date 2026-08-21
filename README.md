# 📁 Organizador de Arquivos

Automação desenvolvida em Python para organizar arquivos automaticamente de acordo com suas extensões, utilizando `pathlib` e `shutil`.

O projeto nasceu de uma **necessidade real do meu dia a dia**: manter organizada uma pasta pessoal que utilizo constantemente. Com o tempo, a organização manual dos arquivos passou a consumir uma parte considerável da minha rotina, principalmente quando diferentes tipos de documentos, imagens, planilhas, vídeos e outros arquivos se acumulavam no mesmo diretório.

Em vez de continuar realizando essa tarefa manualmente, decidi transformar o problema em uma oportunidade para aplicar meus conhecimentos de Python e criar uma solução própria.

> 🚀 **Versão atual: v1.0.0**

---

## 💡 O problema que deu origem ao projeto

Todos os dias, novos arquivos eram adicionados à minha pasta pessoal e, eventualmente, eu precisava parar o que estava fazendo para organizar tudo manualmente.

O processo era simples, mas repetitivo:

```text
Arquivo → identificar o tipo → criar/encontrar a pasta → mover → repetir
```

Quando realizado manualmente diversas vezes, esse processo acabava consumindo tempo que poderia ser utilizado em outras atividades.

Foi a partir desse problema que surgiu a ideia:

> **"Se eu faço a mesma tarefa repetidamente, por que não automatizá-la?"**

A partir disso, desenvolvi o **Organizador de Arquivos**, uma aplicação capaz de identificar automaticamente os arquivos e direcioná-los para suas respectivas pastas.

Em uma **estimativa baseada na minha utilização diária**, a automação reduziu em aproximadamente **70% o tempo que eu gastava com essa tarefa de organização manual**.

O objetivo não era apenas criar um exercício de Python, mas desenvolver uma solução que eu realmente pudesse utilizar no meu cotidiano.

---

## 🎯 Sobre o projeto

O **Organizador de Arquivos** é uma aplicação de terminal capaz de identificar arquivos presentes em um diretório e organizá-los automaticamente em pastas de acordo com seus formatos.

Por exemplo:

```text
Download/
│
├── PDF/
│   ├── contrato.pdf
│   └── aulas_python.pdf
│
├── DOCX/
│   └── relatorio.docx
│
├── JPG/
│   └── foto_ferias.jpg
│
├── PNG/
│   └── logo.png
│
├── MP3/
│   └── musica.mp3
│
└── Outros/
    └── arquivo.xyz
```

Além da organização automática, o programa apresenta um relatório operacional no terminal informando a quantidade de arquivos processados, movimentados e excluídos.

---

## 🧠 Do problema à solução

O desenvolvimento seguiu uma lógica simples:

```text
Problema real
     ↓
Identificação da tarefa repetitiva
     ↓
Análise do processo manual
     ↓
Automação com Python
     ↓
Tratamento de possíveis erros
     ↓
Interface e relatório
     ↓
Solução funcional
```

Esse processo foi importante para mim porque permitiu transformar conceitos estudados durante minha jornada de aprendizado em uma ferramenta que resolve uma necessidade que realmente fazia parte da minha rotina.

---

## 🎯 Objetivo

O objetivo inicial do projeto foi praticar conceitos fundamentais de automação de arquivos utilizando Python.

Durante o desenvolvimento, o projeto evoluiu para incluir:

* Manipulação de arquivos e diretórios;
* Criação automática de pastas;
* Identificação de extensões;
* Movimentação de arquivos;
* Verificação de arquivos duplicados;
* Tratamento de exceções;
* Contadores de operações;
* Interface de terminal;
* Barra de progresso;
* Relatório operacional.

O projeto foi encerrado na versão `v1.0.0` após cumprir o objetivo de estudo proposto e, principalmente, entregar uma solução funcional para um problema real do meu cotidiano.

---

## ⚙️ Funcionalidades

### 📂 Organização automática

Os arquivos são classificados de acordo com sua extensão e enviados para suas respectivas pastas.

Exemplo:

```text
.pdf → PDF
.docx → DOCX
.xlsx → XLSX
.jpg → JPG
.png → PNG
.py → PY
.mp4 → MP4
.mp3 → MP3
```

---

### 📦 Pasta "Outros"

Arquivos que não possuem uma extensão previamente cadastrada são direcionados automaticamente para a pasta `Outros`.

Exemplo:

```text
arquivo.xyz
arquivo_sem_extensao
```

---

### ♻️ Tratamento de arquivos duplicados

Antes de realizar uma movimentação, o programa verifica se já existe um arquivo com o mesmo nome no destino.

Quando um arquivo duplicado é identificado, ele é tratado de acordo com a lógica definida no projeto e contabilizado no relatório final.

---

### ⚠️ Tratamento de erros

O projeto utiliza tratamento de exceções para lidar com possíveis problemas durante a manipulação dos arquivos.

Entre os erros considerados estão:

```text
FileNotFoundError
FileExistsError
PermissionError
IsADirectoryError
NotADirectoryError
```

O objetivo é evitar que uma falha em uma operação interrompa inesperadamente todo o processo.

---

### 📊 Relatório operacional

Ao final da execução, o programa apresenta um relatório contendo informações como:

```text
Arquivos Processados
Arquivos Movidos
Arquivos em Outros
Arquivos Excluídos
Arquivos com Erro
```

---

### 🎨 Interface de terminal

A interface utiliza a biblioteca `Rich` para melhorar a visualização das informações no terminal.

Entre os recursos utilizados estão:

* `Panel`
* `Table`
* `Progress`
* Formatação de texto
* Cores
* Barra de progresso

---

## 🛠️ Tecnologias utilizadas

### Linguagem

* **Python**

### Bibliotecas

* `pathlib`
* `shutil`
* `time`
* `rich`

### Ferramentas

* Git
* GitHub
* Visual Studio Code

---

## 📚 Principais conceitos praticados

Durante o desenvolvimento foram praticados conceitos importantes de Python:

* Variáveis;
* Listas;
* Dicionários;
* Estruturas condicionais;
* Loops `for`;
* Funções;
* `try/except`;
* Manipulação de exceções;
* `pathlib.Path`;
* Criação de diretórios;
* Criação de arquivos;
* Movimentação de arquivos;
* Exclusão de arquivos;
* Verificação de existência;
* Extensões de arquivos;
* Modularização de lógica;
* Interface de terminal.

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/viana7771/organizador-downloads
```

### 2. Entre na pasta do projeto

```bash
cd organizador_download
```

### 3. Crie e ative o ambiente virtual

No Windows:

```bash
python -m venv .venv
```

Ativação:

```bash
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install rich
```

### 5. Execute o projeto

```bash
python C:\Users\kaire\OneDrive\Área de Trabalho\organizador_download\organizador_download.py
```

---

## 📋 Exemplo do fluxo

O funcionamento básico do programa segue esta lógica:

```text
Arquivos
    ↓
Identificação da extensão
    ↓
Verificação da categoria
    ↓
Criação da pasta de destino
    ↓
Verificação de duplicidade
    ↓
Movimentação do arquivo
    ↓
Contabilização da operação
    ↓
Relatório final
```

---

## 📈 Resultado

O projeto permitiu transformar um problema cotidiano em uma solução automatizada.

Além de reduzir o tempo gasto com uma tarefa repetitiva, o desenvolvimento permitiu consolidar conhecimentos de Python e entender melhor como transformar uma necessidade real em uma aplicação funcional.

O principal resultado para mim não foi apenas o programa funcionar.

Foi perceber que conceitos que antes estavam sendo estudados de forma isolada — como `pathlib`, `shutil`, estruturas condicionais, loops, exceções e bibliotecas externas — poderiam ser combinados para resolver um problema que fazia parte da minha própria rotina.

### ⏱️ Impacto na rotina

Com base na minha utilização e em uma estimativa do tempo que eu costumava gastar realizando essa organização manualmente, considero que a automação proporcionou uma redução de aproximadamente **70% no tempo dedicado à tarefa**.

> **70% menos tempo organizando arquivos manualmente.
> Mais tempo dedicado ao que realmente importa.**

Essa estimativa representa minha experiência prática com a ferramenta e não uma medição controlada de produtividade.

---

## 🔮 Possíveis melhorias futuras

O projeto foi encerrado na versão `v1.0.0`, mas algumas funcionalidades poderiam ser implementadas futuramente:

* Configuração das categorias através de arquivo externo;
* Interface gráfica;
* Logs em arquivo;
* Modo de simulação antes da movimentação;
* Configuração personalizada das pastas;
* Histórico das operações;
* Testes automatizados;
* Sistema mais completo de gerenciamento de erros.

Essas funcionalidades não fazem parte do escopo da versão `v1.0.0`.

---

## 📌 Status

**Concluído — v1.0.0**

Projeto desenvolvido para fins de estudo, automação pessoal e portfólio.

O projeto nasceu de uma necessidade real do meu cotidiano e foi desenvolvido com o objetivo de transformar uma tarefa manual e repetitiva em um processo automatizado.

---

## 👨‍💻 Autor

**Kairê Viana**

Projeto desenvolvido como parte da minha jornada de estudos em Python, automação e desenvolvimento de soluções práticas.

Este projeto representa uma etapa importante do meu aprendizado: sair da execução de exercícios isolados e começar a utilizar programação para **identificar problemas reais, construir soluções e medir o impacto delas no meu próprio dia a dia**.

---

⭐ Se este projeto foi útil ou interessante, considere deixar uma estrela no repositório.
