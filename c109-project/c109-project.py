import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
math_list = df["math"].to_list()
read_list = df["read"].to_list()
#Mean for math and read
math_mean = statistics.mean(math_list)
read_mean = statistics.mean(read_list)
#Median for math and read
math_median = statistics.median(math_list)
read_median = statistics.median(read_list)
#Mode for math and read
math_mode = statistics.mode(math_list)
read_mode = statistics.mode(read_list)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of math is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
print("Mean, Median and Mode of read is {}, {} and {} respectively".format(read_mean, read_median, read_mode))
#Standard deviation for math and read
math_std_deviation = statistics.stdev(math_list)
read_std_deviation = statistics.stdev(read_list)
#1, 2 and 3 Standard Deviations for math
math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)
#1, 2 and 3 Standard Deviations for read
read_first_std_deviation_start, read_first_std_deviation_end = read_mean-read_std_deviation, read_mean+read_std_deviation
read_second_std_deviation_start, read_second_std_deviation_end = read_mean-(2*read_std_deviation), read_mean+(2*read_std_deviation)
read_third_std_deviation_start, read_third_std_deviation_end = read_mean-(3*read_std_deviation), read_mean+(3*read_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for math
math_list_of_data_within_1_std_deviation = [result for result in math_list if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_list_of_data_within_2_std_deviation = [result for result in math_list if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_list_of_data_within_3_std_deviation = [result for result in math_list if result > math_third_std_deviation_start and result < math_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for read
read_list_of_data_within_1_std_deviation = [result for result in read_list if result > read_first_std_deviation_start and result < read_first_std_deviation_end]
read_list_of_data_within_2_std_deviation = [result for result in read_list if result > read_second_std_deviation_start and result < read_second_std_deviation_end]
read_list_of_data_within_3_std_deviation = [result for result in read_list if result > read_third_std_deviation_start and result < read_third_std_deviation_end]
#Printing data for math and read(Standard Deviation)
print("{}% of data for math lies within 1 standard deviation".format(len(math_list_of_data_within_1_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 2 standard deviations".format(len(math_list_of_data_within_2_std_deviation)*100.0/len(math_list)))
print("{}% of data for math lies within 3 standard deviations".format(len(math_list_of_data_within_3_std_deviation)*100.0/len(math_list)))
print("{}% of data for readlies within 1 standard deviation".format(len(read_list_of_data_within_1_std_deviation)*100.0/len(read_list)))
print("{}% of data for readlies within 2 standard deviations".format(len(read_list_of_data_within_2_std_deviation)*100.0/len(read_list)))
print("{}% of data for readlies within 3 standard deviations".format(len(read_list_of_data_within_3_std_deviation)*100.0/len(read_list)))
