tarefas = []

def adicionar():
    nova_tarefa = input('Qual a tarefa? ').strip()
    if nova_tarefa:
        tarefas.append({"tarefas": nova_tarefa, "conluído": False})
        print(f"A tarefa", nova_tarefa, "foi adicionado.")
    else:
        print("Não é aceito tarefas em branco.")

def listar():
    if not tarefas:
        print("Não possui tarefas")
    else:
        for i, t in enumerate(tarefas, 1):
            status = 'Ok' if t['conluído'] else 'Fail'
            print(f'{i}. {t['tarefas']} {status}')

def concluir():
    listar()
    try:
        indice = int(input('Diga o número da tarefa concluída: ')) - 1
        if 0 <= indice < len(tarefas):
            print('Tarefa marcada como concluída')
        else:
            print('Número inválido')
    except ValueError:
        print('Número inválido')

def remover():
    listar()
    try:
        indice = int(input('Diga o número da tarefa para remover: '))
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print('Tarefa removida')

        else:
            ('Número inválido')
    except ValueError:
        print('Digite número válido')


def sair():
    pass


menu ={
    "1": adicionar,
    "2": listar,
    "3": concluir,
    "4": remover,
    "5": sair
}

adicionar()
listar()
concluir()
listar()