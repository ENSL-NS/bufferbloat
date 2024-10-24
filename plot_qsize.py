import matplotlib.pyplot as plt

def parse_file(filename):
    times = []
    qsize = []
    with open(filename, 'r') as file:
        for l in file:
            fields = l.strip().split(',')
            if len(fields) != 2:
                continue
            times.append(float(fields[0]))
            qsize.append(int(fields[1]))
    return times, qsize

def plot_queue_length(f):
    times, qsize = parse_file(f)
    plt.figure(figsize=(16, 6))
    
    plt.plot(times, qsize, lw=2, color = 'red')

    plt.ylabel("Packets")
    plt.grid(True)
    plt.xlabel("Seconds")
    plt.title("{}: Number of packets in queue".format(f), fontsize=16)

    return plt
