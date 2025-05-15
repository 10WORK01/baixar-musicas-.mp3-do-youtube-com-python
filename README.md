# baixar-musicas-.mp3-do-youtube-com-python
 
1. Instale o Python (se ainda não tiver)
Acesse: https://www.python.org/downloads/

Baixe e instale a versão mais recente do Python 3 (de preferência 3.6 ou superior).

Durante a instalação, marque a opção “Add Python to PATH” para facilitar o uso no terminal.

2. Instale o yt-dlp e FFmpeg
Abra o Prompt de Comando (cmd) ou terminal.

Digite e execute o comando para instalar o yt-dlp:

pip install yt-dlp

Faça o download do FFmpeg no site oficial:

https://ffmpeg.org/download.html

Extraia o arquivo zip e copie o caminho da pasta bin dentro do FFmpeg (onde está o ffmpeg.exe).

Adicione esse caminho ao PATH do sistema para que o Windows reconheça o comando ffmpeg:

Pesquise por “variáveis de ambiente” no Windows.

Edite a variável Path e adicione o caminho completo da pasta bin.

Salve e feche.

Para testar, abra um novo terminal e digite:

CMD DO WINDOWS:

ffmpeg -version

Se aparecer a versão do ffmpeg, está tudo certo!

depois disso vc precisa criar uma pasta com um nome qualquer, cole o arquivo .py nesta pasta 
voce precisa editar o arquivo para colocar a URL, salve e execute.
irá criar uma pasta download com a musica .mp3

Se algo der errado

Confirme que o Python, yt-dlp e ffmpeg estão instalados e configurados corretamente.

Verifique se adicionou o ffmpeg ao PATH.Se algo der errado
Confirme que o Python, yt-dlp e ffmpeg estão instalados e configurados corretamente.

Verifique se adicionou o ffmpeg ao PATH.

