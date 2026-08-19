from pathlib import Path
import shutil
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

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
    'documento.txt',
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

for arquivo in arquivos:
    origem_arquivo = origem / arquivo
    origem_arquivo.touch()
    destino_arquivo = destino / arquivo

    shutil.move(
        origem_arquivo,
        destino_arquivo
    )

arquivos_processados = 0
arquivo_movido = 0
arquivo_movido_outros = 0
arquivos_excluidos = 0

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
        '[yellow]Organizador de Arquivos, mais expecificamente arquivos de \ndownload, para automatizar tarefas repetitivas [/]',
        title='[bold yellow]AUTOMAÇÃO PYTHON[/] :file_folder:',
        subtitle='[yellow]Facilitando o seu dia a dia[/] ',
        border_style='bold blue'
    )
)

table = Table(
    title='Relatorio Operacional:'
)

table.add_column(
    'Tarefas'
)
table.add_column(
    'Quantidade'
)

table.add_row(
    '[yellow]Arquivos Processados:[/]', f'[bold green]{arquivos_processados}[/]'
)

table.add_row(
    '[yellow]Arquivos Movidos:[/]', f'[bold green]{arquivo_movido}[/]'
)

table.add_row(
    '[yellow]Arquivos em Outros:[/]', f'[bold green]{arquivo_movido_outros}[/]'
)

table.add_row(
    '[yellow]Arquivos Excluidos:[/]', f'[bold red]{arquivos_excluidos}[/]'
)

console = Console()
console.print(table)