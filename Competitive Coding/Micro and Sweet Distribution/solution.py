T = int(input().strip())

for _ in range(T):
        rowCount,columnCount = [int(ele) for ele in input().strip().split(" ")]
        startingRow,startingColumn = [int(ele) for ele in input().strip().split(" ")]
        MicroRow, MicroColumn = [int(ele) for ele in input().strip().split(" ")]
    
        if(startingRow == 1 and startingColumn == 1):
            if(columnCount == 1):
                if(MicroRow == rowCount):
                    print("Over")
                else:
                    print("Down")
            elif(MicroRow == rowCount and MicroColumn == columnCount and rowCount%2 != 0):
                print("Over")
            elif(MicroRow == rowCount and MicroColumn == 1 and rowCount%2 == 0):
                print("Over")
            else:
                if(MicroRow%2 == 0):
                    if(MicroColumn == 1):
                        print("Back")
                    else:
                        print("Left")
                else:
                    if(MicroColumn == columnCount):
                        print("Back")
                    else:
                        print("Right")
        elif(startingRow == 1 and startingColumn == columnCount ):
            if(columnCount == 1):
                if(MicroRow == rowCount):
                    print("Over")
                else:
                    print("Down")
            elif(MicroRow == rowCount and MicroColumn == 1 and rowCount%2 != 0):
                print("Over")
            elif(MicroRow == rowCount and MicroColumn == columnCount and rowCount%2 == 0):
                print("Over")
            else:
                if(MicroRow%2 == 0):
                    if(MicroColumn == columnCount):
                        print("Back")
                    else:
                        print("Right")
                else:
                    if(MicroColumn == 1):
                        print("Back")
                    else:
                        print("Left")
        if(startingRow == rowCount and startingColumn == 1):
            if(columnCount == 1):
                if(MicroRow == 1):
                    print("Over")
                else:
                    print("Front")
            elif(rowCount%2 != 0):
                if(MicroRow == 1 and MicroColumn == columnCount):
                    print("Over")
                else:
                    if(MicroRow%2 == 0):
                        if(MicroColumn == 1):
                            print("Front")
                        else:
                            print("Left")
                    else:
                        if(MicroColumn == columnCount):
                            print("Front")
                        else:
                            print("Right")
            else:
                if(MicroRow == 1 and MicroColumn == 1):
                    print("Over")
                else:
                    if(MicroRow%2 != 0):
                        if(MicroColumn == 1):
                            print("Front")
                        else:
                            print("Left")
                    else:
                        if(MicroColumn == columnCount):
                            print("Front")
                        else:
                            print("Right")
        if(startingRow == rowCount and startingColumn == columnCount):
            if(columnCount == 1):
                if(MicroRow == 1):
                    print("Over")
                else:
                    print("Front")
            elif(startingRow %2 !=0 ):
                if(MicroRow == 1 and MicroColumn == 1):
                    print("Over")
                else:
                    if(MicroRow%2 == 0):
                        if(MicroColumn == columnCount):
                            print("Front")
                        else:
                            print("Right")
                    else:
                        if(MicroColumn == 1):
                            print("Front")
                        else:
                            print("Left")
            else:
                if(MicroRow == 1 and MicroColumn == columnCount):
                    print("Over")
                else:
                    if(MicroRow%2 != 0):
                        if(MicroColumn == columnCount):
                            print("Front")
                        else:
                            print("Right")
                    else:
                        if(MicroColumn == 1):
                            print("Front")
                        else:
                            print("Left")
							