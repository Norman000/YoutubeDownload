from subprocess import call


def song(e):
    name = e.get()
    print('Fazendo o download da música: {}'.format(name))

    search = ["ytsearch:" + name]
    command = ['youtube-dl', '-o', '/Downloads/Musicas/%(title)s.%(ext)s+']
    audio_format = "-x --audio-format mp3".split()
    search.extend(audio_format)
    command.extend(search)
    call(command, shell=False)
    print()
