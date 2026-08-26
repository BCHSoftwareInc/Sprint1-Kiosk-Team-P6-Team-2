def main():
    print("+--------------------------------------+")
    print("|          APEX VISITOR CHECK IN       |")
    print("+--------------------------------------+")
    
    # SE: Use input() to capture Name, Company, Email, and Badge Tier
    # SE: Use print() to render the ASCII badge

main(    )
Name=input("Enter_Name ")
Dept=input("Enter_Department/Organization ")
Email=input("Enter_Email/Handle ")
Badge=input("Enter_Badge/Access_Tier ")
#these take the inputs for each to be utilized later
print("+-------------------------------------------+")
print("|           APEX ENTERTAINMENT PASS         |")
print("+-------------------------------------------+")
print("|  ATTENDEE : " + Name.ljust(30) + "|")
print("|  ORGANIZATION : " + Dept.ljust(26) + "|")
print("|  HANDLE : " + Email.ljust(32) + "|")
print("|  BADGE TIER : " + Badge.ljust(28) + "|")
print("|  ISSUER : BCH SOFTWARE TERMINAL SYSTEM    |")
print("+-------------------------------------------+")