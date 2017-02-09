import csv
import json

def main():
    with open('vehicles.csv', 'r') as f:
      reader = csv.reader(f)
      your_list = list(reader)
    tempLine = []
    count = 0;
    for line in your_list:
        if len(tempLine) != 0:
            if tempLine[0] != line[0] and tempLine[1] != line[1]:
                #print("templine: ", tempLine[0], "line: ", line[0])
                tempLine = line;
                count+=1
                printFunc(tempLine, count);

                # print(tempLine)
            elif tempLine[0] == line[0] and tempLine[1] != line[1]:
                tempLine = line;
                count+=1
                # print(tempLine);
                printFunc(tempLine, count);

            else:
                if tempLine[5] != line[5] or tempLine[6] != line[6] or tempLine[7] != line[7] or tempLine[8] != line[8]:
                    tempLine = line;
                    count+=1;
                    #print(tempLine)
                    printFunc(tempLine, count);
        else:
            tempLine = line
            count+=1;
            # print(tempLine)
            printFunc(tempLine, count);

# def main():
#     with open('vehicles.csv', 'r') as f:
#       reader = csv.reader(f)
#       your_list = list(reader)
#     tempLine = []
#     count = 0;
#     for line in your_list:
#         if len(tempLine) != 0:
#             if tempLine[0][0] != line[0] and tempLine[0][1] != line[1]:
#                 #print("templine: ", tempLine[0], "line: ", line[0])
#                 tempLine.clear();
#                 tempLine.append(line);
#                 count+=1
#                 print(tempLine[0])
#             elif tempLine[0] == line[0] and tempLine[1] != line[1]:
#                 tempLine.clear();
#                 tempLine.append(line);
#                 count+=1
#                 print(tempLine[0]);
#
#             else:
#                 if line not in tempLine:
#                     # if tempLine[5] != line[5] or tempLine[6] != line[6] or tempLine[7] != line[7] or tempLine[8] != line[8]:
#                     #     tempLine = line;
#                     #     count+=1;
#                     tempLine.append(line)
#                     print(tempLine[-1:])
#                     #printFunc(tempLine, count);
#         else:
#             tempLine.append(line)
#             count+=1;
#             print(tempLine)


def printFunc(line, count):
    tab = "    "
    print(tab,"{")
    print(tab,tab, '"model": "tripapp.Car",');
    print(tab, tab, '"pk": ', count, ",");
    print(tab, tab, '"fields": {');
    print(tab*2, tab, "\"car_make\": ","\"",line[0],"\",")
    print(tab*2, tab, "\"car_model\": ","\"",line[1],"\",")
    print(tab*2, tab, "\"car_highway_mpg\": ",line[2],",")
    print(tab*2, tab, "\"car_city_mpg\": ",line[3],",")
    print(tab*2, tab, "\"car_comb_mpg\": ",line[4],",")
    print(tab*2, tab, "\"car_cylinder\": ",line[5],",")
    print(tab*2, tab, "\"car_drive\": ","\"",line[6],"\",")
    print(tab*2, tab, "\"fuel\": ","\"",line[7],"\",")
    #print(tab*2, tab, "\"car_year\": ",line[8])
    print(tab*2, tab, "\"car_year\": ","\"",line[8],"\"")
    #print(tab*2, tab, "\"car_make\": ","\"",line[0],"\",")

    print(tab*2, "}")
    print(tab,"},")



if __name__ == "__main__":
    print("[")
    main()
    print("]")
