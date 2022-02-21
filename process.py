log_file = open("um-server-01.txt")  # open the txt file


def sales_reports(log_file):  # make the function sales_reports
    for line in log_file:  # loop over all lines in the file
        line = line.rstrip()  # remove trailing characters from the line
        day = line[0:3]  # extract the day-of-the-week (the first 3 characters of the line)
        # if day == "Tue":  # if day is 'Tue'
        if day == "Mon":  # if day is 'Mon'
            print(line)  # print the whole line of data


def more_than_ten(log_file):  # make the function more_than_ten
    for line in log_file:  # loop over all lines in the file
        line = line.strip()  # remove leading and trailing characters from the line
        elements = line.split(' ')  # split the line at spaces
        if int(elements[2]) > 10:  # if number sold > 10
            print(line)  # print the whole line of data


def more_than_ten_melons(log_file):  # make the function more_than_ten_melons
    for line in log_file:  # loop over all lines in the file
        line = line.strip()  # remove leading and trailing characters from the line
        if not "cucumber" in line.lower():  # if line doesn't include "cucumber"
            elements = line.split(' ')  # split the line at spaces
            if int(elements[2]) > 10:  # if number sold > 10
                print(line)  # print the whole line of data


print("===\n====== sales_reports =========================================\n===")  # print out a separator
sales_reports(log_file)  # execute the sales_reports function on log_file

log_file.seek(0,0)  # rewind the file

print("===\n====== more_than_ten =========================================\n===")  # print out a separator
more_than_ten(log_file)  # execute the more_than_ten function on log_file

log_file.seek(0,0)  # rewind the file

print("===\n====== more_than_ten_melons =========================================\n===")  # print out a separator
more_than_ten_melons(log_file)  # execute the more_than_ten_melons function on log_file

log_file.close()  # close the log_file reader