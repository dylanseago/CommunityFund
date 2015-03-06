from django.db import models
import random


class Placeholder:
    lorem_ipsum = ('Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante '
                   'sollicitudin commodo. Cras purus odio, vestibulum in vulputate at, tempus viverra '
                   'turpis. Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis '
                   'in faucibus.')

    @staticmethod
    def user(user_id):
        return {
            'id': user_id,
            'name': 'User ' + str(user_id)
        }

    @staticmethod
    def project(project_id):
        goal = random.randint(0, 100000)
        funded = random.randint(0, goal)
        return {
            'id': project_id,
            'name': "Project " + str(project_id),
            'description': Placeholder.lorem_ipsum,
            'goal': goal,
            'amount_funded': funded,
            'percent_funded': round((funded / goal) * 100)
        }

    @staticmethod
    def community(community_id):
        return {
            'id': community_id,
            'name': "Community " + str(community_id),
            'description': Placeholder.lorem_ipsum,
            'subscribers': [Placeholder.user(i) for i in range(10)],
            'projects': [Placeholder.project(i) for i in range(5)],
            'comments': [Placeholder.comment(i) for i in range(5)]
        }

    @staticmethod
    def comment(user_id):
        return {'user_id': user_id,
                'time': 'August 25, 2014 at 9:30 PM',
                'body': Placeholder.lorem_ipsum}