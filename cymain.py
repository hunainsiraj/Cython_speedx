from adjusted_functions import weighted_levenshtein

def main():
    # Ejemplo de matriz de pesos, debe tener este formato
    # Example of weight matrix, it must have this format
    weight_dict = {
    ('substitute', '®', 'R', 'middle'): 0.9,
    ('substitute', '$', 'S', 'middle'): 0.97,
    ('substitute', '$', 'X', 'middle'): 0.99,
    ('substitute', 'A', 'E', 'middle'): 0.9,
    ('substitute', 'A', 'I', 'middle'): 0.97,
    ('substitute', 'A', 'O', 'middle'): 0.9,
    ('substitute', 'A', 'U', 'middle'): 0.97,
    ('substitute', 'B', 'D', 'middle'): 0.97,
    ('substitute', 'B', 'F', 'middle'): 0.99,
    ('substitute', 'B', 'P', 'middle'): 0.97,
    ('substitute', 'Ç', 'H', 'middle'): 0.99,
    ('substitute', 'Ç', 'J', 'middle'): 0.99,
    ('substitute', 'Ç', 'K', 'middle'): 0.99,
    ('substitute', 'Ç', 'W', 'middle'): 0.97,
    ('substitute', 'D', 'P', 'middle'): 0.99,
    ('substitute', 'D', 'T', 'middle'): 0.99,
    ('substitute', 'E', 'I', 'middle'): 0.9,
    ('substitute', 'E', 'O', 'middle'): 0.97,
    ('substitute', 'E', 'U', 'middle'): 0.97,
    ('substitute', 'F', 'P', 'middle'): 0.99,
    ('substitute', 'F', 'S', 'middle'): 0.99,
    ('substitute', 'H', 'J', 'middle'): 0.97,
    ('substitute', 'H', 'W', 'middle'): 0.99,
    ('substitute', 'I', 'O', 'middle'): 0.97,
    ('substitute', 'I', 'U', 'middle'): 0.97,
    ('substitute', 'I', 'Y', 'middle'): 0.99,
    ('substitute', 'J', 'W', 'middle'): 0.99,
    ('substitute', 'K', 'X', 'middle'): 0.99,
    ('substitute', 'L', 'Y', 'middle'): 0.99,
    ('substitute', 'M', 'N', 'middle'): 0.9,
    ('substitute', 'M', 'Ñ', 'middle'): 0.99,
    ('substitute', 'N', 'Ñ', 'middle'): 0.9,
    ('substitute', 'O', 'U', 'middle'): 0.9,
    ('substitute', 'P', 'T', 'middle'): 0.99,
    ('substitute', 'S', 'X', 'middle'): 0.97,
    ('substitute', 'U', 'W', 'middle'): 0.99,
    ('substitute', 'R', '®', 'middle'): 0.9,
    ('substitute', 'S', '$', 'middle'): 0.97,
    ('substitute', 'X', '$', 'middle'): 0.99,
    ('substitute', 'E', 'A', 'middle'): 0.9,
    ('substitute', 'I', 'A', 'middle'): 0.97,
    ('substitute', 'O', 'A', 'middle'): 0.9,
    ('substitute', 'U', 'A', 'middle'): 0.97,
    ('substitute', 'D', 'B', 'middle'): 0.97,
    ('substitute', 'F', 'B', 'middle'): 0.99,
    ('substitute', 'P', 'B', 'middle'): 0.97,
    ('substitute', 'H', 'Ç', 'middle'): 0.99,
    ('substitute', 'J', 'Ç', 'middle'): 0.99,
    ('substitute', 'K', 'Ç', 'middle'): 0.99,
    ('substitute', 'W', 'Ç', 'middle'): 0.97,
    ('substitute', 'P', 'D', 'middle'): 0.99,
    ('substitute', 'T', 'D', 'middle'): 0.99,
    ('substitute', 'I', 'E', 'middle'): 0.9,
    ('substitute', 'O', 'E', 'middle'): 0.97,
    ('substitute', 'U', 'E', 'middle'): 0.97,
    ('substitute', 'P', 'F', 'middle'): 0.99,
    ('substitute', 'S', 'F', 'middle'): 0.99,
    ('substitute', 'J', 'H', 'middle'): 0.97,
    ('substitute', 'W', 'H', 'middle'): 0.99,
    ('substitute', 'O', 'I', 'middle'): 0.97,
    ('substitute', 'U', 'I', 'middle'): 0.97,
    ('substitute', 'Y', 'I', 'middle'): 0.99,
    ('substitute', 'W', 'J', 'middle'): 0.99,
    ('substitute', 'X', 'K', 'middle'): 0.99,
    ('substitute', 'Y', 'L', 'middle'): 0.99,
    ('substitute', 'N', 'M', 'middle'): 0.9,
    ('substitute', 'Ñ', 'M', 'middle'): 0.99,
    ('substitute', 'Ñ', 'N', 'middle'): 0.9,
    ('substitute', 'U', 'O', 'middle'): 0.9,
    ('substitute', 'T', 'P', 'middle'): 0.99,
    ('substitute', 'X', 'S', 'middle'): 0.97,
    ('substitute', 'W', 'U', 'middle'): 0.99,
    ('substitute', '®', 'R', 'start'): 0.9,
    ('substitute', '$', 'S', 'start'): 0.97,
    ('substitute', '$', 'X', 'start'): 0.99,
    ('substitute', 'A', 'E', 'start'): 0.9,
    ('substitute', 'A', 'I', 'start'): 0.97,
    ('substitute', 'A', 'O', 'start'): 0.9,
    ('substitute', 'A', 'U', 'start'): 0.97,
    ('substitute', 'B', 'D', 'start'): 0.97,
    ('substitute', 'B', 'F', 'start'): 0.99,
    ('substitute', 'B', 'P', 'start'): 0.97,
    ('substitute', 'Ç', 'H', 'start'): 0.99,
    ('substitute', 'Ç', 'J', 'start'): 0.99,
    ('substitute', 'Ç', 'K', 'start'): 0.99,
    ('substitute', 'Ç', 'W', 'start'): 0.97,
    ('substitute', 'D', 'P', 'start'): 0.99,
    ('substitute', 'D', 'T', 'start'): 0.99,
    ('substitute', 'E', 'I', 'start'): 0.9,
    ('substitute', 'E', 'O', 'start'): 0.97,
    ('substitute', 'E', 'U', 'start'): 0.97,
    ('substitute', 'F', 'P', 'start'): 0.99,
    ('substitute', 'F', 'S', 'start'): 0.99,
    ('substitute', 'H', 'J', 'start'): 0.97,
    ('substitute', 'H', 'W', 'start'): 0.99,
    ('substitute', 'I', 'O', 'start'): 0.97,
    ('substitute', 'I', 'U', 'start'): 0.97,
    ('substitute', 'I', 'Y', 'start'): 0.99,
    ('substitute', 'J', 'W', 'start'): 0.99,
    ('substitute', 'K', 'X', 'start'): 0.99,
    ('substitute', 'L', 'Y', 'start'): 0.99,
    ('substitute', 'M', 'N', 'start'): 0.9,
    ('substitute', 'M', 'Ñ', 'start'): 0.99,
    ('substitute', 'N', 'Ñ', 'start'): 0.9,
    ('substitute', 'O', 'U', 'start'): 0.9,
    ('substitute', 'P', 'T', 'start'): 0.99,
    ('substitute', 'S', 'X', 'start'): 0.97,
    ('substitute', 'U', 'W', 'start'): 0.99,
    ('substitute', 'R', '®', 'start'): 0.9,
    ('substitute', 'S', '$', 'start'): 0.97,
    ('substitute', 'X', '$', 'start'): 0.99,
    ('substitute', 'E', 'A', 'start'): 0.9,
    ('substitute', 'I', 'A', 'start'): 0.97,
    ('substitute', 'O', 'A', 'start'): 0.9,
    ('substitute', 'U', 'A', 'start'): 0.97,
    ('substitute', 'D', 'B', 'start'): 0.97,
    ('substitute', 'F', 'B', 'start'): 0.99,
    ('substitute', 'P', 'B', 'start'): 0.97,
    ('substitute', 'H', 'Ç', 'start'): 0.99,
    ('substitute', 'J', 'Ç', 'start'): 0.99,
    ('substitute', 'K', 'Ç', 'start'): 0.99,
    ('substitute', 'W', 'Ç', 'start'): 0.97,
    ('substitute', 'P', 'D', 'start'): 0.99,
    ('substitute', 'T', 'D', 'start'): 0.99,
    ('substitute', 'I', 'E', 'start'): 0.9,
    ('substitute', 'O', 'E', 'start'): 0.97,
    ('substitute', 'U', 'E', 'start'): 0.97,
    ('substitute', 'P', 'F', 'start'): 0.99,
    ('substitute', 'S', 'F', 'start'): 0.99,
    ('substitute', 'J', 'H', 'start'): 0.97,
    ('substitute', 'W', 'H', 'start'): 0.99,
    ('substitute', 'O', 'I', 'start'): 0.97,
    ('substitute', 'U', 'I', 'start'): 0.97,
    ('substitute', 'Y', 'I', 'start'): 0.99,
    ('substitute', 'W', 'J', 'start'): 0.99,
    ('substitute', 'X', 'K', 'start'): 0.99,
    ('substitute', 'Y', 'L', 'start'): 0.99,
    ('substitute', 'N', 'M', 'start'): 0.9,
    ('substitute', 'Ñ', 'M', 'start'): 0.99,
    ('substitute', 'Ñ', 'N', 'start'): 0.9,
    ('substitute', 'U', 'O', 'start'): 0.9,
    ('substitute', 'T', 'P', 'start'): 0.99,
    ('substitute', 'X', 'S', 'start'): 0.97,
    ('substitute', 'W', 'U', 'start'): 0.99,
    ('substitute', '®', 'R', 'end'): 0.9,
    ('substitute', '$', 'S', 'end'): 0.97,
    ('substitute', '$', 'X', 'end'): 0.99,
    ('substitute', 'A', 'E', 'end'): 0.9,
    ('substitute', 'A', 'I', 'end'): 0.97,
    ('substitute', 'A', 'O', 'end'): 0.9,
    ('substitute', 'A', 'U', 'end'): 0.97,
    ('substitute', 'B', 'D', 'end'): 0.97,
    ('substitute', 'B', 'F', 'end'): 0.99,
    ('substitute', 'B', 'P', 'end'): 0.97,
    ('substitute', 'Ç', 'H', 'end'): 0.99,
    ('substitute', 'Ç', 'J', 'end'): 0.99,
    ('substitute', 'Ç', 'K', 'end'): 0.99,
    ('substitute', 'Ç', 'W', 'end'): 0.97,
    ('substitute', 'D', 'P', 'end'): 0.99,
    ('substitute', 'D', 'T', 'end'): 0.99,
    ('substitute', 'E', 'I', 'end'): 0.9,
    ('substitute', 'E', 'O', 'end'): 0.97,
    ('substitute', 'E', 'U', 'end'): 0.97,
    ('substitute', 'F', 'P', 'end'): 0.99,
    ('substitute', 'F', 'S', 'end'): 0.99,
    ('substitute', 'H', 'J', 'end'): 0.97,
    ('substitute', 'H', 'W', 'end'): 0.99,
    ('substitute', 'I', 'O', 'end'): 0.97,
    ('substitute', 'I', 'U', 'end'): 0.97,
    ('substitute', 'I', 'Y', 'end'): 0.99,
    ('substitute', 'J', 'W', 'end'): 0.99,
    ('substitute', 'K', 'X', 'end'): 0.99,
    ('substitute', 'L', 'Y', 'end'): 0.99,
    ('substitute', 'M', 'N', 'end'): 0.9,
    ('substitute', 'M', 'Ñ', 'end'): 0.99,
    ('substitute', 'N', 'Ñ', 'end'): 0.9,
    ('substitute', 'O', 'U', 'end'): 0.9,
    ('substitute', 'P', 'T', 'end'): 0.99,
    ('substitute', 'S', 'X', 'end'): 0.97,
    ('substitute', 'U', 'W', 'end'): 0.99,
    ('substitute', 'R', '®', 'end'): 0.9,
    ('substitute', 'S', '$', 'end'): 0.97,
    ('substitute', 'X', '$', 'end'): 0.99,
    ('substitute', 'E', 'A', 'end'): 0.9,
    ('substitute', 'I', 'A', 'end'): 0.97,
    ('substitute', 'O', 'A', 'end'): 0.9,
    ('substitute', 'U', 'A', 'end'): 0.97,
    ('substitute', 'D', 'B', 'end'): 0.97,
    ('substitute', 'F', 'B', 'end'): 0.99,
    ('substitute', 'P', 'B', 'end'): 0.97,
    ('substitute', 'H', 'Ç', 'end'): 0.99,
    ('substitute', 'J', 'Ç', 'end'): 0.99,
    ('substitute', 'K', 'Ç', 'end'): 0.99,
    ('substitute', 'W', 'Ç', 'end'): 0.97,
    ('substitute', 'P', 'D', 'end'): 0.99,
    ('substitute', 'T', 'D', 'end'): 0.99,
    ('substitute', 'I', 'E', 'end'): 0.9,
    ('substitute', 'O', 'E', 'end'): 0.97,
    ('substitute', 'U', 'E', 'end'): 0.97,
    ('substitute', 'P', 'F', 'end'): 0.99,
    ('substitute', 'S', 'F', 'end'): 0.99,
    ('substitute', 'J', 'H', 'end'): 0.97,
    ('substitute', 'W', 'H', 'end'): 0.99,
    ('substitute', 'O', 'I', 'end'): 0.97,
    ('substitute', 'U', 'I', 'end'): 0.97,
    ('substitute', 'Y', 'I', 'end'): 0.99,
    ('substitute', 'W', 'J', 'end'): 0.99,
    ('substitute', 'X', 'K', 'end'): 0.99,
    ('substitute', 'Y', 'L', 'end'): 0.99,
    ('substitute', 'N', 'M', 'end'): 0.9,
    ('substitute', 'Ñ', 'M', 'end'): 0.99,
    ('substitute', 'Ñ', 'N', 'end'): 0.9,
    ('substitute', 'U', 'O', 'end'): 0.9,
    ('substitute', 'T', 'P', 'end'): 0.99,
    ('substitute', 'X', 'S', 'end'): 0.97,
    ('substitute', 'W', 'U', 'end'): 0.99,
    ('insert', 'H', 'middle'): 0,
    ('delete', 'H', 'middle'): 0,
    ('insert', 'H', 'start'): 0,
    ('delete', 'H', 'start'): 0,
    ('insert', 'H', 'end'): 0,
    ('delete', 'H', 'end'): 0,
    ('delete', 'S', 'end'): 0,
    ('insert', 'S', 'end'): 0,
    ('insert', 'X', 'end'): 0.9,
    ('delete', 'X', 'end'): 0.9,
    ('insert', 'N', 'end'): 0.9,
    ('delete', 'N', 'end'): 0.9,
    ('insert', 'A', 'end'): 0.9,
    ('insert', 'E', 'end'): 0.9,
    ('insert', 'I', 'end'): 0.9,
    ('insert', 'O', 'end'): 0.9,
    ('insert', 'U', 'end'): 0.9,
    ('delete', 'A', 'end'): 0.9,
    ('delete', 'E', 'end'): 0.9,
    ('delete', 'I', 'end'): 0.9,
    ('delete', 'O', 'end'): 0.9,
    ('delete', 'U', 'end'): 0.9,
    }
    # Probar la funcion con string de ejemplo
    # Test the function with an example string
    str1 = "TEXT1"
    str2 = "TEXT2"
    distance, ops  = weighted_levenshtein(str1, str2, weight_dict)
    print(f"The weighted Levenshtein distance between '{str1}' y '{str2}' es: {distance}")
    
    #print(f"La distancia de Levenshtein ponderada entre '{str1}' y '{str2}' es: {distance}")
    print(ops)

if __name__ == "__main__":
    main()
