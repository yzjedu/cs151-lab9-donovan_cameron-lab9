# Algorithm Document


### Purpose: reading file
    ### Name: read_file_name
    ### Parameters: none
    ### Return: file name
    ### Algorithm: 
   1. ask user for file name
   2. while file is not available 
      1. prints error messaging
      2. ask user for file name
   3. return file name

### Purpose: reading file to lists
    ### Name: file_to_list
    ### Parameters: file name
    ### Return: data
    ### Algorithm:
   1. open file
   2. readlines in file and set to data
   3. close the file
   4. return data

   
### Purpose: formate the groups
    ### Name: table_groups
    ### Parameters: lists
    ### Return: formated groups
    ### Algorithm:
   1. output '~' times 20
   2. set table equal to 1
   3. set seat equal to 1
   4. for i in range of 0 to length of data_list
      1. output table #, seat #, data index
      2. add 1 to seat
      3. if seat is equal to 5
         1. add 1 to table
         2. set seat equal to 1
   5. output '~' times 15
   6. return

### Purpose: calling other function
    ### Name: main
    ### Parameters: none
    ### Return: nothing
    ### Algorithm:
   1. call read file
   2. call file to list
   3. call table groups

3. call main function
