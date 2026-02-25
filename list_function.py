def create_list(n):
    """Создает список от 0 до n-1 циклом"""
    result = []
    for i in range(n):
	result.append(i)
    return result

if __name__ == "__main__":
    result = create_list(10)
    print(result)
