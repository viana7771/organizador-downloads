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
    'arquivo.xyz'
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
    caminho_arquivo = origem / arquivo
    caminho_arquivo.touch()

for arquivo in arquivos:
    origem_arquivo = origem / arquivo
    destino_arquivo = destino / arquivo

    shutil.move(origem_arquivo, destino_arquivo)

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
            shutil.move(
                arquivo,
                pasta_destino
            )
            print(f'O arquivo --> {arquivo.name} <--\nFoi movido para pasta --> {pasta_destino.name} <-- com sucesso!\n')

        else:
            pasta_outros = destino / 'Outros'
            pasta_outros.mkdir(
                parents=True,
                exist_ok=True
            )
            shutil.move(
                arquivo,
                pasta_outros
            )
            print(f'O arquivo --> {arquivo.name} <--\nFoi movido para pasta --> {pasta_outros.name} <-- com sucesso!\n') 
