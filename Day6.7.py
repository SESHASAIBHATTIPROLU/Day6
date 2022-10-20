import statistics
 
data = [0,160,180,270,160,230,210,190,0]
 
# Finding Mean
print("\nMean: ", statistics.mean(data))
 
# Finding Median
print("Median: ", statistics.median(data))
 
# Finding Single Mode
print("Single Mode: ", statistics.mode(data))
 
# Finding Multiple Modes
print("Mode: ", statistics.multimode(data))
