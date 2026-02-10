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

Aqui está a seção de instalação e execução em texto corrido para complementar o seu README:

Para utilizar este projeto é necessário preparar o ambiente com as dependências listadas. A instalação pode ser feita executando o comando pip install -r requirements.txt, 
que instalará automaticamente os pacotes openai-whisper, gTTS, ffmpeg-python, numpy e torch. Após a instalação, o projeto pode ser executado de duas formas: abrindo 
o notebook exemplo_colab.ipynb no Google Colab ou rodando diretamente o arquivo main.py em um ambiente Python configurado. No Colab, o usuário poderá escolher entre gravar 
áudio pelo navegador ou fazer upload de um arquivo. A gravação é limitada a sessenta segundos e salva o arquivo como entrada.wav. No caso de upload, o sistema verifica a 
duração e corta o áudio se necessário. Em seguida, o áudio é transcrito pelo modelo Whisper e convertido em voz sintetizada com gTTS, gerando o arquivo resposta.mp3. 
Durante o processo, o sistema informa a data e hora de cada etapa e o tempo total de execução. Essa sequência garante que qualquer usuário consiga instalar, configurar e 
executar o projeto sem dificuldades.

Aqui está a seção de exemplos de uso em texto corrido para complementar o seu README:

Após instalar as dependências e configurar o ambiente, o usuário pode executar o projeto escolhendo entre duas opções de entrada. Na primeira opção, é possível gravar 
áudio diretamente pelo navegador, definindo o tempo de gravação em segundos, limitado a sessenta. O arquivo resultante será salvo como entrada.wav e processado automaticamente. 
Na segunda opção, o usuário pode fazer upload de um arquivo de áudio. Caso o arquivo ultrapasse sessenta segundos, o sistema corta o conteúdo para respeitar o limite, 
gerando entrada_cortada.wav. Em ambos os casos, o áudio é transcrito pelo modelo Whisper e o texto reconhecido é exibido no console junto com a data e hora da transcrição. 
Em seguida, o texto é convertido em voz sintetizada com gTTS, criando o arquivo resposta.mp3, que pode ser reproduzido diretamente no ambiente de execução. Durante todo o 
processo, o sistema informa as etapas realizadas, incluindo gravação, transcrição e resposta, além do tempo total de execução. Esses exemplos demonstram como o fluxo completo 
funciona, desde a captura de áudio até a geração da resposta em voz.

Aqui está a seção detalhando as principais funções e módulos do projeto em texto corrido para complementar o README:

O projeto é composto por funções que organizam o fluxo de captura, processamento e resposta em áudio. A função gravar_navegador é responsável por iniciar a gravação diretamente 
pelo navegador, utilizando código JavaScript integrado ao Google Colab para acessar o microfone e salvar o áudio em formato WAV. A função saveAudio atua como callback, recebendo 
os dados em base64 e convertendo-os em arquivo entrada.wav. A função cortar_audio verifica a duração do arquivo de áudio e, caso ultrapasse sessenta segundos, utiliza o ffmpeg 
para cortar o conteúdo e gerar entrada_cortada.wav. A função transcrever_audio carrega o modelo Whisper na versão base e realiza a transcrição do áudio, retornando o texto 
reconhecido. A função falar_texto utiliza a biblioteca gTTS para converter o texto transcrito em voz sintetizada, salvando o resultado em resposta.mp3 e permitindo a reprodução 
no ambiente de execução. Por fim, a função main organiza todo o fluxo, desde a escolha da entrada pelo usuário até a geração da resposta em áudio, incluindo marcações de data e 
hora em cada etapa e cálculo do tempo total de execução. Essa estrutura modular facilita a compreensão do código, a manutenção e futuras expansões do projeto.

Aqui está a seção final de licença e contribuições em texto corrido para complementar o seu README:

Este projeto é disponibilizado sob a licença MIT, permitindo uso, modificação e distribuição livre, desde que seja mantida a atribuição ao autor original. A escolha dessa licença 
garante flexibilidade para desenvolvedores que desejem adaptar ou expandir o código em diferentes contextos. Quanto às contribuições, qualquer pessoa interessada pode colaborar 
abrindo issues para relatar problemas ou sugerir melhorias, além de enviar pull requests com alterações no código. Recomenda-se que os colaboradores sigam boas práticas de 
programação, mantenham a clareza nos commits e respeitem a estrutura já definida no repositório. Essa abertura para contribuições tem como objetivo incentivar a evolução contínua 
do projeto e fortalecer a comunidade em torno dele.

Aqui está a seção de créditos e referências em texto corrido para complementar o seu README:

Este projeto faz uso de diversas bibliotecas e ferramentas que merecem reconhecimento. A transcrição de áudio é realizada com o modelo Whisper, desenvolvido pela OpenAI, enquanto 
a síntese de voz é feita com a biblioteca gTTS, que utiliza o serviço Google Text-to-Speech. O processamento de arquivos multimídia é apoiado pelo ffmpeg, integrado ao Python por 
meio da biblioteca ffmpeg-python. Operações matemáticas e suporte ao modelo de aprendizado de máquina são fornecidos pelo numpy e pelo torch. O ambiente Google Colab é utilizado 
como plataforma principal de execução, permitindo integração com JavaScript para captura de áudio pelo navegador e manipulação de arquivos. Além disso, agradece-se a comunidade 
open source que mantém e atualiza essas ferramentas, possibilitando a criação de soluções práticas e acessíveis. Para mais detalhes técnicos, recomenda-se consultar a documentação 
oficial de Whisper, gTTS, ffmpeg e Google Colab.


