from pathlib import Path
import shutil
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from time import sleep

console = Console()

origem = Path('arquivo')
destino = Path('Download')

origem.mkdir(
    parents=True,
    exist_ok=True
)
destino.mkdir(
    parents=True,
    exist_ok=True
)

arquivos = [
    'relatorio.docx',
    'contrato.pdf',
    'tabela.xlsx',
    'apresentacao.pptx',
    'foto_ferias.jpg',
    'logo.png',
    'animacao.gif',
    'musica.mp3',
    'video_aula.mp4',
    'backup.zip',
    'programa.exe',
    'codigo.py',
    'pagina.html',
    'arquivo_sem_extensao',
    'arquivo.xyz',
    'aulas_python.pdf',
    'tarbalho_universitario.docx'
]

pasta_extensoes = {
    '.html': 'HTML',
    '.py': 'PY',
    '.exe': 'EXE',
    '.zip': 'ZIP',
    '.mp4': 'MP4',
    '.mp3': 'MP3',
    '.gif': 'GIF',
    '.png': 'PNG',
    '.jpg': 'JPG',
    '.pptx': 'PPTX',
    '.xlsx': 'XLSX',
    '.docx': 'DOCX',
    '.pdf': 'PDF',
    '.txt': 'TXT'
}

listagem_error ={
    'FileNotFoundError': 'O arquivo ou pasta não foi encrontrado',
    'FileExistsError': 'Algo que Você tentou criar já existe',
    'PermissionError': 'Não tem permissão para realizar a operação',
    'IsADirectoryError': 'Você tratou uma pasta como se fosse um arquivo',
    'NotADirectoryError': 'Você tratou um arquivo como se fosse uma pasta'
}

arquivos_processados = 0
arquivo_movido = 0
arquivo_movido_outros = 0
arquivos_excluidos = 0
arquivos_error = 0

for arquivo in arquivos:
    origem_arquivo = origem / arquivo
    origem_arquivo.touch()
    destino_arquivo = destino / arquivo

    shutil.move(
        origem_arquivo,
        destino_arquivo
    )

for arquivo in destino.iterdir():
    if arquivo.is_file():
        extensao = arquivo.suffix
        arquivos_processados += 1
        if extensao in pasta_extensoes:
            nome_pasta = pasta_extensoes[extensao]
            pasta_destino = destino / nome_pasta
            pasta_destino.mkdir(
                parents=True,
                exist_ok=True
            )

            arquivo_destino = pasta_destino / arquivo.name

            if arquivo_destino.exists():
                arquivo.unlink()
                arquivos_excluidos += 1
            else:
                shutil.move(
                    arquivo,
                    pasta_destino
                )
                arquivo_movido += 1

        else:
            pasta_outros = destino / 'Outros'
            pasta_outros.mkdir(
                parents=True,
                exist_ok=True
            )

            destino_outros = pasta_outros / arquivo.name

            if destino_outros.exists():
                arquivo.unlink()
                arquivos_excluidos += 1

            else:
                shutil.move(
                    arquivo,
                    pasta_outros
                )
                arquivo_movido_outros += 1

print(
    Panel.fit(
        "[bold cyan]Bem-vindo ao Organizador de Arquivos![/bold cyan]\n\n"
        "[white]Automatizando a organização dos seus arquivos "
        "de forma simples, rápida e eficiente.[/white]",
        title=":file_folder: [bold yellow]Organizador de Arquivos[/bold yellow]",
        border_style="cyan",
        padding=(1, 4)
    )
)

with Progress() as progress:
    tarefa = progress.add_task(
        "[yellow]Iniciando processo...",
        total=100
    )

    while not progress.finished:
        progress.update(tarefa, advance=10)
        sleep(0.1)

table = Table(
    title="Relatório Operacional",
    title_style="bold cyan"
)

table.add_column(
    "Tarefas",
    style="yellow"
)

table.add_column(
    "Quantidade",
    justify="center"
)

table.add_row(
    "Arquivos Processados:",
    f"[bold green]{arquivos_processados}[/]"
)

table.add_row(
    "Arquivos Movidos:",
    f"[bold green]{arquivo_movido}[/]"
)

table.add_row(
    "Arquivos em Outros:",
    f"[bold yellow]{arquivo_movido_outros}[/]"
)

table.add_row(
    "Arquivos Excluídos:",
    f"[bold red]{arquivos_excluidos}[/]"
)

print(
    Panel.fit(
        table,
        title="[bold cyan]Resultado da Operação[/bold cyan]",
        border_style="cyan",
        padding=(1, 2)
    )
)