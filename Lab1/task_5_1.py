def is_prime(num):
  
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        #num**0.5 is the square root
        #int() is used to convert the square root to an integer
        #+1 is added to include the square root
        if num % i == 0:
            return False
    return True

def main():
    try:
        print("Search for prime numbers between a and b.")
        a = int(input("Enter number a: "))
        b = int(input("Enter number b: "))

        # Determine start and end because user might input a > b
        start = min(a, b)
        end = max(a, b)

        print(f"Prime numbers in range {start} to {end}:")
        
        found = False
        for num in range(start, end + 1):
            if is_prime(num):
                print(num, end=" ")
                found = True
        
        if not found:
            print("\nNo prime numbers found.")
        print()

    except ValueError:
        print("Error: Please enter valid integers.")

if __name__ == "__main__":
    main()