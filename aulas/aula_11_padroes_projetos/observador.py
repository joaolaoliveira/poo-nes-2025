class Subject:
    def __init__(self) -> None:
        self._observers = []
        self._state = None

    def attach(self, observer) -> None:
        if observer not in self._observers :
            self._observers.append(observer)

    def detach(self, observer) -> None:
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self) -> None | str:
        return self._state
    
    @state.setter
    def state(self, value : str) -> None:
        self._state = value
        self.notify()


class Observer:
    def update(self, subject : Subject):
        print(f"Observer: O estado do sujeito mudou para {subject.state}")


# Cria o sujeito
sujeito = Subject()

# Cria o observador
observador_1 =  Observer()
observador_2 = Observer()

# Adiciona observador ao sujetito
sujeito.attach(observador_1)

# Altera o estado do sujeito
sujeito.state = "estado 1"
sujeito.state = "estado 2"

# Remove o observador e altera o estado novamente
sujeito.detach(observador_1)
sujeito.state = "estado 3"
