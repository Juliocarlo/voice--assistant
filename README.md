# voice--assistant

Este projeto tem como objetivo realizar gravação de áudio pelo navegador ou upload de arquivos de áudio, aplicar corte automático caso o tempo exceda sessenta segundos, 
transcrever o conteúdo utilizando o modelo Whisper e sintetizar a fala do texto transcrito com a biblioteca gTTS. O fluxo completo envolve captura, processamento, 
transcrição e resposta em áudio, permitindo uma interação prática e automatizada dentro do ambiente Google Colab.
A instalação inicial requer os pacotes openai-whisper, gTTS, ffmpeg-python, numpy e torch. Estes pacotes garantem respectivamente a transcrição de áudio, a conversão de 
texto em fala, o processamento de arquivos multimídia, operações matemáticas e suporte ao modelo de aprendizado de máquina. O projeto também utiliza bibliotecas padrão do 
Python como os, time, base64, wave, contextlib e subprocess, além de recursos específicos do Colab como IPython.display, google.colab.files e google.colab.output.
A função gravar_navegador permite capturar áudio diretamente pelo navegador, com limite máximo de sessenta segundos. Caso o usuário solicite tempo superior, o sistema 
restringe automaticamente. O áudio é gravado em formato WAV e salvo como entrada.wav. Para isso, é utilizado código JavaScript integrado ao Colab que acessa o microfone, 
grava o fluxo e converte em base64 para ser processado pelo Python. O callback saveAudio é responsável por decodificar o áudio recebido e salvar o arquivo localmente.
A função cortar_audio verifica a duração do arquivo WAV e, se ultrapassar o limite estabelecido, utiliza o ffmpeg para cortar o áudio e salvar em entrada_cortada.wav. 
Caso o arquivo não esteja em formato WAV, o sistema informa que não foi possível calcular a duração, mas ainda assim tenta processar com Whisper.
A função transcrever_audio carrega o modelo Whisper na versão base e realiza a transcrição do arquivo de áudio, retornando o texto reconhecido. Em seguida, a função 
falar_texto utiliza gTTS para sintetizar o texto transcrito em voz, salvando em resposta.mp3 e exibindo o áudio no Colab.
O fluxo principal é controlado pela função main. O usuário escolhe entre gravar pelo navegador ou fazer upload de um arquivo. No caso de gravação, o áudio é salvo como 
entrada.wav. No caso de upload, o arquivo é processado e cortado se necessário. Após a captura, o áudio é transcrito, o texto é exibido junto com a data e hora da 
transcrição e, em seguida, convertido em voz sintetizada. O sistema também apresenta informações de tempo total de execução e marcações de data e hora para cada etapa: 
gravação, transcrição e resposta.
Em resumo, este projeto integra captura de áudio, processamento de duração, transcrição automática com Whisper e síntese de voz com gTTS, oferecendo uma solução 
completa para transformar fala em texto e texto em fala dentro do ambiente Google Colab.
