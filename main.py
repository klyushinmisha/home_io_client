import random
import time

from home_io_sdk import HomeIoClient

client = HomeIoClient('testuser', 'TestPassword')

while True:
    telemetry = 1 / random.randint(1, 100)
    print(f'Sent telemetry: {telemetry}')
    client.push_log(
        '29b6e4ff-99b2-456f-a9bf-5288609a63d7',
        {
            'telemetry': telemetry
        },
        'another_test'
    )
    time.sleep(2)

    tasks = client.get_tasks('29b6e4ff-99b2-456f-a9bf-5288609a63d7')
    print(f'Got tasks: {tasks}')
    time.sleep(1)
