# Instalação dos pacotes necessários
!pip install openai-whisper gTTS ffmpeg-python numpy torch

import whisper, os, time, base64, wave, contextlib, subprocess
from gtts import gTTS
from datetime import datetime
from IPython.display import Audio, display, Javascript
from google.colab import files, output

# Função para gravar pelo navegador
def gravar_navegador(segundos=5, nome_arquivo="entrada.wav"):
    if segundos > 60:
        segundos = 60
        print("Tempo solicitado maior que 60 segundos. Restrito para 60 segundos.")
    RECORD = f"""
    const sleep = time => new Promise(resolve => setTimeout(resolve, time))
    const b2text = blob => new Promise(resolve => {{
      const reader = new FileReader()
      reader.onloadend = e => resolve(e.target.result)
      reader.readAsDataURL(blob)
    }})
    var record = async function() {{
      const stream = await navigator.mediaDevices.getUserMedia({{ audio: true }})
      const recorder = new MediaRecorder(stream)
      let data = []
      recorder.ondataavailable = event => data.push(event.data)
      recorder.start()
      await sleep({segundos*1000})
      recorder.stop()
      await new Promise(resolve => recorder.onstop = resolve)
      const audioBlob = new Blob(data, {{ type: 'audio/wav' }})
      const base64data = await b2text(audioBlob)
      google.colab.kernel.invokeFunction('notebook.saveAudio', [base64data], {{}})
    }}
    record()
    """
    display(Javascript(RECORD))

# Callback para salvar o áudio gravado
def saveAudio(b64data):
    header, data = b64data.split(',', 1)
    audio = base64.b64decode(data)
    with open("entrada.wav", "wb") as f:
        f.write(audio)
    print("Áudio gravado pelo navegador e salvo como entrada.wav")

output.register_callback('notebook.saveAudio', saveAudio)

# Função para checar duração e cortar se necessário
def cortar_audio(arquivo, limite=60):
    try:
        with contextlib.closing(wave.open(arquivo,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            duracao = frames / float(rate)
        if duracao > limite:
            print(f"Atenção: o áudio tem {duracao:.2f} segundos. Será cortado para {limite} segundos.")
            arquivo_cortado = "entrada_cortada.wav"
            subprocess.run([
                "ffmpeg", "-y", "-i", arquivo,
                "-t", str(limite),
                arquivo_cortado
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return arquivo_cortado
        else:
            print(f"Duração do áudio: {duracao:.2f} segundos.")
            return arquivo
    except:
        print("Não foi possível calcular a duração (formato não WAV). O Whisper ainda tentará processar.")
        return arquivo

# Funções auxiliares
def transcrever_audio(arquivo):
    modelo = whisper.load_model("base")
    resultado = modelo.transcribe(arquivo)
    return resultado["text"]

def falar_texto(texto, arquivo="resposta.mp3"):
    tts = gTTS(text=texto, lang="pt")
    tts.save(arquivo)
    display(Audio(arquivo))

# Fluxo principal
def main():
    inicio = time.time()
    momento_inicio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Escolha a opção de entrada:")
    print("1 - Gravar pelo navegador (até 60 segundos)")
    print("2 - Fazer upload de arquivo (até 60 segundos)")
    escolha = input("Digite 1 ou 2: ")

    if escolha == "1":
        segundos = int(input("Digite o tempo de gravação em segundos (máx 60): "))
        gravar_navegador(segundos=segundos)
        arquivo_audio = "entrada.wav"
        print("Após a gravação, o arquivo será salvo como entrada.wav")
    else:
        uploaded = files.upload()
        arquivo_audio = list(uploaded.keys())[0]
        arquivo_audio = cortar_audio(arquivo_audio, limite=60)

    texto_transcrito = transcrever_audio(arquivo_audio)
    momento_transcricao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Transcrição ({momento_transcricao}): {texto_transcrito}")

    falar_texto(texto_transcrito)
    momento_resposta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fim = time.time()
    tempo_total = fim - inicio
    print(f"Data/hora da gravação: {momento_inicio}")
    print(f"Data/hora da transcrição: {momento_transcricao}")
    print(f"Data/hora da resposta (voz sintetizada): {momento_resposta}")
    print(f"Tempo total do fluxo: {tempo_total:.2f} segundos")

main()
