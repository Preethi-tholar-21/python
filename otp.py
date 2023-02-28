import math, random #importing necessary modules

 # function to generate OTP

def generateOTP() :

 # Declare a digits variable which stores all digits

    digits = "0123456789"
    OTP = ""
# we can change the length of otp by changing value in the range

    for i in range(5) :

        OTP += digits[math.floor(random.random() * 10)]

 

    return OTP

 

# Driver code

if __name__ == "__main__" :

     

    print("OTP of 4 digits:", generateOTP())