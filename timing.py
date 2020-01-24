import re
import sys
import datetime
import matplotlib.pyplot as plt


def split_text(filename):
    chat = open("Filename.txt",errors='ignore')
    chatText = chat.read()
    return chatText.splitlines()


def groupByHour(AM, PM):
    time_groups = {}

    for i in range(24):
        time_groups[str(i)] = 0 
    for time in AM:
        current_hour = int(time.split(":")[0])

        if current_hour == 12:
            current_hour = 0  
        current_hour = str(current_hour)
        time_groups[current_hour] += 1

    for time in PM:
        current_hour = int(time.split(":")[0])

        if current_hour == 24:
            current_hour = 12

        current_hour = str(current_hour)
        time_groups[current_hour] += 1

    return time_groups


def distributeByAmPm(linesText):
    timeRegex = re.compile("\d+\/\d+\/\d+, (\d+\:\d+)")

    AM, PM = [], []
    for index, line in enumerate(linesText):
        print(index)
        matches = re.findall(timeRegex, line)
        if (len(matches) > 0):
            match = datetime.datetime.strptime(
                matches[0], "%H:%M").strftime('%p')

            if match == "AM":
                AM.append(matches[0])
            else:
                PM.append(matches[0])

    return AM, PM


def plot_graph(time_groups, name):
    plt.bar(range(len(time_groups)), list(
        time_groups.values()), align='center')

    plt.xticks(range(len(time_groups)), list(time_groups.keys()))

    plt.xlabel('Time groups with 1 hour interval')
    plt.ylabel('Frequency')
    plt.title("Timing Analysis - Chat with {0}".format(name.capitalize()))
    plt.show()


def analyze(name):
    linesText = split_text(name)

    AM, PM = distributeByAmPm(linesText)

    time_groups = groupByHour(AM, PM)

    plot_graph(time_groups, name)


analyze(sys.argv[1])