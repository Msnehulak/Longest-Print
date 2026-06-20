import time 
from deep_translator import GoogleTranslator

TARGET_TRANS = ["de", "cs", "en", "pl", "ja", "zh-TW"]

stopwatch = []

def measure(name, des = None):
    global stopwatch
    time_now = time.perf_counter()
    duration = time_now - stopwatch[-1]["time"]
    stopwatch.append({"name": name, "time": time_now, "des": des, "duration": duration})

def translate(inp_text, target_lang=TARGET_TRANS):
    ret = []
    for lang in target_lang:
        ret.append(GoogleTranslator(source='auto', target=lang).translate(inp_text))
    return ret

def save_load_from_file(inp_text, temp_file = "temp.txt"):
    with open(temp_file, 'w', encoding='utf-8') as f:
        f.write(inp_text)

    with open(temp_file, 'r', encoding='utf-8') as f:
        load_text = f.read()

    return load_text

# start 
stopwatch.append({"name": "start", "des": "start", "time": time.perf_counter(), "duration": 0})
to_print = "Hello World"

# Translate
trans = translate(to_print)
measure("translate")

# W/R to file
load = save_load_from_file(to_print)
measure('W/R to file', des='write and read to file')

# end 
print(to_print)
measure("end")

# print 
total_time = 0

print()
for stamp in stopwatch:
    if stamp['name'] == "start": continue
    name = str(stamp['name']).capitalize()
    duration = stamp['duration']
    if stamp['des']: des = f" | {stamp['des']}" 
    else: des = ""

    print(f"{name:>15} | {duration:<2.6f}s{des}")
    
    total_time += duration

print(f"{'='*15}=|={'='*15}")
print(f"{'Total':>15} | {total_time:<6.6f}s")

