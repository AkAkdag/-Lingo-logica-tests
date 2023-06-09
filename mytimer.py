import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.totaal_verstreken_time = 0

    def start(self):
        self.start_time = time.time()
    
    # Functie om timer te resetten
    def reset(self):
        self.start_time = None
        self.totaal_verstreken_time = 0


    # Functie om timer te stoppen
    def stop(self):
        if self.start_time is not None:
            verstreken_time = time.time() - self.start_time
            self.totaal_verstreken_time += verstreken_time
            self.start_time = None
    # Functie om de verstreken tijd te berekenen
    def get_verstreken_time(self):
        if self.start_time is not None:
            verstreken_time = time.time() - self.start_time
            return self.totaal_verstreken_time + verstreken_time
        return self.totaal_verstreken_time
