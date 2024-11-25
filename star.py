def star(x: int):
    if not isinstance(x, int) or x < 0 or x % 2 == 0:
        return "Error"
    result = ""
    r = (x + 1) // 2
    c = lambda x, y: ((x + r)**2 + (y + r)**2)**0.5
    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if c(x, y) <= r or c(-x, y) <= r or c(x, -y) <= r or c(-x, -y) <= r:
                result += "# "
                continue
            result += "  "
        result += "\n"
    return result[:-1]

if __name__ == "__main__":
    print(star(71))