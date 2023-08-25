Start
Step 1:
    Declare function to calculate EMI
    Function name->EMI(float principal, float rate, float time)
    float emi
    set r = rate / (12 * 100)
    Set t = time * 12
    Set emi = (principal * rate * pow(1 + rate, time)) / (pow(1 + rate, time) - 1)
    Return emi
Step 2:
    In main()
    Declare variables for principal amount, rate, time, emi
    Take input for principal amount , rate and time.
    Set EMI = calculate_EMI(principal, rate, time)
    Print EMI.
Stop