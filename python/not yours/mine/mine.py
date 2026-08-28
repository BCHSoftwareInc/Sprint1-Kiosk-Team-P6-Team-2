def main():
    print("+--------------------------------------+")
    print("|          APEX VISITOR CHECK IN       |")
    print("+--------------------------------------+")
    
    # SE: Use input() to capture Name, Company, Email, and Badge Tier
    # SE: Use print() to render the ASCII badge
main()
space = ""
Name=input("Enter_Name ")
Dept=input("Enter_Department/Organization ")
Email=input("Enter_Email/Handle ")
Badge=input("Enter_Badge/Access_Tier ")
#these take the inputs for each to be utilized later
print("+-------------------------------------------+")
print("|           APEX ENTERTAINMENT PASS         |")
print("+-------------------------------------------+")
print("|  ATTENDEE : " + f"{Name.ljust(23):.23}" + "       |")
print("|  ORGANIZATION : " + f"{Dept.ljust(25):.23}" + "   |")
print("|  HANDLE : " + f"{Email.ljust(25):.23}" + "         |")
print("|  BADGE TIER : " + f"{Badge.ljust(25):.23}" + "     |")
print("|  ISSUER : BCH SOFTWARE TERMINAL SYSTEM    |")
print("+-------------------------------------------+")

