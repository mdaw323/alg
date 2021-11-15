import fileinput
import re

BOTS = 500


bot_values = [[] for i in range(BOTS)]
output = [None for i in range(BOTS)]
lines = [line.strip() for line in fileinput.input()]

# value 61 goes to bot 49

for line in lines:
    match = re.match(r"value (\d+) goes to bot (\d+)", line)
    if match:
        value, bot = map(int, match.groups())
        bot_values[bot].append(value)


for i in range(100):
    # print(f"iter: {i}")
    for line in lines:
        match = re.match(
            r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line)
        if match:
            bot, low_dest, low_number, high_dest, high_number = match.groups()
            bot, low_number, high_number = map(
                int, [bot, low_number, high_number])
            if len(bot_values[bot]) == 2:
                low = min(bot_values[bot])
                high = max(bot_values[bot])
                # print(f"{bot_values[bot]} low: {low} ,high: {high}")
                if (low == 17 and high == 61):
                    print(bot)
                bot_values[bot] = []
                if low_dest == 'output':
                    output[low_number] = low
                    # print (f"bot {bot} output {low_number} value {low}")
                else:
                    bot_values[low_number].append(low)
                if high_dest == 'output':
                    # print (f"bot {bot} output {high_number} value {high}")
                    output[high_number] = high

                else:
                    bot_values[high_number].append(high)

                assert(len(bot_values[low_number]) <= 2)
                assert(len(bot_values[high_number]) <= 2)

print(output[0] * output[1] * output[2])
