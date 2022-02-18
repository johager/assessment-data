log_file = open("um-server-01.txt")  # open the txt file


def sales_reports(log_file):  # make the function sales_reports
    for line in log_file:  # loop over all lines in the file
        line = line.rstrip()  # remove trailing characters from the line
        day = line[0:3]  # extract the day-of-the-week (the first 3 characters of the line)
        if day == "Tue":  # if day is 'Tue'
            print(line)  # print the whole line of data


sales_reports(log_file)  # execute the sales_reports function on log_file

log_file.close()  # close the log_file reader