class Topic(object):
    
    def __init__(self):
        self.__users = []

    def register(self, user):
        self.__users.append(user)
    
    def notifyAll(self, *args, **kwargs):
        for user in self.__users:
            user.notify(*args, **kwargs)


class Observer(object):
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, args, ' for ', topic)


class Observer2(object):
    def __init__(self, topic):
        topic.register(self)

    def notify(self, *args, **kwargs):
        print(type(self).__name__, args, ' for ', topic)


if __name__ == "__main__":
    topic = Topic()
    subscribers = []
    
    for i in range(10):
        subscribers.append(Observer(topic))
    for i in range(10):
        subscribers.append(Observer2(topic))

    topic.notifyAll('Thank you !!')