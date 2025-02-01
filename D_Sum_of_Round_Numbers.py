def round_numbers(n):
    components = []
    place_value = 1
    
    while n > 0:
        digit = n % 10
        if digit > 0:
            components.append(digit * place_value)
        n //= 10
        place_value *= 10
    
    return components

def main():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        components = round_numbers(n)
        results.append(f"{len(components)}\n" + " ".join(map(str, components)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()