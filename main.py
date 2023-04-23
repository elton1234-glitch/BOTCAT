import time

time.sleep(2)
print("               -------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print("             //   ______________       _______________     _________________     _______________       ________________     -----------------      //")
time.sleep(1)
print("            //  / **************/    /***************/    /****************/    /**************/      /***************/    /****************/     //")
time.sleep(1)
print("           //  / **************/    /***/       /***/    /****************/    /***/      /***/      /***************/    /****************/     //")
time.sleep(1)
print("          //  /***/       /***/    /***/       /***/           /***/          /***/      /***/      /***/       /***/           /***/           //")
time.sleep(1)
print("         //  /***/_______/***/    /***/       /***/           /***/          /***/                 /***/_______/***/           /***/           //")
time.sleep(1)
print("        //  /***************/    /***/       /***/           /***/          /***/                 /***************/           /***/           //")
time.sleep(1)
print("       //  /***/       /***/    /***/       /***/           /***/          /***/                 /***/       /***/           /***/           //")
time.sleep(1)
print("      //  /***/_______/***/    /***/       /***/           /***/          /***/       /***/     /***/       /***/           /***/           //")
time.sleep(1)
print("     //  /***************/    /***/       /***/           /***/          /***/       /***/     /***/       /***/           /***/           //")
time.sleep(1)
print("    //  /***************/    /***************/           /***/          /***************/     /***/       /***/           /***/           //")
time.sleep(1)
print("      -------------------------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
a = int(input("Enter the first number: "))
time.sleep(1)
b = int(input("Enter the second number: "))
time.sleep(1)
print("******************************************************************************************************************************************************")
print("******************************************************************************************************************************************************")
time.sleep(3)
print(" 1. ADD")
print(" 2. SUBTRACT")
print(" 3. MULTIPLY")
print(" 4. DIVIDE")
print(" 5. ALL")
choice = input("Select any 1 of your choice: ")

#if choice = 1
if choice =="1":
    time.sleep(1)
    sum = a+b;
    print("Sum: "+ str(sum))
    exit(0)
#if choice = 2
elif choice == "2":
    time.sleep(1)
    diff = b-a;
    print("Difference: " + str(diff))
    exit(0)
#if choice = 3
elif choice =="3":
    time.sleep(1)
    prod = a*b;
    print("Product: " + str(prod))
    exit(0)
#if choice = 4
elif choice == "4":
    time.sleep(1)
    quo = a/b;
    print("Quotient: " + str(quo))
    exit(0)
#if choice = 5
else:
    time.sleep(1)
    sum = a+b;
    diff = b-a;
    prod = a*b;
    quo = a/b;
    print("sum: " + str(sum))
    time.sleep(1)
    print("Difference: " + str(diff))
    time.sleep(1)
    print("Product: " + str(prod))
    time.sleep(1)
    print("Quotient: " + str(quo))
    time.sleep(1)
    exit(0)
