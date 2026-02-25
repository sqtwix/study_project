def create_list(n):
    """Создает список от 0 до n-1 используя генератор"""
    return [i for i in range(n)]

if __name__ == "__main__":
    result = create_list(10)
    print(result)
