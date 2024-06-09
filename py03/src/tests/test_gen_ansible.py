import yaml
import pytest
import gen_ansible

def test_gen_ansible():
    # Чтение сгенерированного deploy.yml
    with open('deploy.yml', 'r') as file:
        deploy_data = yaml.safe_load(file)

    # Проверка структуры deploy.yml
    assert 'hosts' in deploy_data
    assert deploy_data['hosts'] == 'all'
    assert 'tasks' in deploy_data

    tasks = deploy_data['tasks']

    # Проверка задач
    assert len(tasks) == 5
    assert tasks[0]['name'] == 'Install packages'
    assert 'package' in tasks[0]
    assert tasks[0]['package']['name'] == ['python3', 'nginx']

    assert tasks[1]['name'] == 'Copy exploit.py'
    assert tasks[2]['name'] == 'Copy consumer.py'
    assert tasks[3]['name'] == 'Execute exploit.py with arguments'
    assert tasks[4]['name'] == 'Execute consumer.py with arguments'

if __name__ == "__main__":
    pytest.main()

