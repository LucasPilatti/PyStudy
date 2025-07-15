# Exercício
'''
Criar lista de tarefas com desfazer e refazer
todo = [] -> lista de tarefas
todo = ['fazer café'] -> Adicionar fazer café
todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer = ['fazer café'] -> Refazer ['caminhar']
desfazer = [] -> Refazer ['caminhar', 'fazer café']
refazer = todo ['fazer café']
refazer = todo ['fazer café', 'caminhar]
'''
import os
task_list = []
redo_store = []
'''
def undo(a=task_list, b=redo_store):
    return b.append(a.pop())  

def redo(task_list, redo_store):
    return task_list.append(redo_store.pop())
'''

while True:
    act = input('Comandos: listar, desfazer, refazer \n Digite uma tarefa ou comando: ')
    os.system('cls')
    
    if act.lower() == 'listar':
        if task_list:
            print(task_list)
        else:
            print('Lista vazia')

    elif act.lower() == 'desfazer':
        if task_list:
            redo_store.append(task_list.pop())
        else:
            print('Nada a desfazer')

    elif act.lower() == 'refazer':
        if redo_store:
            task_list.append(redo_store.pop())
        else:
            print('Nada a refazer')

    else:
        task_list.append(act)
