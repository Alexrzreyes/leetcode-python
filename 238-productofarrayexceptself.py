def productExceptSelf(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(n)
    Space Complexity: O(1) (El arreglo de salida no cuenta como memoria extra)
    """
    n = len(nums)
    res = [1] * n
    print(f"Prefix product: {res}")

    # 1. Calcular el producto de los prefijos (elementos a la izquierda)
    prefix = 1
    ejrange = range(n)
    print(f"Range: {ejrange}")
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # 2. Calcular el producto de los sufijos (elementos a la derecha) y multiplicarlo
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

# Casos de prueba
print(productExceptSelf([1, 2, 3, 4])) # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]
