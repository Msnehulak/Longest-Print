import time
from deep_translator import GoogleTranslator
import gc
import string

CHARACTERS = list(
    string.ascii_lowercase +
    string.ascii_uppercase +
    string.digits +
    string.punctuation +
    string.whitespace
)
TARGET_TRANS = ["de", "cs", "en", "pl", "ja", "zh-TW"] 

class LongestPrint:
    def __init__(self) -> None:
        self.to_print = "Hello World"
        self.stopwatch = []

    def measure(self, id, name, des):
        if not self.stopwatch:
            self.stopwatch.append({
                "id": id,
                "name": name,
                "des": des,
                "time": time.perf_counter(), 
                "duration": 0 
            })
            return

        time_now = time.perf_counter()
        duration = time_now - self.stopwatch[-1]["time"]
        
        self.stopwatch.append({
            "id": id,
            "name": name,
            "des": des,
            "time": time_now, 
            "duration": duration
        })

    def translate(self, target_lang=TARGET_TRANS):
        ret = []
        for lang in target_lang:
            try:
                translated_text = GoogleTranslator(
                    source='auto', 
                    target=lang
                ).translate(self.to_print)
 
                if translated_text:
                    ret.append(translated_text) 
            except Exception as e:
                print(f"Neočekávaná chyba sítě při překladu do '{lang}': {e}")
                
        return ret

    def save_load_from_file(self, temp_file = "temp.txt"):
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write(self.to_print)

        with open(temp_file, 'r', encoding='utf-8') as f:
            load_text = f.read()
        return load_text

    def long_print(self):
        for i in self.to_print:
            for x in CHARACTERS: 
                if x == i:
                    print(x, end="")
        print()

    def main(self):
        print("--- Start")
        self.measure("start", "Start", "Start of print")
        self.to_print = "Hello World"

        tran = self.translate()
        self.measure('tran', 'Translate', 'Translate to other lang')

        load = self.save_load_from_file()
        self.measure('wr', 'W/R to file', 'write and read to file')

        self.long_print()
        self.measure('lp', 'Long print', 'loop in loop print')

        gc.collect()
        self.measure('gc', 'Garbage Collector', 'Force start of GC')
        print("--- End")

    def _check_valid_list(self):
        if not self.stopwatch:
            print("ERROR: Don't have data. Runnig self.main()")
            self.main()

    def get_data(self):
        self._check_valid_list()
        return self.stopwatch

    def print_data(self):
        self._check_valid_list()
        total_time = 0

        print()
        for stamp in self.stopwatch:
            if stamp['id'] == "start": continue

            name = stamp['name']
            duration = stamp['duration']
            des = stamp['des'] 

            print(f"{name:>20} | {duration:.6f}s    {des}")
            total_time += duration

        print(f"{'='*20}=|={'='*20}")
        print(f"{'Total':>15} | {total_time:<6.6f}s")

if __name__ == "__main__":
    app = LongestPrint()
    app.main()
    app.print_data()



