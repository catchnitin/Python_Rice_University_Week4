import statistics
def problem4_2(ran_list):
    """ Compute the mean and standard deviation of a list of floats """
    comp_mean = statistics.mean(ran_list)
    comp_stdev = statistics.stdev(ran_list)
    print(comp_mean)
    print(comp_stdev)