from subprocess import call


def video(e):
    name = e.get()
    print('Fazendo o download do vídeo: {}'.format(name))

    search = ["ytsearch:" + name]
    command = ['youtube-dl', '-o', '/Downloads/Videos/%(title)s.%(ext)s+']
    command.extend(search)
    call(command, shell=False)
    print()
