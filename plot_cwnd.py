import matplotlib.pyplot as plt

IPERF_PORT = '5001'

"""
Sample line:
10662503,10,2.0.19.137,2.0.135.230,5001,34790
"""
def parse_file(filename):
    times = []
    cwnd = []
    with open(filename, 'r') as file:
        for l in file:
            fields = l.strip().split(',')
            if len(fields) != 6:
                continue
            if fields[5] != IPERF_PORT:
                continue
            times.append(float(fields[0]))

            c = int(fields[1])
            cwnd.append(c * 1480 / 1024.0)
    return times, cwnd

def plot_congestion_window(filename, histogram=False):
    times, cwnd = parse_file(filename)
    plt.figure(figsize=(16, 6))

    plt.plot(times, cwnd, lw=2)
    plt.xlabel("seconds")
    plt.ylabel("cwnd KB")
    plt.title("{}: TCP congestion window (cwnd)".format(filename), fontsize=16)
    return plt
