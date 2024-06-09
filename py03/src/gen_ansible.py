import yaml

# Задача для установки пакетов
def create_install_packages_task(packages):
    return {
        'name': 'Install packages',
        'package':
            {
                'name': packages,
                'state': 'present'
            }
    }

# Задача для копирования файлов
def create_copy_files_task(files):
    tasks = []
    for file in files:
        tasks.append({
            'name': f'Copy {file}',
            'copy': {
                'src': file,
                'dest': f'/remote/path/{file}'
            }
        })
    return tasks

# Задача для выполнения файлов с аргументами
def create_execute_files_task(files, args):
    tasks = []
    for file in files:
        tasks.append({
            'name': f'Execute {file} with arguments',
            'command': f'python3 /remote/path/{file} -e {",".join(args)}'
        })
    return tasks

def main():
    with open('todo.yml', 'r') as file:
        todo_data = yaml.safe_load(file)

    tasks = []

    # Добавление задач по установке пакетов
    if 'install_packages' in todo_data['server']:
        tasks.append(create_install_packages_task(todo_data['server']['install_packages']))

    # Добавление задач по копированию файлов
    if 'exploit_files' in todo_data['server']:
        tasks.extend(create_copy_files_task(todo_data['server']['exploit_files']))

    # Добавление задач по выполнению файлов с аргументами
    if 'exploit_files' in todo_data['server'] and 'bad_guys' in todo_data:
        tasks.extend(create_execute_files_task(todo_data['server']['exploit_files'], todo_data['bad_guys']))

    # Создание конечного словаря для YAML
    deploy_data = {
        'hosts': 'all',
        'tasks': tasks
    }

    with open('deploy.yml', 'w') as file:
        yaml.dump(deploy_data, file, default_flow_style=False)

if __name__ == "__main__":
    main()

