#!/usr/bin/python3
""" Gather data from an API """


if __name__ == '__main__':
    import requests
    import sys
    USER_ID = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    """ making requests and getting information from the API """
    tasks_completed = requests.get(
        todos_url,
        params={
            'completed': 'true',
            'userId': USER_ID}).json()
    all_tasks = requests.get(todos_url, params={'userId': USER_ID}).json()
    user_info = requests.get(users_url, params={'id': USER_ID}).json()

    """ filtering useful information """
    EMPLOYEE_NAME = user_info[0]['name']
    NUMBER_OF_DONE_TASKS = len(tasks_completed)
    TOTAL_NUMBER_OF_TASKS = len(all_tasks)

    """ printing it """
    print('Employee {} is done with tasks({}/{}):'.format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,
        TOTAL_NUMBER_OF_TASKS))
    for eachtask in tasks_completed:
        print('\t ' + eachtask['title'])
