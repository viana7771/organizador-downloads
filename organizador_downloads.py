from pathlib import Path
import shutil

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
    '.txt': 'TXT',
    '': 'Gerais',
}

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
                print(
                    f'Arquivo -->{arquivo.name}<-- já existe em -->{pasta_destino}\nArquivo será excluido!\n '
                )
            else:
                shutil.move(
                    arquivo,
                    pasta_destino
                )  
                print(
                    f'O arquivo --> {arquivo.name} <--\nFoi movido para pasta --> {pasta_destino.name} <-- com sucesso!\n'
                )

        else:
            pasta_outros = destino / 'Outros'
            pasta_outros.mkdir(
                parents=True,
                exist_ok=True
            )

            destino_outros = pasta_outros / arquivo.name

            if destino_outros.exists():
                arquivo.unlink()
                print(
                    f'Arquivo -->{arquivo.name}<-- já existe em -->{pasta_destino}\nArquivo será excluido!\n '
                )

            else:
                shutil.move(
                    arquivo,
                    pasta_outros
                )
                print(
                    f'O arquivo --> {arquivo.name} <--\nFoi movido para pasta --> {pasta_outros.name} <-- com sucesso!\n'
                ) 
