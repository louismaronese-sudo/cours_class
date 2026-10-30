def increase_percent(initial_value, after_value):
    try:
        return (after_value / initial_value) * 100
    except ZeroDivisionError:
        return 0
    except Exception as error:
        print("Uh oh, unexpected error occurred!")
        raise error


def main():  
    try:
        initial_value = float(input("Valeur initiale : "))
        after_value = float(input("Valeur après augmentation : "))
    except ValueError:
        print("Erreur : saisis des nombres, avec un point pour les décimales.")
  
    # Appel de la fonction
    result = increase_percent(initial_value, after_value)
    print(f"Augmentation : {result:.1f} %")

if __name__ == "__main__":
    main()

