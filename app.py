import sys
import time
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("=== Temperature Converter (Push 1) ===")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Exit")
    if not sys.stdin.isatty():
        print("Non-interactive mode active (Kubernetes). Running health loop...")
        print(f"Test calculation: 0°C = {celsius_to_fahrenheit(0)}°F")
        while True:
            time.sleep(3600)     
    choice = input("Enter choice (1-2): ").strip()
    if choice == '1':
        cels = float(input("Enter Celsius: "))
        print(f"Result: {celsius_to_fahrenheit(cels)}°F")
if __name__ == "__main__":
    main()
